#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mediamatrix Demo - Version 2: Style Moderne Coloré
Interface de démonstration pour l'optimiseur de campagnes médias radio
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Configuration de la page
st.set_page_config(
    page_title="Mediamatrix - Optimisation Radio",
    page_icon="📻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Style CSS moderne et coloré
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }
    
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        background-attachment: fixed;
    }
    
    .block-container {
        background-color: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 10px 40px rgba(0,0,0,0.2);
    }
    
    .stMetric {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
    }
    
    .stMetric label {
        color: rgba(255, 255, 255, 0.9) !important;
        font-weight: 600;
    }
    
    .stMetric [data-testid="stMetricValue"] {
        color: white !important;
        font-size: 2rem !important;
    }
    
    h1 {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
        font-size: 3rem !important;
        margin-bottom: 0.5rem;
    }
    
    h2 {
        color: #667eea;
        font-weight: 600;
    }
    
    h3 {
        color: #764ba2;
        font-weight: 600;
    }
    
    .gradient-box {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 20px;
        border-radius: 15px;
        color: white;
        box-shadow: 0 5px 15px rgba(245, 87, 108, 0.3);
    }
    
    .success-card {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        padding: 20px;
        border-radius: 15px;
        color: white;
        box-shadow: 0 5px 15px rgba(79, 172, 254, 0.3);
    }
    
    .info-card {
        background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
        padding: 20px;
        border-radius: 15px;
        color: white;
        box-shadow: 0 5px 15px rgba(67, 233, 123, 0.3);
    }
    
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 10px 30px;
        font-weight: 600;
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 7px 20px rgba(102, 126, 234, 0.6);
    }
    
    div[data-testid="stDataFrame"] {
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 3px 10px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Données pré-calculées d'optimisation
@st.cache_data
def load_demo_data():
    """Charge les données de démonstration pré-calculées"""
    
    campaign_config = {
        "nom_campagne": "Campagne Nationale Août 2024",
        "client": "Horizon Media (anonymisé)",
        "budget": 30000,
        "periode": "19-21 Août 2024",
        "regies": ["NRJ GLOBAL", "ALTICE", "LAGARDÈRE"],
        "radios": ["Chérie FM", "RMC", "Europe 1", "Fun Radio"],
        "objectif": "Maximiser le GRP total"
    }
    
    optimization_results = {
        "status": "optimal",
        "n_spots": 87,
        "total_grp": 94.35,
        "total_cost": 29850.0,
        "execution_time": 2.43,
        "solver": "SCIP (OR-Tools)",
        "n_variables": 180,
        "n_constraints": 24
    }
    
    spots_data = []
    dates = ['19/08/2024', '20/08/2024', '21/08/2024']
    jours = ['Lundi', 'Mardi', 'Mercredi']
    
    radios_config = {
        'Chérie FM': {'count': 12, 'grp_moy': 0.95, 'prix_moy': 420, 'regie': 'NRJ GLOBAL'},
        'RMC': {'count': 28, 'grp_moy': 1.15, 'prix_moy': 380, 'regie': 'ALTICE'},
        'Europe 1': {'count': 18, 'grp_moy': 0.85, 'prix_moy': 410, 'regie': 'LAGARDÈRE'},
        'Fun Radio': {'count': 29, 'grp_moy': 1.28, 'prix_moy': 350, 'regie': 'NRJ GLOBAL'}
    }
    
    creneaux_prime = ['07:00', '07:30', '17:00', '17:30', '18:00']
    creneaux_standard = ['06:00', '06:30', '08:00', '08:30', '16:00', '16:30', '18:30', '20:00']
    
    spot_id = 1
    for radio, config in radios_config.items():
        spots_per_day = config['count'] // 3
        for i, (date, jour) in enumerate(zip(dates, jours)):
            for j in range(spots_per_day):
                if j % 2 == 0 and creneaux_prime:
                    creneau = creneaux_prime[j % len(creneaux_prime)]
                    prix = int(config['prix_moy'] * 1.3)
                    grp = round(config['grp_moy'] * 1.25, 2)
                else:
                    creneau = creneaux_standard[j % len(creneaux_standard)]
                    prix = config['prix_moy']
                    grp = config['grp_moy']
                
                spots_data.append({
                    'ID': f"S{spot_id:03d}",
                    'Régie': config['regie'],
                    'Radio': radio,
                    'Date': date,
                    'Jour': jour,
                    'Créneau': creneau,
                    'Prix (€)': prix,
                    'GRP': grp,
                    'Ratio GRP/€': round(grp / prix * 1000, 3)
                })
                spot_id += 1
    
    df_spots = pd.DataFrame(spots_data)
    return campaign_config, optimization_results, df_spots

campaign_config, optimization_results, df_spots = load_demo_data()

# ========== HEADER ==========
st.title("📻 Mediamatrix")
st.markdown("### 🚀 Optimisation intelligente de campagnes radio")

# ========== SIDEBAR ==========
with st.sidebar:
    st.markdown("""
    <div style='text-align: center; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 15px; color: white; margin-bottom: 20px;'>
        <h1 style='color: white; margin: 0;'>📻</h1>
        <h2 style='color: white; margin: 10px 0 0 0; font-size: 1.5rem;'>Mediamatrix</h2>
    </div>
    """, unsafe_allow_html=True)
    
    page = st.radio("🎯 Navigation", [
        "🏠 Accueil",
        "📊 Résultats",
        "📈 Analytics",
        "📋 Planning",
        "⚙️ Config"
    ])
    
    st.markdown("---")
    
    st.markdown("""
    <div class='info-card' style='font-size: 0.9rem;'>
        <strong>💡 Le saviez-vous ?</strong><br>
        Mediamatrix optimise vos campagnes en quelques secondes grâce à l'IA et la programmation linéaire !
    </div>
    """, unsafe_allow_html=True)

# ========== PAGE: ACCUEIL ==========
if page == "🏠 Accueil":
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f"""
        <div class='gradient-box'>
            <h2 style='color: white; margin-top: 0;'>🎯 {campaign_config['nom_campagne']}</h2>
            <p style='margin: 5px 0;'><strong>Client:</strong> {campaign_config['client']}</p>
            <p style='margin: 5px 0;'><strong>Période:</strong> {campaign_config['periode']}</p>
            <p style='margin: 5px 0;'><strong>Budget:</strong> {campaign_config['budget']:,} €</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class='success-card'>
            <h3 style='color: white; margin-top: 0;'>✨ Optimisation</h3>
            <p style='font-size: 1.2rem; margin: 5px 0;'><strong>Statut:</strong> {optimization_results['status'].upper()}</p>
            <p style='margin: 5px 0;'><strong>Temps:</strong> {optimization_results['execution_time']}s</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # KPIs avec style moderne
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("🎯 Spots", f"{optimization_results['n_spots']}", delta="sélectionnés")
    
    with col2:
        st.metric("📊 GRP Total", f"{optimization_results['total_grp']:.1f}", delta=f"+{optimization_results['total_grp']:.1f}")
    
    with col3:
        st.metric("💰 Coût", f"{optimization_results['total_cost']/1000:.1f}k€", delta=f"-{(campaign_config['budget'] - optimization_results['total_cost'])/1000:.1f}k€")
    
    with col4:
        ratio = optimization_results['total_grp'] / (optimization_results['total_cost'] / 1000)
        st.metric("⚡ Ratio", f"{ratio:.2f}", delta="GRP/k€")
    
    st.markdown("---")
    
    # Graphiques d'accueil
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🎨 Répartition GRP")
        grp_by_radio = df_spots.groupby('Radio')['GRP'].sum().reset_index()
        fig1 = px.pie(
            grp_by_radio,
            values='GRP',
            names='Radio',
            color_discrete_sequence=px.colors.sequential.Plasma,
            hole=0.5
        )
        fig1.update_traces(textposition='inside', textinfo='percent+label', textfont_size=14)
        fig1.update_layout(height=400, showlegend=True, margin=dict(t=20, b=20, l=20, r=20))
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        st.markdown("### 💎 Top radios (GRP)")
        top_radios = df_spots.groupby('Radio')['GRP'].sum().reset_index().sort_values('GRP', ascending=False)
        fig2 = px.bar(
            top_radios,
            y='Radio',
            x='GRP',
            orientation='h',
            color='GRP',
            color_continuous_scale='Viridis',
            text='GRP'
        )
        fig2.update_traces(texttemplate='%{text:.1f}', textposition='outside')
        fig2.update_layout(height=400, showlegend=False, margin=dict(t=20, b=20, l=20, r=20))
        st.plotly_chart(fig2, use_container_width=True)
    
    st.markdown("---")
    
    # Points forts
    st.markdown("### ✨ Points forts de l'optimisation")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class='info-card'>
            <h4 style='color: white; margin-top: 0;'>🎯 Précision</h4>
            <p>Budget utilisé à <strong>99.5%</strong></p>
            <p>Contraintes 100% respectées</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='success-card'>
            <h4 style='color: white; margin-top: 0;'>⚡ Rapidité</h4>
            <p>Optimisation en <strong>2.43s</strong></p>
            <p>180 variables analysées</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='gradient-box'>
            <h4 style='color: white; margin-top: 0;'>🚀 Performance</h4>
            <p>Ratio GRP/k€: <strong>{:.2f}</strong></p>
            <p>Solution optimale garantie</p>
        </div>
        """.format(optimization_results['total_grp'] / (optimization_results['total_cost'] / 1000)), unsafe_allow_html=True)

# ========== PAGE: RÉSULTATS ==========
elif page == "📊 Résultats":
    st.subheader("📊 Vue d'ensemble des résultats")
    
    # Tableau récapitulatif coloré
    summary = df_spots.groupby('Radio').agg({
        'ID': 'count',
        'GRP': 'sum',
        'Prix (€)': 'sum'
    }).reset_index()
    summary.columns = ['Radio', 'Spots', 'GRP total', 'Coût total (€)']
    summary['% GRP'] = (summary['GRP total'] / summary['GRP total'].sum() * 100).round(1)
    summary['Ratio GRP/k€'] = (summary['GRP total'] / (summary['Coût total (€)'] / 1000)).round(2)
    
    st.dataframe(
        summary.style.format({
            'GRP total': '{:.2f}',
            'Coût total (€)': '{:,.0f}',
            '% GRP': '{:.1f}%',
            'Ratio GRP/k€': '{:.2f}'
        }).background_gradient(cmap='Viridis', subset=['GRP total', 'Coût total (€)']),
        use_container_width=True,
        hide_index=True,
        height=300
    )
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📅 Distribution temporelle")
        daily = df_spots.groupby('Date').agg({'GRP': 'sum', 'ID': 'count'}).reset_index()
        fig3 = go.Figure()
        fig3.add_trace(go.Bar(
            x=daily['Date'],
            y=daily['GRP'],
            name='GRP',
            marker_color='rgb(102, 126, 234)',
            text=daily['GRP'].round(1),
            textposition='outside'
        ))
        fig3.update_layout(height=350, showlegend=False, margin=dict(t=20, b=20, l=20, r=20))
        st.plotly_chart(fig3, use_container_width=True)
    
    with col2:
        st.markdown("### ⏰ Créneaux horaires")
        slots = df_spots.groupby('Créneau').size().reset_index(name='Nombre')
        slots = slots.sort_values('Créneau')
        fig4 = px.area(
            slots,
            x='Créneau',
            y='Nombre',
            color_discrete_sequence=['rgb(118, 75, 162)']
        )
        fig4.update_layout(height=350, showlegend=False, margin=dict(t=20, b=20, l=20, r=20))
        st.plotly_chart(fig4, use_container_width=True)

# ========== PAGE: ANALYTICS ==========
elif page == "📈 Analytics":
    st.subheader("📈 Analyses avancées")
    
    # Heatmap
    st.markdown("### 🔥 Heatmap GRP par jour et créneau")
    pivot_data = df_spots.pivot_table(
        values='GRP',
        index='Créneau',
        columns='Date',
        aggfunc='sum',
        fill_value=0
    )
    
    fig_heat = px.imshow(
        pivot_data,
        labels=dict(x="Date", y="Créneau", color="GRP"),
        color_continuous_scale='Plasma',
        aspect='auto'
    )
    fig_heat.update_layout(height=500)
    st.plotly_chart(fig_heat, use_container_width=True)
    
    st.markdown("---")
    
    # Analyse comparative
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 💰 Coût vs GRP par radio")
        scatter_data = df_spots.groupby('Radio').agg({
            'Prix (€)': 'sum',
            'GRP': 'sum',
            'ID': 'count'
        }).reset_index()
        
        fig_scatter = px.scatter(
            scatter_data,
            x='Prix (€)',
            y='GRP',
            size='ID',
            color='Radio',
            text='Radio',
            color_discrete_sequence=px.colors.qualitative.Vivid,
            size_max=40
        )
        fig_scatter.update_traces(textposition='top center')
        fig_scatter.update_layout(height=400, showlegend=True)
        st.plotly_chart(fig_scatter, use_container_width=True)
    
    with col2:
        st.markdown("### 🏢 Performance par régie")
        regie_perf = df_spots.groupby('Régie').agg({
            'GRP': 'sum',
            'Prix (€)': 'sum'
        }).reset_index()
        regie_perf['Ratio'] = regie_perf['GRP'] / (regie_perf['Prix (€)'] / 1000)
        
        fig_regie = px.bar(
            regie_perf,
            x='Régie',
            y='Ratio',
            color='Régie',
            color_discrete_sequence=px.colors.qualitative.Bold,
            text='Ratio'
        )
        fig_regie.update_traces(texttemplate='%{text:.2f}', textposition='outside')
        fig_regie.update_layout(height=400, showlegend=False, yaxis_title="Ratio GRP/k€")
        st.plotly_chart(fig_regie, use_container_width=True)

# ========== PAGE: PLANNING ==========
elif page == "📋 Planning":
    st.subheader("📋 Planning détaillé")
    
    # Filtres colorés
    col1, col2, col3 = st.columns(3)
    
    with col1:
        filter_radio = st.multiselect("📻 Radio", df_spots['Radio'].unique(), default=df_spots['Radio'].unique())
    with col2:
        filter_date = st.multiselect("📅 Date", df_spots['Date'].unique(), default=df_spots['Date'].unique())
    with col3:
        filter_creneau = st.multiselect("⏰ Créneau", sorted(df_spots['Créneau'].unique()), default=sorted(df_spots['Créneau'].unique()))
    
    df_filtered = df_spots[
        (df_spots['Radio'].isin(filter_radio)) &
        (df_spots['Date'].isin(filter_date)) &
        (df_spots['Créneau'].isin(filter_creneau))
    ]
    
    # Stats rapides
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("🎯 Spots", len(df_filtered))
    with col2:
        st.metric("📊 GRP", f"{df_filtered['GRP'].sum():.1f}")
    with col3:
        st.metric("💰 Coût", f"{df_filtered['Prix (€)'].sum()/1000:.1f}k€")
    with col4:
        st.metric("⚡ Ratio", f"{(df_filtered['GRP'].sum() / (df_filtered['Prix (€)'].sum() / 1000)):.2f}")
    
    st.markdown("---")
    
    # Tableau avec style
    st.dataframe(
        df_filtered.style.format({
            'Prix (€)': '{:,.0f}',
            'GRP': '{:.2f}',
            'Ratio GRP/€': '{:.3f}'
        }).background_gradient(cmap='Purples', subset=['GRP']),
        use_container_width=True,
        height=450
    )
    
    # Export
    csv = df_filtered.to_csv(index=False, encoding='utf-8-sig')
    st.download_button(
        label="📥 Télécharger CSV",
        data=csv,
        file_name=f"mediamatrix_{datetime.now().strftime('%Y%m%d')}.csv",
        mime="text/csv"
    )

# ========== PAGE: CONFIG ==========
elif page == "⚙️ Config":
    st.subheader("⚙️ Configuration")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div class='gradient-box'>
            <h3 style='color: white; margin-top: 0;'>📝 Campagne</h3>
            <p><strong>Nom:</strong> {campaign_config['nom_campagne']}</p>
            <p><strong>Client:</strong> {campaign_config['client']}</p>
            <p><strong>Budget:</strong> {campaign_config['budget']:,} €</p>
            <p><strong>Période:</strong> {campaign_config['periode']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class='info-card'>
            <h3 style='color: white; margin-top: 0;'>📻 Radios</h3>
        """, unsafe_allow_html=True)
        for radio in campaign_config['radios']:
            st.markdown(f"<p style='color: white; margin: 5px 0;'>✓ {radio}</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class='success-card'>
            <h3 style='color: white; margin-top: 0;'>🔧 Optimisation</h3>
            <p><strong>Solveur:</strong> {optimization_results['solver']}</p>
            <p><strong>Variables:</strong> {optimization_results['n_variables']}</p>
            <p><strong>Contraintes:</strong> {optimization_results['n_constraints']}</p>
            <p><strong>Temps:</strong> {optimization_results['execution_time']}s</p>
            <p><strong>Statut:</strong> {optimization_results['status'].upper()}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class='gradient-box'>
            <h3 style='color: white; margin-top: 0;'>🏢 Régies</h3>
        """, unsafe_allow_html=True)
        for regie in campaign_config['regies']:
            st.markdown(f"<p style='color: white; margin: 5px 0;'>✓ {regie}</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# ========== FOOTER ==========
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 15px; color: white;'>
    <h3 style='color: white; margin: 0;'>✨ Mediamatrix</h3>
    <p style='margin: 10px 0 0 0;'>Optimisation intelligente de campagnes médias radio</p>
    <p style='margin: 5px 0 0 0; font-size: 0.9rem;'>Propulsé par OR-Tools | Version Démo 2.0</p>
</div>
""", unsafe_allow_html=True)

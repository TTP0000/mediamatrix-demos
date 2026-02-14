#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mediamatrix Demo - Version 1: Style Professionnel Corporate
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

# Style CSS professionnel
st.markdown("""
<style>
    .main {
        background-color: #f8f9fa;
    }
    .stMetric {
        background-color: white;
        padding: 15px;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    h1 {
        color: #1e3a8a;
        font-weight: 700;
        border-bottom: 3px solid #3b82f6;
        padding-bottom: 10px;
    }
    h2 {
        color: #1e40af;
        font-weight: 600;
    }
    h3 {
        color: #334155;
    }
    .success-box {
        background-color: #dcfce7;
        border-left: 4px solid #22c55e;
        padding: 15px;
        border-radius: 4px;
        margin: 10px 0;
    }
    .info-box {
        background-color: #dbeafe;
        border-left: 4px solid #3b82f6;
        padding: 15px;
        border-radius: 4px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Données pré-calculées d'optimisation (basées sur le test_final_grp_scenarios.py)
@st.cache_data
def load_demo_data():
    """Charge les données de démonstration pré-calculées"""
    
    # Configuration de la campagne
    campaign_config = {
        "nom_campagne": "Campagne Nationale Août 2024",
        "client": "Horizon Media (anonymisé)",
        "budget": 30000,
        "periode": "19-21 Août 2024",
        "regies": ["NRJ GLOBAL", "ALTICE", "LAGARDÈRE"],
        "radios": ["Chérie FM", "RMC", "Europe 1", "Fun Radio"],
        "objectif": "Maximiser le GRP total"
    }
    
    # Résultats d'optimisation (simulés à partir du code)
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
    
    # Spots sélectionnés (échantillon représentatif)
    spots_data = []
    dates = ['19/08/2024', '20/08/2024', '21/08/2024']
    jours = ['Lundi', 'Mardi', 'Mercredi']
    
    # Répartition réaliste basée sur les tests
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
                # Alternance créneau prime / standard
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

# Chargement des données
campaign_config, optimization_results, df_spots = load_demo_data()

# ========== HEADER ==========
st.title("📻 Mediamatrix - Optimiseur de Campagnes Radio")
st.markdown("### Plateforme d'optimisation média basée sur la programmation linéaire")

# ========== SIDEBAR ==========
with st.sidebar:
    st.image("https://via.placeholder.com/250x80/1e3a8a/ffffff?text=Mediamatrix", use_container_width=True)
    st.markdown("---")
    st.markdown("### 🎯 Navigation")
    page = st.radio("", [
        "📊 Vue d'ensemble",
        "📈 Analyse détaillée",
        "📋 Planning spots",
        "⚙️ Configuration"
    ])
    st.markdown("---")
    st.markdown("### ℹ️ À propos")
    st.info("""
    **Mediamatrix** optimise l'allocation de spots publicitaires radio en maximisant le GRP sous contraintes multiples.
    
    **Technologie:** OR-Tools (SCIP)
    """)

# ========== PAGE: VUE D'ENSEMBLE ==========
if page == "📊 Vue d'ensemble":
    
    # Informations campagne
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.markdown(f"""
        **Campagne:** {campaign_config['nom_campagne']}  
        **Client:** {campaign_config['client']}  
        **Période:** {campaign_config['periode']}  
        **Budget alloué:** {campaign_config['budget']:,} €
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="success-box">', unsafe_allow_html=True)
        st.markdown(f"""
        ✅ **Optimisation réussie**  
        Statut: `{optimization_results['status'].upper()}`  
        Temps: {optimization_results['execution_time']}s
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # KPIs principaux
    st.subheader("📊 Indicateurs clés de performance")
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric(
            label="Spots sélectionnés",
            value=f"{optimization_results['n_spots']}",
            delta="spots"
        )
    
    with col2:
        st.metric(
            label="GRP Total",
            value=f"{optimization_results['total_grp']:.2f}",
            delta=f"+{optimization_results['total_grp']:.1f}"
        )
    
    with col3:
        st.metric(
            label="Coût total",
            value=f"{optimization_results['total_cost']:,.0f} €",
            delta=f"-{campaign_config['budget'] - optimization_results['total_cost']:.0f} €"
        )
    
    with col4:
        ratio = optimization_results['total_grp'] / (optimization_results['total_cost'] / 1000)
        st.metric(
            label="Ratio GRP/k€",
            value=f"{ratio:.2f}",
            delta="optimal"
        )
    
    with col5:
        budget_usage = (optimization_results['total_cost'] / campaign_config['budget']) * 100
        st.metric(
            label="Budget utilisé",
            value=f"{budget_usage:.1f}%",
            delta=f"{budget_usage:.1f}%"
        )
    
    st.markdown("---")
    
    # Graphiques principaux
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Répartition GRP par régie")
        grp_by_regie = df_spots.groupby('Régie')['GRP'].sum().reset_index()
        fig1 = px.pie(
            grp_by_regie,
            values='GRP',
            names='Régie',
            color_discrete_sequence=['#1e3a8a', '#3b82f6', '#60a5fa'],
            hole=0.4
        )
        fig1.update_traces(textposition='inside', textinfo='percent+label')
        fig1.update_layout(
            showlegend=True,
            height=350,
            margin=dict(t=20, b=20, l=20, r=20)
        )
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        st.subheader("💰 Répartition coût par radio")
        cost_by_radio = df_spots.groupby('Radio')['Prix (€)'].sum().reset_index()
        cost_by_radio = cost_by_radio.sort_values('Prix (€)', ascending=True)
        fig2 = px.bar(
            cost_by_radio,
            x='Prix (€)',
            y='Radio',
            orientation='h',
            color='Prix (€)',
            color_continuous_scale='Blues'
        )
        fig2.update_layout(
            showlegend=False,
            height=350,
            margin=dict(t=20, b=20, l=20, r=20),
            xaxis_title="Coût total (€)",
            yaxis_title=""
        )
        st.plotly_chart(fig2, use_container_width=True)
    
    # Tableau récapitulatif par radio
    st.subheader("📋 Récapitulatif par radio")
    summary = df_spots.groupby('Radio').agg({
        'ID': 'count',
        'GRP': 'sum',
        'Prix (€)': 'sum',
        'Ratio GRP/€': 'mean'
    }).reset_index()
    summary.columns = ['Radio', 'Nombre de spots', 'GRP total', 'Coût total (€)', 'Ratio GRP/€ moyen']
    summary['% GRP'] = (summary['GRP total'] / summary['GRP total'].sum() * 100).round(1)
    summary['% Coût'] = (summary['Coût total (€)'] / summary['Coût total (€)'].sum() * 100).round(1)
    
    st.dataframe(
        summary.style.format({
            'GRP total': '{:.2f}',
            'Coût total (€)': '{:,.0f}',
            'Ratio GRP/€ moyen': '{:.3f}',
            '% GRP': '{:.1f}%',
            '% Coût': '{:.1f}%'
        }),
        use_container_width=True,
        hide_index=True
    )

# ========== PAGE: ANALYSE DÉTAILLÉE ==========
elif page == "📈 Analyse détaillée":
    st.subheader("📈 Analyse approfondie des résultats")
    
    # Analyse temporelle
    st.markdown("#### 📅 Répartition temporelle")
    col1, col2 = st.columns(2)
    
    with col1:
        # GRP par jour
        grp_by_day = df_spots.groupby('Date')['GRP'].sum().reset_index()
        fig3 = px.bar(
            grp_by_day,
            x='Date',
            y='GRP',
            color='GRP',
            color_continuous_scale='Blues',
            text='GRP'
        )
        fig3.update_traces(texttemplate='%{text:.1f}', textposition='outside')
        fig3.update_layout(
            title="GRP par jour",
            height=350,
            showlegend=False,
            xaxis_title="",
            yaxis_title="GRP"
        )
        st.plotly_chart(fig3, use_container_width=True)
    
    with col2:
        # Nombre de spots par jour
        spots_by_day = df_spots.groupby('Date').size().reset_index(name='Nombre de spots')
        fig4 = px.line(
            spots_by_day,
            x='Date',
            y='Nombre de spots',
            markers=True,
            line_shape='spline'
        )
        fig4.update_traces(line_color='#1e3a8a', marker=dict(size=12, color='#3b82f6'))
        fig4.update_layout(
            title="Volume de spots par jour",
            height=350,
            xaxis_title="",
            yaxis_title="Nombre de spots"
        )
        st.plotly_chart(fig4, use_container_width=True)
    
    st.markdown("---")
    
    # Analyse par créneau
    st.markdown("#### ⏰ Analyse par créneau horaire")
    
    grp_by_slot = df_spots.groupby('Créneau').agg({
        'GRP': 'sum',
        'ID': 'count'
    }).reset_index()
    grp_by_slot.columns = ['Créneau', 'GRP total', 'Nombre de spots']
    grp_by_slot = grp_by_slot.sort_values('Créneau')
    
    fig5 = go.Figure()
    fig5.add_trace(go.Bar(
        x=grp_by_slot['Créneau'],
        y=grp_by_slot['GRP total'],
        name='GRP',
        marker_color='#3b82f6',
        yaxis='y'
    ))
    fig5.add_trace(go.Scatter(
        x=grp_by_slot['Créneau'],
        y=grp_by_slot['Nombre de spots'],
        name='Nombre de spots',
        marker_color='#ef4444',
        yaxis='y2',
        mode='lines+markers'
    ))
    fig5.update_layout(
        title="GRP et volume par créneau horaire",
        xaxis_title="Créneau",
        yaxis=dict(title="GRP total", side='left'),
        yaxis2=dict(title="Nombre de spots", side='right', overlaying='y'),
        height=400,
        hovermode='x unified'
    )
    st.plotly_chart(fig5, use_container_width=True)
    
    st.markdown("---")
    
    # Performance par régie
    st.markdown("#### 🏢 Performance par régie")
    
    perf_regie = df_spots.groupby('Régie').agg({
        'ID': 'count',
        'GRP': ['sum', 'mean'],
        'Prix (€)': ['sum', 'mean'],
        'Ratio GRP/€': 'mean'
    }).reset_index()
    perf_regie.columns = ['Régie', 'Spots', 'GRP total', 'GRP moyen', 'Coût total', 'Coût moyen', 'Ratio moyen']
    
    col1, col2, col3 = st.columns(3)
    
    for idx, (col, regie_name) in enumerate(zip([col1, col2, col3], perf_regie['Régie'].unique())):
        regie_data = perf_regie[perf_regie['Régie'] == regie_name].iloc[0]
        with col:
            st.markdown(f"**{regie_name}**")
            st.metric("Spots", f"{int(regie_data['Spots'])}")
            st.metric("GRP total", f"{regie_data['GRP total']:.2f}")
            st.metric("Coût total", f"{regie_data['Coût total']:,.0f} €")
            st.metric("Ratio GRP/k€", f"{regie_data['Ratio moyen']:.3f}")

# ========== PAGE: PLANNING SPOTS ==========
elif page == "📋 Planning spots":
    st.subheader("📋 Planning détaillé des spots")
    
    # Filtres
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        filter_regie = st.multiselect(
            "Régie",
            options=df_spots['Régie'].unique(),
            default=df_spots['Régie'].unique()
        )
    
    with col2:
        filter_radio = st.multiselect(
            "Radio",
            options=df_spots['Radio'].unique(),
            default=df_spots['Radio'].unique()
        )
    
    with col3:
        filter_date = st.multiselect(
            "Date",
            options=df_spots['Date'].unique(),
            default=df_spots['Date'].unique()
        )
    
    with col4:
        filter_creneau = st.multiselect(
            "Créneau",
            options=sorted(df_spots['Créneau'].unique()),
            default=sorted(df_spots['Créneau'].unique())
        )
    
    # Appliquer les filtres
    df_filtered = df_spots[
        (df_spots['Régie'].isin(filter_regie)) &
        (df_spots['Radio'].isin(filter_radio)) &
        (df_spots['Date'].isin(filter_date)) &
        (df_spots['Créneau'].isin(filter_creneau))
    ]
    
    # Statistiques filtrées
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Spots affichés", len(df_filtered))
    with col2:
        st.metric("GRP total", f"{df_filtered['GRP'].sum():.2f}")
    with col3:
        st.metric("Coût total", f"{df_filtered['Prix (€)'].sum():,.0f} €")
    with col4:
        st.metric("Ratio moyen", f"{df_filtered['Ratio GRP/€'].mean():.3f}")
    
    st.markdown("---")
    
    # Tableau des spots
    st.dataframe(
        df_filtered.style.format({
            'Prix (€)': '{:,.0f}',
            'GRP': '{:.2f}',
            'Ratio GRP/€': '{:.3f}'
        }),
        use_container_width=True,
        height=500
    )
    
    # Bouton export
    csv = df_filtered.to_csv(index=False, encoding='utf-8-sig')
    st.download_button(
        label="📥 Exporter en CSV",
        data=csv,
        file_name=f"mediamatrix_spots_{datetime.now().strftime('%Y%m%d')}.csv",
        mime="text/csv"
    )

# ========== PAGE: CONFIGURATION ==========
elif page == "⚙️ Configuration":
    st.subheader("⚙️ Configuration de la campagne")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📝 Paramètres campagne")
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        for key, value in campaign_config.items():
            if key not in ['regies', 'radios']:
                st.markdown(f"**{key.replace('_', ' ').title()}:** {value}")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("#### 🎯 Objectif d'optimisation")
        st.info(campaign_config['objectif'])
        
    with col2:
        st.markdown("#### 🏢 Régies sélectionnées")
        for regie in campaign_config['regies']:
            st.markdown(f"✓ {regie}")
        
        st.markdown("#### 📻 Radios sélectionnées")
        for radio in campaign_config['radios']:
            st.markdown(f"✓ {radio}")
    
    st.markdown("---")
    
    # Contraintes appliquées
    st.markdown("#### 🔒 Contraintes d'optimisation")
    
    constraints_data = [
        {"Type": "Budget maximal", "Valeur": f"{campaign_config['budget']:,} €", "Statut": "✅ Respectée"},
        {"Type": "Période de diffusion", "Valeur": campaign_config['periode'], "Statut": "✅ Respectée"},
        {"Type": "Sélection régies", "Valeur": f"{len(campaign_config['regies'])} régies", "Statut": "✅ Respectée"},
        {"Type": "Sélection radios", "Valeur": f"{len(campaign_config['radios'])} radios", "Statut": "✅ Respectée"},
    ]
    
    df_constraints = pd.DataFrame(constraints_data)
    st.dataframe(df_constraints, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # Informations techniques
    st.markdown("#### 🔧 Détails techniques de l'optimisation")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Solveur", optimization_results['solver'])
        st.metric("Variables", optimization_results['n_variables'])
    
    with col2:
        st.metric("Contraintes", optimization_results['n_constraints'])
        st.metric("Temps d'exécution", f"{optimization_results['execution_time']}s")
    
    with col3:
        st.metric("Statut solution", optimization_results['status'].upper())
        st.metric("Qualité", "Optimale" if optimization_results['status'] == 'optimal' else "Faisable")

# ========== FOOTER ==========
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #64748b; padding: 20px;'>
    <p><strong>Mediamatrix</strong> - Optimisation de campagnes médias radio</p>
    <p>Propulsé par OR-Tools (SCIP) | Version démo 1.0</p>
</div>
""", unsafe_allow_html=True)

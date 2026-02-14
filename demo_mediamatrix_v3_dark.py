#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mediamatrix Demo - Version 3: Style Data Analytics (Dark Theme)
Interface de démonstration pour l'optimiseur de campagnes médias radio
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Configuration de la page
st.set_page_config(
    page_title="Mediamatrix Analytics - Optimisation Radio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Style CSS Dark Analytics
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Inter:wght@400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    code, pre {
        font-family: 'JetBrains Mono', monospace;
    }
    
    .main {
        background-color: #0a0e27;
        color: #e4e4e7;
    }
    
    .block-container {
        background-color: #0a0e27;
        padding: 2rem;
    }
    
    .stMetric {
        background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
        border: 1px solid #334155;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
    }
    
    .stMetric label {
        color: #94a3b8 !important;
        font-weight: 600;
        text-transform: uppercase;
        font-size: 0.75rem;
        letter-spacing: 0.05em;
    }
    
    .stMetric [data-testid="stMetricValue"] {
        color: #10b981 !important;
        font-family: 'JetBrains Mono', monospace;
        font-size: 1.8rem !important;
        font-weight: 700;
    }
    
    .stMetric [data-testid="stMetricDelta"] {
        color: #06b6d4 !important;
    }
    
    h1 {
        color: #10b981;
        font-weight: 700;
        font-size: 2.5rem !important;
        font-family: 'JetBrains Mono', monospace;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        border-left: 5px solid #10b981;
        padding-left: 15px;
        margin-bottom: 1rem;
    }
    
    h2 {
        color: #06b6d4;
        font-weight: 600;
        font-family: 'JetBrains Mono', monospace;
        border-bottom: 2px solid #334155;
        padding-bottom: 8px;
    }
    
    h3 {
        color: #a78bfa;
        font-weight: 600;
    }
    
    .data-box {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border: 1px solid #334155;
        border-left: 4px solid #10b981;
        padding: 20px;
        border-radius: 8px;
        margin: 10px 0;
        font-family: 'JetBrains Mono', monospace;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
    }
    
    .alert-success {
        background: linear-gradient(135deg, #065f46 0%, #064e3b 100%);
        border: 1px solid #10b981;
        border-left: 4px solid #10b981;
        padding: 15px;
        border-radius: 8px;
        color: #d1fae5;
        font-weight: 600;
    }
    
    .alert-info {
        background: linear-gradient(135deg, #164e63 0%, #0e7490 100%);
        border: 1px solid #06b6d4;
        border-left: 4px solid #06b6d4;
        padding: 15px;
        border-radius: 8px;
        color: #cffafe;
    }
    
    .alert-warning {
        background: linear-gradient(135deg, #78350f 0%, #92400e 100%);
        border: 1px solid #f59e0b;
        border-left: 4px solid #f59e0b;
        padding: 15px;
        border-radius: 8px;
        color: #fef3c7;
    }
    
    .terminal-box {
        background-color: #000000;
        border: 1px solid #10b981;
        border-radius: 8px;
        padding: 15px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.85rem;
        color: #10b981;
        box-shadow: 0 0 20px rgba(16, 185, 129, 0.3);
    }
    
    .stat-card {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border: 1px solid #334155;
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
    }
    
    .stat-card h4 {
        color: #94a3b8;
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin: 0 0 8px 0;
    }
    
    .stat-card .value {
        color: #10b981;
        font-size: 1.8rem;
        font-weight: 700;
        font-family: 'JetBrains Mono', monospace;
        margin: 0;
    }
    
    div[data-testid="stDataFrame"] {
        background-color: #1e293b;
        border: 1px solid #334155;
        border-radius: 8px;
        overflow: hidden;
    }
    
    .stButton>button {
        background: linear-gradient(135deg, #059669 0%, #10b981 100%);
        color: #000000;
        border: none;
        border-radius: 6px;
        padding: 10px 25px;
        font-weight: 700;
        font-family: 'JetBrains Mono', monospace;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        box-shadow: 0 4px 12px rgba(16, 185, 129, 0.4);
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(16, 185, 129, 0.6);
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #0f172a;
        border-right: 1px solid #334155;
    }
    
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
        color: #10b981;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #1e293b;
        border-radius: 8px;
        padding: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: #0f172a;
        color: #94a3b8;
        border-radius: 6px;
        padding: 10px 20px;
        font-family: 'JetBrains Mono', monospace;
        font-weight: 600;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #059669 0%, #10b981 100%);
        color: #000000;
    }
</style>
""", unsafe_allow_html=True)

# Données pré-calculées d'optimisation
@st.cache_data
def load_demo_data():
    """Charge les données de démonstration pré-calculées"""
    
    campaign_config = {
        "nom_campagne": "CAMPAIGN_NATIONAL_AUG_2024",
        "client": "HORIZON_MEDIA_CLIENT_001",
        "budget": 30000,
        "periode": "19-21 Aug 2024",
        "regies": ["NRJ_GLOBAL", "ALTICE", "LAGARDERE"],
        "radios": ["CHERIE_FM", "RMC", "EUROPE_1", "FUN_RADIO"],
        "objectif": "MAXIMIZE_GRP"
    }
    
    optimization_results = {
        "status": "OPTIMAL",
        "n_spots": 87,
        "total_grp": 94.35,
        "total_cost": 29850.0,
        "execution_time": 2.43,
        "solver": "SCIP_OR_TOOLS",
        "n_variables": 180,
        "n_constraints": 24,
        "gap": 0.0,
        "iterations": 1247
    }
    
    spots_data = []
    dates = ['19/08/2024', '20/08/2024', '21/08/2024']
    jours = ['MON', 'TUE', 'WED']
    
    radios_config = {
        'CHERIE_FM': {'count': 12, 'grp_moy': 0.95, 'prix_moy': 420, 'regie': 'NRJ_GLOBAL'},
        'RMC': {'count': 28, 'grp_moy': 1.15, 'prix_moy': 380, 'regie': 'ALTICE'},
        'EUROPE_1': {'count': 18, 'grp_moy': 0.85, 'prix_moy': 410, 'regie': 'LAGARDERE'},
        'FUN_RADIO': {'count': 29, 'grp_moy': 1.28, 'prix_moy': 350, 'regie': 'NRJ_GLOBAL'}
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
                    'SPOT_ID': f"SPOT_{spot_id:04d}",
                    'REGIE': config['regie'],
                    'RADIO': radio,
                    'DATE': date,
                    'DAY': jour,
                    'TIME_SLOT': creneau,
                    'COST_EUR': prix,
                    'GRP': grp,
                    'EFFICIENCY': round(grp / prix * 1000, 3)
                })
                spot_id += 1
    
    df_spots = pd.DataFrame(spots_data)
    return campaign_config, optimization_results, df_spots

campaign_config, optimization_results, df_spots = load_demo_data()

# ========== HEADER ==========
st.title("📊 MEDIAMATRIX ANALYTICS")
st.markdown("### RADIO CAMPAIGN OPTIMIZATION PLATFORM")

# ========== SIDEBAR ==========
with st.sidebar:
    st.markdown("""
    <div class='terminal-box'>
        <div style='color: #06b6d4; margin-bottom: 10px;'>$ mediamatrix --version</div>
        <div>MEDIAMATRIX v3.0.0</div>
        <div>SOLVER: OR-Tools SCIP</div>
        <div>STATUS: <span style='color: #10b981;'>ONLINE</span></div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    page = st.radio("⚡ NAVIGATION", [
        "🏠 DASHBOARD",
        "📊 RESULTS",
        "📈 ANALYTICS",
        "🗓️ SCHEDULE",
        "⚙️ CONFIG",
        "💻 TERMINAL"
    ], label_visibility="visible")
    
    st.markdown("---")
    
    st.markdown("""
    <div class='alert-info' style='font-size: 0.85rem;'>
        <strong>⚡ OPTIMIZATION ENGINE</strong><br>
        Linear programming solver analyzing 180+ variables with 24 constraints in real-time.
    </div>
    """, unsafe_allow_html=True)

# ========== PAGE: DASHBOARD ==========
if page == "🏠 DASHBOARD":
    
    # Campaign info
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown(f"""
        <div class='data-box'>
            <h3 style='color: #10b981; margin-top: 0; font-family: "JetBrains Mono"'>⚡ {campaign_config['nom_campagne']}</h3>
            <code style='color: #94a3b8;'>CLIENT_ID: {campaign_config['client']}</code><br>
            <code style='color: #94a3b8;'>PERIOD: {campaign_config['periode']}</code><br>
            <code style='color: #94a3b8;'>BUDGET: €{campaign_config['budget']:,}</code><br>
            <code style='color: #94a3b8;'>OBJECTIVE: {campaign_config['objectif']}</code>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class='alert-success'>
            <strong>✓ OPTIMIZATION</strong><br>
            STATUS: {optimization_results['status']}<br>
            TIME: {optimization_results['execution_time']}s<br>
            GAP: {optimization_results['gap']:.2%}
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # KPIs - Style terminal
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric("SPOTS_COUNT", f"{optimization_results['n_spots']}", delta=f"+{optimization_results['n_spots']}")
    
    with col2:
        st.metric("GRP_TOTAL", f"{optimization_results['total_grp']:.2f}", delta=f"+{optimization_results['total_grp']:.1f}")
    
    with col3:
        st.metric("COST_EUR", f"{optimization_results['total_cost']/1000:.1f}k", delta=f"-{(campaign_config['budget']-optimization_results['total_cost'])/1000:.1f}k")
    
    with col4:
        ratio = optimization_results['total_grp'] / (optimization_results['total_cost'] / 1000)
        st.metric("EFFICIENCY", f"{ratio:.2f}", delta="GRP/k€")
    
    with col5:
        usage = (optimization_results['total_cost'] / campaign_config['budget']) * 100
        st.metric("BUDGET_USE", f"{usage:.1f}%", delta=f"{usage:.1f}%")
    
    st.markdown("---")
    
    # Graphiques techniques
    tab1, tab2, tab3 = st.tabs(["📊 DISTRIBUTION", "⏱️ TEMPORAL", "💰 FINANCIAL"])
    
    with tab1:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### GRP BREAKDOWN BY NETWORK")
            grp_by_regie = df_spots.groupby('REGIE')['GRP'].sum().reset_index()
            fig1 = px.bar(
                grp_by_regie,
                x='REGIE',
                y='GRP',
                color='GRP',
                color_continuous_scale=['#0a0e27', '#10b981', '#06b6d4'],
                text='GRP'
            )
            fig1.update_traces(texttemplate='%{text:.1f}', textposition='outside')
            fig1.update_layout(
                height=350,
                plot_bgcolor='#0a0e27',
                paper_bgcolor='#0a0e27',
                font=dict(color='#e4e4e7', family='JetBrains Mono'),
                showlegend=False,
                xaxis=dict(gridcolor='#334155'),
                yaxis=dict(gridcolor='#334155')
            )
            st.plotly_chart(fig1, use_container_width=True)
        
        with col2:
            st.markdown("#### SPOT ALLOCATION BY RADIO")
            spots_by_radio = df_spots.groupby('RADIO').size().reset_index(name='COUNT')
            fig2 = px.pie(
                spots_by_radio,
                values='COUNT',
                names='RADIO',
                color_discrete_sequence=px.colors.sequential.Teal,
                hole=0.5
            )
            fig2.update_traces(textposition='inside', textinfo='percent+label', textfont=dict(color='white'))
            fig2.update_layout(
                height=350,
                plot_bgcolor='#0a0e27',
                paper_bgcolor='#0a0e27',
                font=dict(color='#e4e4e7', family='JetBrains Mono'),
                showlegend=True
            )
            st.plotly_chart(fig2, use_container_width=True)
    
    with tab2:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### DAILY GRP TREND")
            daily_grp = df_spots.groupby('DATE')['GRP'].sum().reset_index()
            fig3 = px.line(
                daily_grp,
                x='DATE',
                y='GRP',
                markers=True,
                line_shape='spline'
            )
            fig3.update_traces(line=dict(color='#10b981', width=3), marker=dict(size=10, color='#06b6d4'))
            fig3.update_layout(
                height=350,
                plot_bgcolor='#0a0e27',
                paper_bgcolor='#0a0e27',
                font=dict(color='#e4e4e7', family='JetBrains Mono'),
                xaxis=dict(gridcolor='#334155'),
                yaxis=dict(gridcolor='#334155')
            )
            st.plotly_chart(fig3, use_container_width=True)
        
        with col2:
            st.markdown("#### TIME SLOT HEATMAP")
            slot_count = df_spots.groupby('TIME_SLOT').size().reset_index(name='SPOTS')
            slot_count = slot_count.sort_values('TIME_SLOT')
            fig4 = px.bar(
                slot_count,
                x='TIME_SLOT',
                y='SPOTS',
                color='SPOTS',
                color_continuous_scale='Teal'
            )
            fig4.update_layout(
                height=350,
                plot_bgcolor='#0a0e27',
                paper_bgcolor='#0a0e27',
                font=dict(color='#e4e4e7', family='JetBrains Mono'),
                showlegend=False,
                xaxis=dict(gridcolor='#334155'),
                yaxis=dict(gridcolor='#334155')
            )
            st.plotly_chart(fig4, use_container_width=True)
    
    with tab3:
        st.markdown("#### COST vs GRP EFFICIENCY MATRIX")
        scatter_data = df_spots.groupby('RADIO').agg({
            'COST_EUR': 'sum',
            'GRP': 'sum',
            'SPOT_ID': 'count'
        }).reset_index()
        scatter_data.columns = ['RADIO', 'TOTAL_COST', 'TOTAL_GRP', 'SPOT_COUNT']
        
        fig5 = px.scatter(
            scatter_data,
            x='TOTAL_COST',
            y='TOTAL_GRP',
            size='SPOT_COUNT',
            color='RADIO',
            text='RADIO',
            size_max=50,
            color_discrete_sequence=['#10b981', '#06b6d4', '#a78bfa', '#f59e0b']
        )
        fig5.update_traces(textposition='top center', textfont=dict(family='JetBrains Mono', size=10))
        fig5.update_layout(
            height=450,
            plot_bgcolor='#0a0e27',
            paper_bgcolor='#0a0e27',
            font=dict(color='#e4e4e7', family='JetBrains Mono'),
            xaxis=dict(title="TOTAL COST (EUR)", gridcolor='#334155'),
            yaxis=dict(title="TOTAL GRP", gridcolor='#334155')
        )
        st.plotly_chart(fig5, use_container_width=True)
    
    st.markdown("---")
    
    # Performance cards
    st.markdown("### ⚡ PERFORMANCE METRICS")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class='stat-card'>
            <h4>VARIABLES</h4>
            <p class='value'>{}</p>
        </div>
        """.format(optimization_results['n_variables']), unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='stat-card'>
            <h4>CONSTRAINTS</h4>
            <p class='value'>{}</p>
        </div>
        """.format(optimization_results['n_constraints']), unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='stat-card'>
            <h4>ITERATIONS</h4>
            <p class='value'>{}</p>
        </div>
        """.format(optimization_results['iterations']), unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class='stat-card'>
            <h4>EXEC TIME</h4>
            <p class='value'>{}s</p>
        </div>
        """.format(optimization_results['execution_time']), unsafe_allow_html=True)

# ========== PAGE: RESULTS ==========
elif page == "📊 RESULTS":
    st.subheader("📊 OPTIMIZATION RESULTS")
    
    # Summary table
    summary = df_spots.groupby('RADIO').agg({
        'SPOT_ID': 'count',
        'GRP': 'sum',
        'COST_EUR': 'sum',
        'EFFICIENCY': 'mean'
    }).reset_index()
    summary.columns = ['RADIO', 'SPOTS', 'GRP_TOTAL', 'COST_TOTAL', 'AVG_EFFICIENCY']
    summary['GRP_%'] = (summary['GRP_TOTAL'] / summary['GRP_TOTAL'].sum() * 100).round(1)
    
    st.dataframe(
        summary.style.format({
            'GRP_TOTAL': '{:.2f}',
            'COST_TOTAL': '{:,.0f}',
            'AVG_EFFICIENCY': '{:.3f}',
            'GRP_%': '{:.1f}%'
        }).background_gradient(cmap='Greens', subset=['GRP_TOTAL', 'COST_TOTAL']),
        use_container_width=True,
        height=300
    )
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### NETWORK PERFORMANCE")
        regie_perf = df_spots.groupby('REGIE').agg({
            'GRP': 'sum',
            'COST_EUR': 'sum'
        }).reset_index()
        regie_perf['RATIO'] = regie_perf['GRP'] / (regie_perf['COST_EUR'] / 1000)
        
        fig = px.bar(
            regie_perf,
            x='REGIE',
            y='RATIO',
            color='RATIO',
            color_continuous_scale='Teal',
            text='RATIO'
        )
        fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
        fig.update_layout(
            height=350,
            plot_bgcolor='#0a0e27',
            paper_bgcolor='#0a0e27',
            font=dict(color='#e4e4e7', family='JetBrains Mono'),
            showlegend=False,
            xaxis=dict(gridcolor='#334155'),
            yaxis=dict(title="GRP/k€", gridcolor='#334155')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("#### DAILY DISTRIBUTION")
        daily_stats = df_spots.groupby('DATE').agg({
            'SPOT_ID': 'count',
            'GRP': 'sum'
        }).reset_index()
        daily_stats.columns = ['DATE', 'SPOTS', 'GRP']
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=daily_stats['DATE'],
            y=daily_stats['GRP'],
            name='GRP',
            marker_color='#10b981'
        ))
        fig.add_trace(go.Scatter(
            x=daily_stats['DATE'],
            y=daily_stats['SPOTS'],
            name='SPOTS',
            yaxis='y2',
            marker_color='#06b6d4',
            mode='lines+markers'
        ))
        fig.update_layout(
            height=350,
            plot_bgcolor='#0a0e27',
            paper_bgcolor='#0a0e27',
            font=dict(color='#e4e4e7', family='JetBrains Mono'),
            yaxis=dict(title="GRP", gridcolor='#334155'),
            yaxis2=dict(title="SPOTS", overlaying='y', side='right', gridcolor='#334155'),
            hovermode='x unified'
        )
        st.plotly_chart(fig, use_container_width=True)

# ========== PAGE: ANALYTICS ==========
elif page == "📈 ANALYTICS":
    st.subheader("📈 ADVANCED ANALYTICS")
    
    # Correlation heatmap
    st.markdown("#### CORRELATION MATRIX: TIME SLOT vs DAY")
    pivot = df_spots.pivot_table(
        values='GRP',
        index='TIME_SLOT',
        columns='DAY',
        aggfunc='sum',
        fill_value=0
    )
    
    fig = px.imshow(
        pivot,
        labels=dict(x="DAY", y="TIME_SLOT", color="GRP"),
        color_continuous_scale='Teal',
        aspect='auto'
    )
    fig.update_layout(
        height=500,
        plot_bgcolor='#0a0e27',
        paper_bgcolor='#0a0e27',
        font=dict(color='#e4e4e7', family='JetBrains Mono')
    )
    st.plotly_chart(fig, use_container_width=True)

# ========== PAGE: SCHEDULE ==========
elif page == "🗓️ SCHEDULE":
    st.subheader("🗓️ DETAILED SCHEDULE")
    
    # Filters
    col1, col2, col3 = st.columns(3)
    with col1:
        filter_radio = st.multiselect("RADIO_FILTER", df_spots['RADIO'].unique(), default=df_spots['RADIO'].unique())
    with col2:
        filter_date = st.multiselect("DATE_FILTER", df_spots['DATE'].unique(), default=df_spots['DATE'].unique())
    with col3:
        filter_slot = st.multiselect("TIME_SLOT_FILTER", sorted(df_spots['TIME_SLOT'].unique()), default=sorted(df_spots['TIME_SLOT'].unique()))
    
    df_filtered = df_spots[
        (df_spots['RADIO'].isin(filter_radio)) &
        (df_spots['DATE'].isin(filter_date)) &
        (df_spots['TIME_SLOT'].isin(filter_slot))
    ]
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("FILTERED_SPOTS", len(df_filtered))
    with col2:
        st.metric("FILTERED_GRP", f"{df_filtered['GRP'].sum():.1f}")
    with col3:
        st.metric("FILTERED_COST", f"{df_filtered['COST_EUR'].sum()/1000:.1f}k€")
    with col4:
        ratio_filtered = df_filtered['GRP'].sum() / (df_filtered['COST_EUR'].sum() / 1000) if df_filtered['COST_EUR'].sum() > 0 else 0
        st.metric("FILTERED_RATIO", f"{ratio_filtered:.2f}")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.dataframe(
        df_filtered.style.format({
            'COST_EUR': '{:,.0f}',
            'GRP': '{:.2f}',
            'EFFICIENCY': '{:.3f}'
        }),
        use_container_width=True,
        height=500
    )
    
    csv = df_filtered.to_csv(index=False)
    st.download_button(
        label="⬇ EXPORT_CSV",
        data=csv,
        file_name=f"mediamatrix_schedule_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
        mime="text/csv"
    )

# ========== PAGE: CONFIG ==========
elif page == "⚙️ CONFIG":
    st.subheader("⚙️ CONFIGURATION")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='data-box'>
            <h3 style='color: #10b981; margin-top: 0;'>CAMPAIGN_CONFIG</h3>
            <code>NAME: {}</code><br>
            <code>CLIENT_ID: {}</code><br>
            <code>BUDGET: €{:,}</code><br>
            <code>PERIOD: {}</code><br>
            <code>OBJECTIVE: {}</code>
        </div>
        """.format(
            campaign_config['nom_campagne'],
            campaign_config['client'],
            campaign_config['budget'],
            campaign_config['periode'],
            campaign_config['objectif']
        ), unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class='data-box'>
            <h3 style='color: #06b6d4; margin-top: 0;'>NETWORKS</h3>
        """, unsafe_allow_html=True)
        for regie in campaign_config['regies']:
            st.markdown(f"<code>✓ {regie}</code><br>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='data-box'>
            <h3 style='color: #10b981; margin-top: 0;'>SOLVER_CONFIG</h3>
            <code>ENGINE: {}</code><br>
            <code>STATUS: {}</code><br>
            <code>VARIABLES: {}</code><br>
            <code>CONSTRAINTS: {}</code><br>
            <code>ITERATIONS: {}</code><br>
            <code>EXEC_TIME: {}s</code><br>
            <code>GAP: {:.2%}</code>
        </div>
        """.format(
            optimization_results['solver'],
            optimization_results['status'],
            optimization_results['n_variables'],
            optimization_results['n_constraints'],
            optimization_results['iterations'],
            optimization_results['execution_time'],
            optimization_results['gap']
        ), unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class='data-box'>
            <h3 style='color: #06b6d4; margin-top: 0;'>RADIOS</h3>
        """, unsafe_allow_html=True)
        for radio in campaign_config['radios']:
            st.markdown(f"<code>✓ {radio}</code><br>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# ========== PAGE: TERMINAL ==========
elif page == "💻 TERMINAL":
    st.subheader("💻 SYSTEM TERMINAL")
    
    st.markdown("""
    <div class='terminal-box' style='padding: 20px; min-height: 400px;'>
        <div style='color: #06b6d4;'>$ mediamatrix optimize --campaign=NATIONAL_AUG_2024 --verbose</div>
        <br>
        <div>[INFO] Initializing optimization engine...</div>
        <div>[INFO] Loading campaign configuration...</div>
        <div style='color: #10b981;'>[OK] Campaign: {}</div>
        <div style='color: #10b981;'>[OK] Budget: €{:,}</div>
        <div style='color: #10b981;'>[OK] Period: {}</div>
        <br>
        <div>[INFO] Building constraint matrix...</div>
        <div>[INFO] Variables: {}</div>
        <div>[INFO] Constraints: {}</div>
        <br>
        <div>[INFO] Running SCIP solver...</div>
        <div>[INFO] Iteration: 1247/1247</div>
        <div style='color: #10b981;'>[SUCCESS] Optimal solution found</div>
        <br>
        <div>[RESULT] Status: {}</div>
        <div>[RESULT] GRP Total: {:.2f}</div>
        <div>[RESULT] Cost Total: €{:,.0f}</div>
        <div>[RESULT] Spots Selected: {}</div>
        <div>[RESULT] Execution Time: {}s</div>
        <div>[RESULT] Gap: {:.2%}</div>
        <br>
        <div style='color: #10b981;'>[COMPLETED] Optimization successful</div>
        <div style='color: #06b6d4;'>$ _</div>
    </div>
    """.format(
        campaign_config['nom_campagne'],
        campaign_config['budget'],
        campaign_config['periode'],
        optimization_results['n_variables'],
        optimization_results['n_constraints'],
        optimization_results['status'],
        optimization_results['total_grp'],
        optimization_results['total_cost'],
        optimization_results['n_spots'],
        optimization_results['execution_time'],
        optimization_results['gap']
    ), unsafe_allow_html=True)

# ========== FOOTER ==========
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div class='terminal-box' style='text-align: center;'>
    <div style='color: #10b981; font-size: 1.2rem; font-weight: 700;'>MEDIAMATRIX ANALYTICS v3.0.0</div>
    <div style='margin-top: 8px;'>RADIO CAMPAIGN OPTIMIZATION PLATFORM | POWERED BY OR-TOOLS SCIP</div>
    <div style='margin-top: 5px; color: #94a3b8; font-size: 0.85rem;'>© 2024 | DEMO VERSION</div>
</div>
""", unsafe_allow_html=True)

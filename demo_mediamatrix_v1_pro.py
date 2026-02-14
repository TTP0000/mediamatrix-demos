#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mediamatrix Demo V1 Pro - Structure IDENTIQUE à l'application originale
Reproduit exactement : pages, onglets, contraintes, graphiques
Bouton "Lancer l'optimisation" désactivé | Résultats pré-calculés affichés
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(
    page_title="MediaMatrix - Optimisation Radio",
    page_icon="📻",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main { background-color: #f8f9fa; }
    .stMetric { background-color: white; padding: 15px; border-radius: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
    h1 { color: #1e3a8a; font-weight: 700; border-bottom: 3px solid #3b82f6; padding-bottom: 10px; margin-bottom: 20px; }
    h2 { color: #1e40af; font-weight: 600; }
    .info-box { background-color: #dbeafe; border-left: 4px solid #3b82f6; padding: 15px; border-radius: 4px; margin: 10px 0; }
    .success-box { background-color: #dcfce7; border-left: 4px solid #22c55e; padding: 15px; border-radius: 4px; margin: 10px 0; }
    .disabled-box { background-color: #f1f5f9; border-left: 4px solid #94a3b8; padding: 15px; border-radius: 4px; margin: 10px 0; opacity: 0.9; }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_demo_data():
    campaign_config = {
        "nom_campagne": "Campagne Nationale Août 2024",
        "client": "Horizon Media",
        "budget": 30000,
        "date_debut": "19/08/2024",
        "date_fin": "21/08/2024",
        "audience_cible": "25-49 ans, CSP+",
        "objectifs": "Maximiser la notoriété de marque",
        "regies": ["NRJ GLOBAL", "ALTICE", "LAGARDÈRE"],
        "radios": ["Chérie FM", "RMC", "Europe 1", "Fun Radio"],
        "timeSlots": [
            {"name": "Matinale", "start": "06:00", "end": "09:00"},
            {"name": "Milieu de journée", "start": "09:00", "end": "16:00"},
            {"name": "Drive", "start": "16:00", "end": "19:00"},
        ],
        "grpConstraints": {
            "regie": {"NRJ GLOBAL": 35, "ALTICE": 40, "LAGARDÈRE": 25},
            "slots": {},
            "slotGroups": [],
            "slotAbsoluteGrp": {},
        },
    }
    optimization_results = {
        "status": "optimal",
        "n_spots": 87,
        "total_grp": 94.35,
        "total_cost": 29850.0,
        "execution_time": 2.43,
    }
    spots_data = []
    dates = ['19/08/2024', '20/08/2024', '21/08/2024']
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
        for date in dates:
            for j in range(spots_per_day):
                if j % 2 == 0:
                    creneau = creneaux_prime[j % len(creneaux_prime)]
                    prix = int(config['prix_moy'] * 1.3)
                    grp = round(config['grp_moy'] * 1.25, 2)
                else:
                    creneau = creneaux_standard[j % len(creneaux_standard)]
                    prix = config['prix_moy']
                    grp = config['grp_moy']
                jour = 'Lundi' if date == dates[0] else 'Mardi' if date == dates[1] else 'Mercredi'
                spots_data.append({
                    'regie': config['regie'], 'radio': radio, 'date': date, 'jour': jour,
                    'creneau': creneau, 'prix': prix, 'GRP': grp
                })
                spot_id += 1
    df_spots = pd.DataFrame(spots_data)
    return campaign_config, optimization_results, df_spots

cfg, opt, df_spots = load_demo_data()

st.markdown("<h1>MediaMatrix - Optimisation de Campagnes Radio</h1>", unsafe_allow_html=True)

# === SIDEBAR (ordre exact de l'app) ===
with st.sidebar:
    st.markdown("### 📻 MediaMatrix")
    st.markdown("---")
    page = st.radio("Navigation", [
        "📄 Fichier Source",
        "👤 Profils Clients",
        "📋 Gestion Campagnes",
        "🎯 Optimisation Campagne",
        "📊 Résultats",
    ])
    st.markdown("---")
    st.info("Mode Démo : résultats pré-calculés. Bouton optimisation désactivé.")

# === PAGE 1: FICHIER SOURCE ===
if page == "📄 Fichier Source":
    st.subheader("Fichier Source")
    st.markdown('<div class="success-box">', unsafe_allow_html=True)
    st.markdown("✅ **Fichier chargé** : GRP_demo.csv")
    st.markdown("- 3 726 spots | 3 régies | 4 radios | Période : 19/08-21/08/2024")
    st.markdown('</div>', unsafe_allow_html=True)
    st.button("📤 Charger un nouveau CSV", disabled=True)
    st.markdown("### Aperçu des données")
    sample = pd.DataFrame({
        'Régie': ['ALTICE', 'NRJ GLOBAL', 'LAGARDÈRE'],
        'Radio': ['RMC', 'Chérie FM', 'Europe 1'],
        'Date': ['19/08/2024']*3, 'Créneau': ['07:00', '07:30', '08:00'],
        'Prix (€)': [7275, 546, 4200], 'GRP': [1.15, 0.95, 0.85]
    })
    st.dataframe(sample, hide_index=True)

# === PAGE 2: PROFILS CLIENTS ===
elif page == "👤 Profils Clients":
    st.subheader("Profils Clients")
    st.markdown('<div class="info-box">', unsafe_allow_html=True)
    st.markdown(f"**Client actif** : {cfg['client']}")
    st.markdown('</div>', unsafe_allow_html=True)
    st.dataframe(pd.DataFrame([{"Nom": cfg['client'], "Radios": 4, "Statut": "✅ Actif"}]), hide_index=True)
    st.button("➕ Nouveau client", disabled=True)

# === PAGE 3: GESTION CAMPAGNES ===
elif page == "📋 Gestion Campagnes":
    st.subheader("Gestion des Campagnes")
    st.markdown('<div class="success-box">', unsafe_allow_html=True)
    st.markdown(f"**Campagne active** : {cfg['nom_campagne']}")
    st.markdown('</div>', unsafe_allow_html=True)
    st.dataframe(pd.DataFrame([{
        "Nom": cfg['nom_campagne'], "Client": cfg['client'], "Budget": f"{cfg['budget']:,} €",
        "Période": f"{cfg['date_debut']} - {cfg['date_fin']}", "Statut": "✅ Active"
    }]), hide_index=True)
    st.button("➕ Nouvelle campagne", disabled=True)

# === PAGE 4: OPTIMISATION CAMPAGNE (9 onglets exacts) ===
elif page == "🎯 Optimisation Campagne":
    st.subheader("Configuration de l'Optimisation de Campagne")
    
    st.markdown("**Sélectionner une Campagne à Configurer**")
    st.selectbox("Campagne", [f"{cfg['nom_campagne']} (Client: {cfg['client']})"], disabled=True)
    
    st.markdown("---")
    
    # 9 onglets dans l'ordre exact de l'app
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs([
        "Général & Budget",
        "Régies & Radios",
        "Tranches Horaires",
        "Exclusions",
        "Contraintes GRP",
        "GRP Max par Radio",
        "Pression Journalière",
        "Bornes Spots/Radio",
        "Récapitulatif"
    ])
    
    with tab1:
        st.markdown("Les informations générales sont définies dans 'Gestion des Campagnes'.")
        st.text_input("Public cible", value=cfg['audience_cible'], disabled=True)
        st.text_area("Objectifs", value=cfg['objectifs'], disabled=True)
    
    with tab2:
        st.markdown("#### Régies sélectionnées")
        for r in cfg['regies']:
            st.checkbox(r, value=True, disabled=True)
        st.markdown("#### Radios sélectionnées")
        for r in cfg['radios']:
            st.checkbox(r, value=True, disabled=True)
    
    with tab3:
        st.markdown("#### Tranches horaires définies")
        df_slots = pd.DataFrame([{**s, "Début": s["start"], "Fin": s["end"]} for s in cfg['timeSlots']])
        st.dataframe(df_slots[['name', 'Début', 'Fin']].rename(columns={'name': 'Nom'}), hide_index=True)
        st.button("➕ Ajouter une tranche", disabled=True)
        st.markdown("---")
        st.markdown("#### Spots exacts par tranche horaire (par jour)")
        st.info("Définissez exactement N spots entre une heure de début et de fin.")
        st.button("➕ Ajouter une règle", disabled=True)
    
    with tab4:
        st.markdown("#### Exclusions")
        st.markdown("Types d'exclusion disponibles :")
        excl_types = [
            ("Jour spécifique", "Exclusion d'une date précise (ex: 20/08/2024)"),
            ("Période", "Exclusion d'une plage de dates (début - fin)"),
            ("Jour de la semaine", "Exclusion d'un jour (Lundi, Mardi, ...)"),
            ("Tranche horaire", "Exclusion d'une plage horaire (ex: 06:00-09:00)"),
            ("Tranche horaire d'un jour spécifique", "Exclusion d'une plage horaire un jour donné"),
        ]
        for t, d in excl_types:
            st.markdown(f"- **{t}** : {d}")
        st.markdown("**Aucune exclusion définie.**")
        st.button("➕ Ajouter une exclusion", disabled=True)
    
    with tab5:
        st.markdown("#### Contraintes de répartition GRP par régie (% min. du GRP total)")
        df_grp = pd.DataFrame([{"Régie": k, "% min": f"{v}%"} for k, v in cfg['grpConstraints']['regie'].items()])
        st.dataframe(df_grp, hide_index=True)
        st.caption("Exemple du PRD : Régie 1 ≥ 30% du GRP total")
        st.markdown("---")
        st.markdown("#### Contraintes GRP par Groupes de Tranches Horaires")
        st.info("Définissez des groupes de tranches (ex: Matin) et un % minimum du GRP total. Bouton : + Ajouter un groupe de tranches.")
        st.markdown("**Aucun groupe de tranches défini.**")
        st.markdown("---")
        st.markdown("#### Contraintes GRP par Tranche Horaire Individuelle")
        st.caption("Pour chaque tranche : soit % min du GRP total, soit GRP min absolu (mutuellement exclusifs).")
        if cfg['timeSlots']:
            st.dataframe(pd.DataFrame([{"Tranche": s['name'], "Plage": f"{s['start']}-{s['end']}", "% GRP total (min)": "-", "GRP absolu (min)": "-"} for s in cfg['timeSlots']]), hide_index=True)
    
    with tab6:
        st.markdown("#### GRP Maximal par Radio")
        st.markdown("Limitez le % maximum du GRP total pour une radio donnée.")
        st.markdown("Paramètres : **Radio**, **% GRP Maximal**, **Type de période** (Jours de la semaine / Dates spécifiques), **Tranches horaires**.")
        st.markdown("**Aucune contrainte définie.**")
        st.button("➕ Ajouter contrainte", disabled=True)
    
    with tab7:
        st.markdown("#### Pression Journalière")
        st.markdown("Objectifs de GRP minimum par jour.")
        st.markdown("Ajout en lot : **Tous les jours** | **Jours de semaine** | **Week-end**")
        st.markdown("Pour chaque cible : **Date** (si applicable), **Type** (GRP min ou % min), **Valeur**.")
        st.markdown("**Aucun objectif journalier défini.**")
        st.button("➕ Ajouter un objectif journalier", disabled=True)
    
    with tab8:
        st.markdown("#### Bornes Spots par Radio")
        st.markdown("Min/Max de spots par radio, selon la portée et le temps.")
        st.markdown("- **Portée** : Toute la période | Date précise (YYYY-MM-DD)")
        st.markdown("- **Temps** : Toute la journée | Plage unique (Début–Fin) | Plusieurs plages (HH:MM–HH:MM; séparées par virgules)")
        st.markdown("- **Radios** : optionnel, filtrer par radios")
        st.markdown("**Aucune règle définie.**")
        st.button("➕ Ajouter une règle", disabled=True)
    
    with tab9:
        st.markdown("### Récapitulatif de la Campagne")
        st.markdown(f"**Nom** : {cfg['nom_campagne']}")
        st.markdown(f"**Dates** : {cfg['date_debut']} - {cfg['date_fin']}")
        st.markdown(f"**Budget** : {cfg['budget']:,} €")
        st.markdown(f"**Régies** : {', '.join(cfg['regies'])}")
        st.markdown(f"**Radios** : {', '.join(cfg['radios'])}")
        st.markdown(f"**Tranches** : {len(cfg['timeSlots'])} définies")
        st.markdown("**Exclusions** : Aucune")
        st.markdown("**Pression journalière** : Aucune")
        st.markdown("---")
        st.checkbox("Activer le quiconce (répartition sur plusieurs jours)", value=False, disabled=True)
        st.caption("Quiconce : évite de concentrer les spots sur un seul jour.")
        st.markdown("---")
        st.markdown('<div class="disabled-box">', unsafe_allow_html=True)
        st.markdown("**🔒 Mode Démo** : Le bouton d'optimisation est désactivé. Consultez l'onglet **Résultats** pour voir un exemple.")
        st.markdown('</div>', unsafe_allow_html=True)
        st.button("🚀 Lancer l'optimisation", disabled=True)

# === PAGE 5: RÉSULTATS (5 onglets + graphiques) ===
elif page == "📊 Résultats":
    st.subheader("Résultats de l'optimisation")
    
    st.markdown('<div class="success-box">', unsafe_allow_html=True)
    st.markdown(f"✅ **Optimisation réussie** - Campagne : {cfg['nom_campagne']} - Statut : `{opt['status'].upper()}`")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Onglets Résultats (ordre exact: Résumé, Graphiques, Contraintes, Spots, Calendrier)
    res_tab1, res_tab2, res_tab3, res_tab4, res_tab5 = st.tabs([
        "Résumé",
        "Graphiques",
        "Contraintes",
        "Spots",
        "Calendrier"
    ])
    
    with res_tab1:
        col1, col2, col3, col4, col5, col6 = st.columns(6)
        with col1:
            st.metric("GRP Total", f"{opt['total_grp']:.2f}")
        with col2:
            st.metric("Coût Total", f"{opt['total_cost']:,.0f} €")
        with col3:
            st.metric("Nombre de Spots", opt['n_spots'])
        with col4:
            st.metric("Budget Utilisé", f"{(opt['total_cost']/cfg['budget']*100):.2f}%")
        with col5:
            st.metric("Coût par GRP", f"{opt['total_cost']/opt['total_grp']:,.0f} €")
        with col6:
            st.metric("Temps d'Exécution", f"{opt['execution_time']:.2f}s")
    
    with res_tab2:
        # 4 sous-onglets graphiques : Par Régie, Par Radio, Par Jour, Par Créneau
        chart_sub = st.radio("Vue", ["Par Régie", "Par Radio", "Par Jour", "Par Créneau"], horizontal=True)
        
        if chart_sub == "Par Régie":
            grp_regie = df_spots.groupby('regie')['GRP'].sum().reset_index()
            fig = px.pie(grp_regie, values='GRP', names='regie', title="Répartition des GRP par régie", hole=0.4)
            st.plotly_chart(fig, use_container_width=True)
        elif chart_sub == "Par Radio":
            grp_radio = df_spots.groupby('radio')['GRP'].sum().reset_index()
            fig = px.pie(grp_radio, values='GRP', names='radio', title="Répartition des GRP par radio", hole=0.5)
            st.plotly_chart(fig, use_container_width=True)
        elif chart_sub == "Par Jour":
            grp_day = df_spots.groupby('date').agg({'GRP': 'sum', 'regie': 'count'}).reset_index()
            grp_day.columns = ['date', 'GRP', 'Spots']
            fig = go.Figure()
            fig.add_trace(go.Bar(x=grp_day['date'], y=grp_day['GRP'], name='GRP', yaxis='y'))
            fig.add_trace(go.Scatter(x=grp_day['date'], y=grp_day['Spots'], name='Nombre de spots', yaxis='y2', mode='lines+markers'))
            fig.update_layout(yaxis=dict(title='GRP'), yaxis2=dict(title='Spots', overlaying='y', side='right'))
            st.plotly_chart(fig, use_container_width=True)
        else:
            grp_slot = df_spots.groupby('creneau')['GRP'].sum().reset_index().sort_values('creneau')
            fig = px.bar(grp_slot, x='creneau', y='GRP', title="Répartition par créneau horaire")
            st.plotly_chart(fig, use_container_width=True)
    
    with res_tab3:
        st.markdown("#### Respect des Contraintes")
        constraint_sub = st.radio("Type", [
            "Par Régie", "Par Créneau Utilisateur", "Par Groupe de Créneaux",
            "GRP Absolu par Tranche", "Pression Journalière", "GRP Max par Radio", "Autres Contraintes"
        ], horizontal=True)
        if constraint_sub == "Par Régie":
            regie_actual = df_spots.groupby('regie')['GRP'].sum()
            total_grp = regie_actual.sum()
            regie_pct = (regie_actual / total_grp * 100).round(2)
            df_check = pd.DataFrame({
                'Régie': regie_pct.index,
                'Objectif (%)': [cfg['grpConstraints']['regie'].get(r, 0) for r in regie_pct.index],
                'GRP Réel (%)': regie_pct.values,
                'Statut': ['✓' if regie_pct[r] >= cfg['grpConstraints']['regie'].get(r, 0) - 5 else '✗' for r in regie_pct.index]
            })
            st.dataframe(df_check, hide_index=True)
        else:
            st.info(f"Aucune contrainte {constraint_sub.lower()} à afficher pour cette démo.")
    
    with res_tab4:
        st.markdown("#### Liste des Spots")
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            f_regie = st.multiselect("Régie", df_spots['regie'].unique(), default=df_spots['regie'].unique())
        with col2:
            f_radio = st.multiselect("Radio", df_spots['radio'].unique(), default=df_spots['radio'].unique())
        with col3:
            f_date = st.multiselect("Date", df_spots['date'].unique(), default=df_spots['date'].unique())
        with col4:
            f_jour = st.multiselect("Jour", df_spots['jour'].unique(), default=df_spots['jour'].unique())
        with col5:
            f_creneau = st.multiselect("Créneau", sorted(df_spots['creneau'].unique()), default=sorted(df_spots['creneau'].unique()))
        
        df_f = df_spots[(df_spots['regie'].isin(f_regie)) & (df_spots['radio'].isin(f_radio)) & 
                        (df_spots['date'].isin(f_date)) & (df_spots['jour'].isin(f_jour)) & 
                        (df_spots['creneau'].isin(f_creneau))]
        
        st.dataframe(df_f.style.format({'prix': '{:,.0f}', 'GRP': '{:.2f}'}), use_container_width=True, height=400)
        csv = df_f.to_csv(index=False, encoding='utf-8-sig')
        st.download_button("Exporter CSV", data=csv, file_name="spots_selectionnes.csv", mime="text/csv")
    
    with res_tab5:
        cal_sub = st.radio("Vue calendrier", ["Calendrier", "Infos Spots"], horizontal=True)
        if cal_sub == "Calendrier":
            st.markdown("#### Calendrier des Spots par Radio")
            sel_radio = st.selectbox("Sélectionner une radio", df_spots['radio'].unique())
            radio_spots = df_spots[df_spots['radio'] == sel_radio]
            pivot = radio_spots.pivot_table(index='creneau', columns='date', values='GRP', aggfunc='sum', fill_value=0)
            st.dataframe(pivot, use_container_width=True)
            st.caption("GRP par créneau et par date")
        else:
            st.markdown("#### Informations Spots (Totaux)")
            summary = df_spots.groupby('radio').agg({'regie': 'count', 'GRP': 'sum', 'prix': 'sum'}).reset_index()
            summary.columns = ['Radio', 'Nombre de spots', 'GRP total', 'Coût total']
            st.dataframe(summary.style.format({'GRP total': '{:.2f}', 'Coût total': '{:,.0f}'}), hide_index=True)

st.markdown("---")
st.markdown("<div style='text-align:center;color:#64748b;padding:20px;'><p><strong>MediaMatrix</strong> - Optimisation de campagnes radio | Mode Démo</p></div>", unsafe_allow_html=True)

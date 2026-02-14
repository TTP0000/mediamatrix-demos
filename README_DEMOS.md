# Mediamatrix - Démos Streamlit

Ce dossier contient **3 versions différentes** d'une interface de démonstration pour l'optimiseur de campagnes radio Mediamatrix.

## 📋 Les 3 versions

### Version 1: Style Professionnel Corporate (`demo_mediamatrix_v1_pro.py`)
- **Style**: Sobre, professionnel, type entreprise
- **Couleurs**: Bleus (#1e3a8a, #3b82f6), fond clair
- **Police**: Standard sans-serif
- **Public cible**: Présentation clients, réunions corporate
- **Points forts**: 
  - Interface propre et épurée
  - Graphiques élégants
  - Mise en page classique

### Version 2: Style Moderne Coloré (`demo_mediamatrix_v2_modern.py`)
- **Style**: Moderne, dynamique, coloré
- **Couleurs**: Gradients violets/bleus (#667eea, #764ba2), dégradés multiples
- **Police**: Poppins (Google Fonts)
- **Public cible**: Startups, marketing digital, présentation dynamique
- **Points forts**:
  - Design attractif et moderne
  - Animations et effets visuels
  - Interface engageante

### Version 3: Style Data Analytics Dark (`demo_mediamatrix_v3_dark.py`)
- **Style**: Mode sombre, terminal/tech, data science
- **Couleurs**: Dark theme (#0a0e27), vert (#10b981), cyan (#06b6d4)
- **Police**: JetBrains Mono (monospace) + Inter
- **Public cible**: Data scientists, ingénieurs, présentation technique
- **Points forts**:
  - Interface type terminal
  - Codes et données en évidence
  - Style "hacker" professionnel

## 🚀 Installation et lancement

### 1. Installer les dépendances
```bash
pip install -r requirements_demo.txt
```

### 2. Lancer une démo

**Version 1 - Professionnelle:**
```bash
streamlit run demo_mediamatrix_v1_pro.py
```

**Version 2 - Moderne:**
```bash
streamlit run demo_mediamatrix_v2_modern.py
```

**Version 3 - Dark Analytics:**
```bash
streamlit run demo_mediamatrix_v3_dark.py
```

## 📊 Données de démonstration

Toutes les versions utilisent le même jeu de données pré-calculé simulant une optimisation réelle :

- **Campagne**: Nationale Août 2024
- **Budget**: 30 000 €
- **Spots sélectionnés**: 87
- **GRP total**: 94.35
- **4 radios**: Chérie FM, RMC, Europe 1, Fun Radio
- **3 régies**: NRJ GLOBAL, ALTICE, LAGARDÈRE
- **Période**: 19-21 Août 2024

### Résultats d'optimisation:
- ✅ Solution optimale trouvée
- ⚡ Temps d'exécution: 2.43s
- 🎯 180 variables analysées
- 🔒 24 contraintes respectées
- 💰 Budget utilisé: 99.5%
- 📈 Ratio GRP/k€: 3.16

## 📁 Structure des pages

Chaque version contient les mêmes fonctionnalités organisées différemment :

1. **Vue d'ensemble / Dashboard**: KPIs principaux, graphiques récapitulatifs
2. **Analyse détaillée / Results**: Tableaux détaillés, répartitions
3. **Analytics**: Analyses avancées, heatmaps, corrélations
4. **Planning / Schedule**: Liste des spots avec filtres
5. **Configuration**: Paramètres de campagne et optimisation

## 🎨 Personnalisation

Les données peuvent être facilement modifiées dans la fonction `load_demo_data()` de chaque fichier pour :
- Changer les valeurs de la campagne
- Ajuster les résultats d'optimisation
- Modifier les spots sélectionnés
- Anonymiser/personnaliser les noms

## 📝 Notes techniques

- Toutes les visualisations utilisent **Plotly** (interactif)
- Les données sont mises en cache avec `@st.cache_data`
- Le style CSS personnalisé est injecté via `st.markdown()`
- Aucune connexion backend requise (données statiques)
- Fonctionnement 100% côté client

## 🌐 Déploiement en ligne

Pour mettre en ligne sur **Streamlit Cloud** :

1. Créer un compte sur [streamlit.io](https://streamlit.io)
2. Connecter votre repo GitHub
3. Sélectionner le fichier principal (ex: `demo_mediamatrix_v1_pro.py`)
4. Le déploiement se fait automatiquement !

## ⚙️ Technologies utilisées

- **Streamlit**: Framework web Python
- **Plotly**: Graphiques interactifs
- **Pandas**: Manipulation de données
- **Python 3.9+**: Langage de base

## 💡 Utilisation recommandée

- **Version 1**: Présentations clients, rapports officiels
- **Version 2**: Démos commerciales, pitchs investisseurs
- **Version 3**: Conférences tech, meetups data science

---

**Mediamatrix** - Optimisation de campagnes médias radio powered by OR-Tools

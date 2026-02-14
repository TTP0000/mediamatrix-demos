# 📻 Mediamatrix - Démos Streamlit

**Vitrines interactives pour l'optimiseur de campagnes médias radio Mediamatrix**

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com)

---

## 🎯 À propos

Ce repository contient **3 versions différentes** d'interfaces Streamlit pour présenter les capacités de l'optimiseur **Mediamatrix** - un outil d'optimisation de campagnes publicitaires radio utilisant la programmation linéaire (OR-Tools SCIP).

Chaque version est conçue pour un **public différent** avec un **style visuel distinct**.

---

## 🎨 Les 3 versions

### Version 1 : Professionnelle Corporate 💼
**Fichier :** `demo_mediamatrix_v1_pro.py`

- **Style :** Sobre, bleu, fond clair
- **Public :** Clients corporate, réunions formelles, rapports officiels
- **Caractéristiques :** Interface épurée, graphiques élégants, mise en page classique

### Version 2 : Moderne Colorée 🌈
**Fichier :** `demo_mediamatrix_v2_modern.py`

- **Style :** Dynamique, gradients violets/roses, coloré
- **Public :** Startups, marketing, événements, pitchs
- **Caractéristiques :** Design attractif, animations, effets visuels modernes

### Version 3 : Dark Analytics 💻
**Fichier :** `demo_mediamatrix_v3_dark.py`

- **Style :** Dark mode, terminal, technique
- **Public :** Développeurs, data scientists, conférences tech
- **Caractéristiques :** Police monospace, style "hacker", page Terminal

---

## 🚀 Installation et lancement

### Prérequis
- Python 3.9 ou supérieur
- pip

### Installation rapide

```bash
# Cloner le repository
git clone https://github.com/TTP0000/mediamatrix-demos.git
cd mediamatrix-demos

# Installer les dépendances
pip install -r requirements_demo.txt
```

### Lancer une démo

**Option 1 : Script interactif (Windows)**
```bash
launch_demo.bat
```

**Option 2 : Ligne de commande directe**
```bash
# Version Professionnelle
streamlit run demo_mediamatrix_v1_pro.py

# Version Moderne
streamlit run demo_mediamatrix_v2_modern.py

# Version Dark Analytics
streamlit run demo_mediamatrix_v3_dark.py
```

---

## 📊 Données de démonstration

Toutes les versions utilisent un jeu de données pré-calculé simulant une optimisation réelle :

| Paramètre | Valeur |
|-----------|--------|
| **Campagne** | Nationale Août 2024 |
| **Budget** | 30 000 € |
| **Période** | 19-21 Août 2024 (3 jours) |
| **Spots optimisés** | 87 |
| **GRP total** | 94.35 |
| **Coût** | 29 850 € (99.5% du budget) |
| **Radios** | Chérie FM, RMC, Europe 1, Fun Radio |
| **Régies** | NRJ GLOBAL, ALTICE, LAGARDÈRE |

### Résultats d'optimisation
- ✅ Solution optimale trouvée en **2.43 secondes**
- 🎯 **180 variables** analysées
- 🔒 **24 contraintes** respectées
- 📈 **Ratio GRP/k€ : 3.16**

---

## ✨ Fonctionnalités

### Dans toutes les versions :

- ✅ **5-6 pages de navigation** (Dashboard, Résultats, Analytics, Planning, Config)
- ✅ **10+ graphiques interactifs** (Plotly)
- ✅ **KPIs en temps réel** (spots, GRP, coût, ratio)
- ✅ **Tableaux récapitulatifs** détaillés
- ✅ **Filtres dynamiques** (radio, date, créneau)
- ✅ **Export CSV** avec bouton de téléchargement
- ✅ **Heatmaps et analyses** temporelles
- ✅ **Responsive design** (mobile/tablette/desktop)
- ✅ **Données pré-calculées** (pas de backend requis)

---

## 📚 Documentation

| Fichier | Description |
|---------|-------------|
| `README_DEMOS.md` | Documentation générale complète |
| `COMPARAISON_VERSIONS.md` | Tableau comparatif des 3 styles |
| `QUICK_START.md` | Guide de démarrage rapide |
| `RECAPITULATIF_CREATION.md` | Récapitulatif détaillé du projet |
| `SOMMAIRE_VISUEL.txt` | Vue d'ensemble avec ASCII art |
| `INDEX.md` | Index de navigation |

---

## 🎯 Quelle version choisir ?

| Version | Public cible | Cas d'usage |
|---------|--------------|-------------|
| **V1 - Professionnelle** | Clients corporate | Rapports officiels, réunions formelles |
| **V2 - Moderne** | Startups, marketing | Démos commerciales, pitchs, événements |
| **V3 - Dark** | Développeurs, techs | Conférences tech, formations techniques |

---

## 🌐 Déploiement en ligne

### Sur Streamlit Cloud (gratuit)

1. Fork ce repository
2. Créer un compte sur [share.streamlit.io](https://share.streamlit.io)
3. Connecter votre compte GitHub
4. Sélectionner le fichier principal (ex: `demo_mediamatrix_v1_pro.py`)
5. Déploiement automatique en 2-3 minutes

**Résultat :** URL publique type `https://votre-app.streamlit.app`

---

## 🔧 Personnalisation

### Modifier les données de campagne

Éditer la fonction `load_demo_data()` dans chaque fichier `.py` :

```python
campaign_config = {
    "nom_campagne": "VOTRE CAMPAGNE",
    "client": "VOTRE CLIENT",
    "budget": 50000,  # Votre budget
    ...
}
```

### Modifier les couleurs

Dans la section CSS au début de chaque fichier :

```python
st.markdown("""
<style>
    h1 {
        color: #VOTRE_COULEUR;
    }
</style>
""")
```

### Anonymiser les données

Modifier le dictionnaire `radios_config` pour changer les noms :

```python
radios_config = {
    'Radio A': {...},
    'Radio B': {...},
}
```

---

## 🛠️ Technologies utilisées

- **Framework web** : Streamlit 1.28+
- **Visualisations** : Plotly 5.17+
- **Data processing** : Pandas 2.0+
- **Langage** : Python 3.9+
- **Style** : CSS3 personnalisé
- **Fonts** : Google Fonts (Poppins), JetBrains Mono

---

## 📝 Structure du projet

```
mediamatrix-demos/
├── demo_mediamatrix_v1_pro.py          # Version Professionnelle
├── demo_mediamatrix_v2_modern.py       # Version Moderne
├── demo_mediamatrix_v3_dark.py         # Version Dark Analytics
├── requirements_demo.txt               # Dépendances Python
├── launch_demo.bat                     # Script de lancement Windows
├── README.md                           # Ce fichier
├── INDEX.md                            # Index de navigation
├── QUICK_START.md                      # Guide de démarrage rapide
├── COMPARAISON_VERSIONS.md             # Comparatif détaillé
├── README_DEMOS.md                     # Documentation complète
├── RECAPITULATIF_CREATION.md           # Récapitulatif projet
└── SOMMAIRE_VISUEL.txt                 # Vue d'ensemble ASCII
```

---

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :

1. Fork le projet
2. Créer une branche (`git checkout -b feature/amelioration`)
3. Commit vos changements (`git commit -m 'Ajout fonctionnalité'`)
4. Push vers la branche (`git push origin feature/amelioration`)
5. Ouvrir une Pull Request

---

## 📄 Licence

Ce projet est un exemple de démonstration. Adaptez-le selon vos besoins !

---

## 📞 Support

Pour toute question ou problème :
- Consulter la documentation dans les fichiers `.md`
- Lire les commentaires dans les fichiers `.py`
- Vérifier `QUICK_START.md` pour les problèmes courants

---

## 🎉 Crédits

**Mediamatrix** - Optimisation de campagnes médias radio  
Powered by OR-Tools (SCIP) | Python + Streamlit

---

⭐ **Si ce projet vous est utile, n'oubliez pas de lui donner une étoile !** ⭐

# 🚀 Mediamatrix - Guide de démarrage rapide

## ⚡ Démarrage ultra-rapide

### Option 1 : Script de lancement (recommandé)
```bash
launch_demo.bat
```
Puis sélectionnez la version souhaitée (1, 2 ou 3).

### Option 2 : Ligne de commande directe

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

---

## 📦 Installation (première utilisation)

### 1. Vérifier Python
```bash
python --version
```
*(Python 3.9 ou supérieur requis)*

### 2. Installer les dépendances
```bash
pip install -r requirements_demo.txt
```

### 3. Lancer une démo
```bash
streamlit run demo_mediamatrix_v1_pro.py
```

---

## 🎯 Que contiennent ces démos ?

### Données simulées d'une vraie optimisation

**Campagne exemple :**
- Budget : 30 000 €
- Période : 19-21 Août 2024
- 87 spots optimisés
- GRP total : 94.35
- 4 radios : Chérie FM, RMC, Europe 1, Fun Radio
- 3 régies : NRJ GLOBAL, ALTICE, LAGARDÈRE

**Résultats de l'optimisation :**
- ✅ Solution optimale trouvée en 2.43 secondes
- 🎯 180 variables analysées
- 🔒 24 contraintes respectées
- 💰 99.5% du budget utilisé
- 📈 Ratio GRP/k€ : 3.16

---

## 📊 Fonctionnalités disponibles

### Dans toutes les versions :

1. **Dashboard / Vue d'ensemble**
   - KPIs principaux (spots, GRP, coût, ratio)
   - Graphiques de répartition
   - Statistiques par régie/radio

2. **Résultats / Analytics**
   - Tableaux détaillés
   - Analyses temporelles
   - Comparaisons par créneau horaire

3. **Analyses avancées**
   - Heatmaps
   - Corrélations
   - Matrices de performance

4. **Planning**
   - Liste complète des spots
   - Filtres interactifs (radio, date, créneau)
   - Export CSV

5. **Configuration**
   - Paramètres de campagne
   - Configuration du solveur
   - Informations techniques

---

## 🎨 Quelle version choisir ?

### Version 1 - Professionnelle
- **Pour qui** : Clients corporate, réunions formelles
- **Style** : Sobre, bleu, fond clair
- **Usage** : Rapports officiels, présentations clients

### Version 2 - Moderne
- **Pour qui** : Startups, marketing, événements
- **Style** : Coloré, gradients, dynamique
- **Usage** : Démos commerciales, pitchs

### Version 3 - Dark Analytics
- **Pour qui** : Développeurs, data scientists
- **Style** : Dark mode, terminal, technique
- **Usage** : Conférences tech, formations

---

## 🌐 Déploiement en ligne (gratuit)

### Sur Streamlit Cloud :

1. **Créer un compte** : [share.streamlit.io](https://share.streamlit.io)

2. **Connecter GitHub** :
   - Push votre code sur GitHub
   - Sélectionner le repo

3. **Configurer l'app** :
   - Main file: `demo_mediamatrix_v1_pro.py` (ou v2/v3)
   - Requirements: `requirements_demo.txt`

4. **Déployer** :
   - Le déploiement est automatique !
   - URL publique générée en 2-3 minutes

**Exemple d'URL** : `https://votre-app.streamlit.app`

---

## 💻 Personnalisation rapide

### Changer les données de campagne

Éditer la fonction `load_demo_data()` dans le fichier Python :

```python
campaign_config = {
    "nom_campagne": "VOTRE CAMPAGNE",
    "client": "VOTRE CLIENT",
    "budget": 50000,  # Modifier le budget
    ...
}
```

### Modifier les couleurs (Version 1)

Dans la section CSS au début du fichier :

```python
st.markdown("""
<style>
    h1 {
        color: #1e3a8a;  /* Changer cette couleur */
    }
</style>
""")
```

### Anonymiser les données

Remplacer les noms de radios/régies dans `radios_config` :

```python
radios_config = {
    'Radio A': {...},
    'Radio B': {...},
    ...
}
```

---

## 🔧 Résolution de problèmes

### "Python n'est pas reconnu..."
➜ Installer Python depuis [python.org](https://python.org) ou Microsoft Store

### "streamlit: command not found"
```bash
pip install streamlit
```

### "Module plotly not found"
```bash
pip install -r requirements_demo.txt
```

### Port déjà utilisé
Streamlit utilise le port 8501. Si occupé :
```bash
streamlit run demo_mediamatrix_v1_pro.py --server.port 8502
```

### La page ne charge pas
- Vérifier que toutes les dépendances sont installées
- Essayer de rafraîchir avec Ctrl+F5
- Vérifier la console pour les erreurs

---

## 📱 Navigation dans l'interface

### Sidebar (barre latérale)
- 🎯 Navigation entre les pages
- ℹ️ Informations contextuelles

### Pages principales
- **Dashboard** : Vue d'ensemble rapide
- **Résultats** : Tableaux détaillés
- **Analytics** : Analyses avancées
- **Planning** : Liste des spots
- **Config** : Paramètres techniques

### Interactions
- 📊 **Graphiques** : Survoler pour voir les détails
- 🔍 **Filtres** : Cliquer pour sélectionner
- 📥 **Export** : Bouton de téléchargement CSV
- 🔄 **Rafraîchir** : Bouton "Rerun" en haut à droite

---

## 📚 Documentation complète

- **README_DEMOS.md** : Documentation détaillée
- **COMPARAISON_VERSIONS.md** : Comparatif des 3 versions
- **Ce fichier** : Guide de démarrage rapide

---

## 🆘 Support

### Besoin d'aide ?

1. Consulter les fichiers README
2. Vérifier la section "Résolution de problèmes"
3. Relire les instructions d'installation

### Modifications personnalisées

Les 3 fichiers Python sont bien commentés et faciles à modifier :
- Section `load_demo_data()` : Données
- Section CSS : Styles visuels
- Sections par page : Contenu et graphiques

---

## ✨ Bonnes pratiques

### Pour une démo réussie :

1. **Tester avant** : Lancer la démo 5 min avant la présentation
2. **Préparer les transitions** : Savoir où cliquer
3. **Mode plein écran** : F11 pour masquer l'interface du navigateur
4. **Masquer sidebar** : Cliquer sur la flèche en haut à gauche si besoin
5. **Avoir un backup** : Screenshots en cas de problème technique

### Pendant la présentation :

- 🎯 Commencer par le Dashboard (vue d'ensemble)
- 📊 Montrer 2-3 graphiques clés
- 📋 Démontrer les filtres interactifs
- 💾 Faire un export CSV en direct
- ⚙️ Finir avec la page Config (aspect technique)

---

## 🎉 Prêt à lancer !

Tout est configuré et prêt à l'emploi. Il ne reste qu'à :

```bash
streamlit run demo_mediamatrix_v1_pro.py
```

Et votre démo s'ouvrira automatiquement dans votre navigateur ! 🚀

---

**Bon succès avec vos présentations Mediamatrix !** 📻✨

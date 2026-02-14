# 🚀 GUIDE COMPLET : Uploader sur GitHub

## ✅ FICHIERS PRÊTS POUR GITHUB

Tous les fichiers ont été créés dans :
`C:\Users\thoms\PycharmProjects\PythonProject\`

---

## 📋 MÉTHODE 1 : Via GitHub Desktop (PLUS SIMPLE)

### Étape 1 : Télécharger GitHub Desktop
1. Aller sur https://desktop.github.com/
2. Télécharger et installer GitHub Desktop
3. Se connecter avec votre compte GitHub (TTP0000)

### Étape 2 : Créer un nouveau repository
1. Dans GitHub Desktop : `File` → `New Repository`
2. Remplir :
   - **Name** : `mediamatrix-demos`
   - **Local Path** : `C:\Users\thoms\PycharmProjects\PythonProject`
   - **Initialize with README** : ❌ Décocher (on a déjà un README.md)
3. Cliquer sur `Create Repository`

### Étape 3 : Ajouter tous les fichiers
1. GitHub Desktop va détecter tous les fichiers automatiquement
2. En bas à gauche, dans "Summary", écrire : `Initial commit - 3 versions de démos Mediamatrix`
3. Cliquer sur `Commit to main`

### Étape 4 : Publier sur GitHub
1. Cliquer sur `Publish repository` en haut
2. Décocher `Keep this code private` si vous voulez que ce soit public
3. Cliquer sur `Publish Repository`

✅ **C'EST TERMINÉ !** Votre projet est en ligne sur GitHub !

---

## 📋 MÉTHODE 2 : Via ligne de commande Git (POUR EXPERTS)

### Prérequis : Installer Git
Si Git n'est pas installé :
1. Télécharger : https://git-scm.com/download/win
2. Installer avec les options par défaut

### Commandes à exécuter

Ouvrir PowerShell ou Git Bash dans le dossier du projet, puis :

```bash
# Se placer dans le bon dossier
cd C:\Users\thoms\PycharmProjects\PythonProject

# Initialiser le repository Git
git init

# Configurer votre identité Git (si pas déjà fait)
git config --global user.name "TTP0000"
git config --global user.email "votre-email@example.com"

# Ajouter tous les fichiers
git add .

# Créer le premier commit
git commit -m "Initial commit - 3 versions de démos Mediamatrix"

# Créer le repository sur GitHub via ligne de commande (si gh CLI installé)
# OU créer manuellement sur github.com (voir Méthode 3)

# Lier au repository GitHub (remplacer par votre URL)
git remote add origin https://github.com/TTP0000/mediamatrix-demos.git

# Pousser le code
git branch -M main
git push -u origin main
```

---

## 📋 MÉTHODE 3 : Via l'interface web GitHub

### Étape 1 : Créer le repository sur GitHub.com

1. Aller sur https://github.com/TTP0000
2. Cliquer sur le bouton vert `New` (ou `+` en haut à droite → `New repository`)
3. Remplir :
   - **Repository name** : `mediamatrix-demos`
   - **Description** : `Vitrines Streamlit pour l'optimiseur Mediamatrix - 3 versions avec styles différents`
   - **Public** ou **Private** : Au choix
   - **Initialize with** : ❌ Ne rien cocher (README, .gitignore, licence)
4. Cliquer sur `Create repository`

### Étape 2 : GitHub va vous donner des instructions

Suivre les instructions "push an existing repository from the command line" :

```bash
cd C:\Users\thoms\PycharmProjects\PythonProject
git init
git add .
git commit -m "Initial commit - 3 versions de démos Mediamatrix"
git branch -M main
git remote add origin https://github.com/TTP0000/mediamatrix-demos.git
git push -u origin main
```

---

## 🔑 Authentification GitHub

Si Git demande un mot de passe, vous avez 2 options :

### Option A : Token d'accès personnel (recommandé)
1. Aller sur https://github.com/settings/tokens
2. Cliquer sur `Generate new token` → `Generate new token (classic)`
3. Donner un nom : "Git from PC"
4. Cocher : `repo` (accès complet au repository)
5. Cliquer sur `Generate token`
6. **COPIER LE TOKEN** (vous ne le verrez qu'une fois !)
7. Quand Git demande un mot de passe, coller ce token

### Option B : GitHub CLI
```bash
# Installer GitHub CLI depuis : https://cli.github.com/
# Puis s'authentifier
gh auth login
```

---

## 📁 FICHIERS QUI SERONT UPLOADÉS

### Applications Streamlit (3 fichiers)
- ✅ `demo_mediamatrix_v1_pro.py` (18 Ko)
- ✅ `demo_mediamatrix_v2_modern.py` (20 Ko)
- ✅ `demo_mediamatrix_v3_dark.py` (28 Ko)

### Documentation (6 fichiers)
- ✅ `README.md` (pour GitHub - nouveau)
- ✅ `README_DEMOS.md`
- ✅ `COMPARAISON_VERSIONS.md`
- ✅ `QUICK_START.md`
- ✅ `RECAPITULATIF_CREATION.md`
- ✅ `SOMMAIRE_VISUEL.txt`
- ✅ `INDEX.md`

### Fichiers utilitaires (3 fichiers)
- ✅ `requirements_demo.txt`
- ✅ `launch_demo.bat`
- ✅ `.gitignore` (nouveau)

**TOTAL : 13 fichiers**

---

## ⚠️ FICHIERS À NE PAS UPLOADER

Le fichier `.gitignore` que j'ai créé exclut automatiquement :
- `__pycache__/` (cache Python)
- `.vscode/` (config VSCode)
- `venv/` (environnement virtuel)
- `.streamlit/` (config Streamlit locale)

---

## ✅ VÉRIFICATION POST-UPLOAD

Après l'upload, vérifier sur GitHub que vous voyez :

1. **Page d'accueil** : Le README.md s'affiche automatiquement
2. **13 fichiers** visibles dans la liste
3. **Badges** colorés en haut du README (Streamlit, Python, Plotly)
4. **Description** du repository visible

---

## 🌟 RENDRE LE REPO PUBLIC ET ATTRAYANT

### 1. Ajouter une description
Sur la page du repo GitHub :
- Cliquer sur ⚙️ à droite
- Ajouter : "Vitrines Streamlit pour Mediamatrix - 3 versions professionnelles"

### 2. Ajouter des topics
Toujours dans ⚙️ :
- Topics : `streamlit`, `python`, `optimization`, `plotly`, `data-visualization`, `demo`

### 3. Mettre un lien vers le site web
Si vous déployez sur Streamlit Cloud :
- Ajouter l'URL dans "Website"

---

## 🚀 DÉPLOYER SUR STREAMLIT CLOUD

Une fois sur GitHub, vous pouvez déployer en ligne gratuitement :

1. Aller sur https://share.streamlit.io
2. Se connecter avec GitHub
3. Cliquer sur `New app`
4. Sélectionner :
   - **Repository** : `TTP0000/mediamatrix-demos`
   - **Branch** : `main`
   - **Main file** : `demo_mediamatrix_v1_pro.py` (ou v2/v3)
5. Cliquer sur `Deploy`

➜ En 2-3 minutes, votre app est en ligne avec une URL publique !

---

## 🆘 RÉSOLUTION DE PROBLÈMES

### "git: command not found"
➜ Installer Git depuis https://git-scm.com/download/win

### "Permission denied"
➜ Utiliser un token d'accès personnel au lieu du mot de passe

### "Repository already exists"
➜ Utiliser un autre nom ou supprimer l'ancien repo sur GitHub

### Fichiers trop gros
➜ Tous nos fichiers sont petits, pas de problème

### "fatal: not a git repository"
➜ Vérifier que vous êtes dans le bon dossier avec `cd`

---

## 📞 BESOIN D'AIDE ?

Si vous rencontrez des problèmes :

1. **Méthode 1 (GitHub Desktop)** est la plus simple pour débuter
2. Consulter https://docs.github.com/fr/get-started
3. Me dire où ça bloque et je vous aide !

---

## ✅ CHECKLIST FINALE

Avant de commencer :
- [ ] J'ai un compte GitHub (TTP0000) ✅
- [ ] Je suis dans le bon dossier (`PythonProject`)
- [ ] J'ai choisi ma méthode (Desktop / CLI / Web)
- [ ] Tous les fichiers sont prêts

Après l'upload :
- [ ] Le repo est visible sur GitHub
- [ ] Le README.md s'affiche correctement
- [ ] Les 13 fichiers sont présents
- [ ] (Optionnel) J'ai déployé sur Streamlit Cloud

---

🎉 **UNE FOIS UPLOADÉ, VOTRE URL SERA :**

https://github.com/TTP0000/mediamatrix-demos

**Partagez-la à vos clients et collègues !** 🚀

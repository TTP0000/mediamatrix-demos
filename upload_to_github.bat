@echo off
:: Script d'upload automatique vers GitHub

echo ================================================
echo   UPLOAD VERS GITHUB - MEDIAMATRIX DEMOS
echo ================================================
echo.

echo [1/5] Initialisation Git...
git init
if errorlevel 1 (
    echo ERREUR : Git non installe !
    echo Telechargez : https://git-scm.com/download/win
    pause
    exit /b 1
)
echo.

echo [2/5] Configuration Git...
git config user.name >nul 2^>^&1
if errorlevel 1 (
    set /p username="Nom GitHub (ex: TTP0000): "
    git config --global user.name "%%username%%"
)
git config user.email >nul 2^>^&1
if errorlevel 1 (
    set /p email="Email GitHub: "
    git config --global user.email "%%email%%"
)
echo.

echo [3/5] Ajout des fichiers...
git add .
echo.

echo [4/5] Creation du commit...
git commit -m "Initial commit - 3 versions de demos Mediamatrix"
echo.

echo [5/5] Instructions push...
echo.
echo ================================================
echo   DERNIERE ETAPE
echo ================================================
echo.
echo 1. Creer le repo sur GitHub :
echo    https://github.com/new
echo    Nom : mediamatrix-demos
echo.
echo 2. Executer ces commandes :
echo.
echo    git remote add origin https://github.com/TTP0000/mediamatrix-demos.git
echo    git branch -M main
echo    git push -u origin main
echo.
echo ================================================
echo.
pause

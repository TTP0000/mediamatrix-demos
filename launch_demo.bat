@echo off
:: Script de lancement des démos Mediamatrix
:: Sélection interactive de la version à lancer

echo.
echo ========================================
echo   MEDIAMATRIX - Lanceur de demos
echo ========================================
echo.
echo Selectionnez la version a lancer :
echo.
echo [1] Version Professionnelle (Corporate)
echo [2] Version Moderne Coloree
echo [3] Version Dark Analytics
echo [Q] Quitter
echo.

set /p choice="Votre choix (1/2/3/Q) : "

if /i "%choice%"=="1" (
    echo.
    echo Lancement de la version Professionnelle...
    streamlit run demo_mediamatrix_v1_pro.py
) else if /i "%choice%"=="2" (
    echo.
    echo Lancement de la version Moderne...
    streamlit run demo_mediamatrix_v2_modern.py
) else if /i "%choice%"=="3" (
    echo.
    echo Lancement de la version Dark Analytics...
    streamlit run demo_mediamatrix_v3_dark.py
) else if /i "%choice%"=="Q" (
    echo.
    echo Au revoir !
    exit /b
) else (
    echo.
    echo Choix invalide !
    pause
    goto :EOF
)

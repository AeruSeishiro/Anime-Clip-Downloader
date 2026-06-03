@echo off
title Anime Clip Downloader
echo ================================================
echo   Anime Clip Downloader
echo ================================================
echo.
echo Installing requirements...
pip install yt-dlp --quiet
echo.
echo Starting download...
echo.
python anime_downloader.py
echo.
pause
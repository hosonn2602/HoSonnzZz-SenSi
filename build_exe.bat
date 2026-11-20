@echo off
title Build HoSonn Sensi Pro
python -m pip install --upgrade pip
python -m pip install pyinstaller psutil
pyinstaller --noconfirm --onefile --windowed --name HoSonn_Sensi_Pro HoSonn_Sensi_Pro.py
echo.
echo Build xong! Kiem tra file trong thu muc dist.
pause

REM This batch file is a record of how the executable was built.

python -m nuitka --windows-console-mode=disable --onefile --windows-company-name=marvl --windows-product-version=1.0 --windows-icon-from-ico=data\cubeicon.ico --output-dir=build caveControl.py
REM python -O -m PyInstaller -w -D -i data\cubeicon.ico --noconfirm caveControl.py
pause

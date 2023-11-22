REM This batch file is a record of how the executable was built.

REM python -OO -m nuitka --windows-disable-console --standalone --plugin-enable=tk-inter --plugin-enable=anti-bloat --plugin-enable=upx --windows-company-name=marvl --windows-product-version=1.0  --windows-icon-from-ico=cubeicon.ico --output-dir=build caveControl.py
python -O -m PyInstaller -w -D -i  cubeicon.ico caveControl.py
pause

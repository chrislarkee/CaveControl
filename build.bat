REM This batch file is a record of how the executable was built.
REM This requires PyInstaller, of course.
python -OO -m PyInstaller -w -F -a -i cubeicon.ico caveControl.py

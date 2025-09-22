@echo off
title Photo Tool Packaging with UPX in Clean Venv

REM ====== Configuration ======
set UPX_PATH=E:\upx-5.0.2-win64\upx-5.0.2-win64
set VENV_DIR=venv

@REM set MAIN_SCRIPT=photo_tools.py
set MAIN_SCRIPT=version1.3.py

set REQUIREMENTS_GENERATOR=packup_need.py
set OUTPUT_NAME=PhotoTool

echo -----------------------------------
echo [0/3] Creating a clean virtual environment...
echo -----------------------------------
if exist "%VENV_DIR%" rd /s /q "%VENV_DIR%"
python -m venv %VENV_DIR%
if ERRORLEVEL 1 (
    echo Failed to create virtual environment. Please check your Python installation.
    pause
    exit /b
)

REM Activate virtual environment
call %VENV_DIR%\Scripts\activate

echo -----------------------------------
echo [1/3] Detecting dependencies and generating requirements.txt...
echo -----------------------------------
python %REQUIREMENTS_GENERATOR%
if ERRORLEVEL 1 (
    echo Failed to generate requirements.txt. Please check %REQUIREMENTS_GENERATOR%.
    deactivate
    pause
    exit /b
)

echo -----------------------------------
echo [2/3] Installing required dependencies...
echo -----------------------------------
pip install --upgrade pip >nul -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install pyinstaller -i https://pypi.tuna.tsinghua.edu.cn/simple

echo -----------------------------------
echo [3/3] Building exe with UPX compression...
echo -----------------------------------
pyinstaller --onefile --noconsole --clean --distpath . --name %OUTPUT_NAME% --upx-dir "%UPX_PATH%" %MAIN_SCRIPT%

REM Deactivate virtual environment
deactivate

echo -----------------------------------
echo Done!
echo Executable file: %cd%\%OUTPUT_NAME%.exe
echo -----------------------------------
pause
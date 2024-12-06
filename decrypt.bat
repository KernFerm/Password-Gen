@echo off
REM Save the current directory
pushd %~dp0

REM Check if main_tensorrt.py exists
if not exist de.py (
    echo Error: de.py not found in the current directory.
    popd
    pause
    exit /b 1
)

REM Run the Python script and check for errors
echo Running de.py...
python de.py
if %errorlevel% neq 0 (
    echo Error: de.py did not run successfully. Error level: %errorlevel%
    popd
    pause
    exit /b %errorlevel%
)

REM Provide success feedback
echo de.py ran successfully.

REM Return to the original directory
popd
pause

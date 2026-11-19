@echo off
cd /d "%~dp0"
py -3 bootstrap.py %*
if errorlevel 1 (
  echo.
  echo The launcher exited with an error.
  exit /b 1
)

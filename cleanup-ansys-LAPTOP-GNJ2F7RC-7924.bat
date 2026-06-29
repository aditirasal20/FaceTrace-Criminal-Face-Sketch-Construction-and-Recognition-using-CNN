@echo off
set LOCALHOST=%COMPUTERNAME%
if /i "%LOCALHOST%"=="LAPTOP-GNJ2F7RC" (taskkill /f /pid 18832)
if /i "%LOCALHOST%"=="LAPTOP-GNJ2F7RC" (taskkill /f /pid 7924)

del /F cleanup-ansys-LAPTOP-GNJ2F7RC-7924.bat

@echo off
set LOCALHOST=%COMPUTERNAME%
if /i "%LOCALHOST%"=="LAPTOP-GNJ2F7RC" (taskkill /f /pid 1828)
if /i "%LOCALHOST%"=="LAPTOP-GNJ2F7RC" (taskkill /f /pid 11496)

del /F cleanup-ansys-LAPTOP-GNJ2F7RC-11496.bat

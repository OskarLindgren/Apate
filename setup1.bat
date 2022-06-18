

@echo off
color 0c
CHCP 65001
echo ^◄ Made by Oskar Lindgren (https://github.com/OskarLindgren) ^►
echo.
set /p a="Enter the exe name for virus: "
if [%a%]==[] ( 
    echo.
    echo Please enter a name
    pause
    EXIT /B 1
) 
if [%a%] NEQ [] (
    echo.
    echo Name is: %a%
    pyinstaller --clean --onefile -i NONE -n %a% encrypt.py
    rmdir /s /q __pycache__
    rmdir /s /q build
    del /f / s /q %a%.spec
    ren dist output
    echo.
    echo generated exe as %a%.exe in the output folder
    echo.
    pause
    EXIT /B 1
)
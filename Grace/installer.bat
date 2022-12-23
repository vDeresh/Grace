@echo off
cd dwnl
cls
@echo Nacisnij dowolny przycisk aby przejsc do instalacji pythona
pause>nul
start https://www.python.org/ftp/python/3.10.9/python-3.10.9-amd64.exe
cls
@echo Otworz instalator pythona i postepuj zgodnie z instrukcjami
@echo ZAZNACZ OPCJE 'Add Python to PATH' PODCZAS INSTALACJI
@echo Nacisnij dowolny przycisk aby kontynuowac
pause>nul
timeout 1
start instl.bat
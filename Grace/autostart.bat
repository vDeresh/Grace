@ECHO OFF
cd \Grace
copy Grace.lnk "%AppData%\Microsoft\Windows\Start Menu\Programs\Startup"
cd dwnl
cd msg
start powodzenieAutostart.vbs
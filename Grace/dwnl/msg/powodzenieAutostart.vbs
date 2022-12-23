Set objShell = CreateObject("WScript.Shell")

dim result
result = msgbox("Program zostal dodany do autostartu." & vbNewLine & "Kliknij OK, aby zobaczyc go w folderze", vbInformation + vbOKCancel, "Grace uruchomi sie wraz ze startem systemu")

if result = vbOK then
  objShell.Run "explorer.exe %AppData%\Microsoft\Windows\Start Menu\Programs\Startup"
end if

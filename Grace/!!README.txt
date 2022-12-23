Przenieś folder "Grace" do głównego folderu dysku systemowego (C:)

Aby zainstalować - uruchom plik "installer"

Jeżeli chcesz żeby Grace uruchamiała się wraz ze startem systemu - uruchom plik "autostart"



Nowe polecenia należy dodawać pod linijką 127 (w kodzie asystenta) stosując się do następującego wzoru:

elif "<słowo lub fraza na jaką ma reagować grace (bez dużych liter)>" in command:
	os.system("<Polecenie jakie powinna wykonać Grace w konsoli CMD>") # ----------------------- Polecenie w konsoli CMD (Opcjonalne)
	os.system("start <Nazwa skrótu który jest w C:\Grace>.lnk") # ------------------------------ Otwarcie określonego programu (Opcjonalne)
	webbrowser.open_new_tab("http://<discord.gg/7hbbrbzjpY>") # -------------------------------- Otwarcie określonej strony (Opcjonalne)
	speak("<To co powinna odpowiedzieć Grace>", 'pl-PL') # ------------------------------------- (Opcjonalne)

Rzeczy, które są w ostrych nawiasach ("<>") są opcjonalne i należy je zapisywać bez tych nawiasów.
"elif" powinno być zapisane w tej samej (pionowej) linii co inne "elif" a opcjonalne komendy muszą być oddzielone od tej linii tabem.
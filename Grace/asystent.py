import webbrowser
import speech_recognition as sr
import pyttsx3
import os
import datetime
import wikipedia
import time
import random
import pyautogui
import unicodedata
import string

wikipedia.set_lang("pl")

characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def start():
  os.system("cls")
  now = datetime.datetime.now()
  obecnydzien = now.strftime("%d-%m-%Y")
  obecnagodzina = now.strftime("%H:%M:%S")
  print("")
  print(obecnydzien)
  print(obecnagodzina)
  print("")
  print("⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⠛⠋⠉⠈⠉⠉⠉⠉⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
  print("⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⣿⣿⣿⣿⣿⣿")
  print("⣿⣿⣿⣿⡏⣀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿")
  print("⣿⣿⣿⢏⣴⣿⣷⠀⠀⠀⠀⠀⢾⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿")
  print("⣿⣿⣟⣾⣿⡟⠁⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣷⢢⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿")
  print("⣿⣿⣿⣿⣟⠀⡴⠄⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿")
  print("⣿⣿⣿⠟⠻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠶⢴⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⣿⣿⣿")
  print("⣿⣁⡀⠀⠀⢰⢠⣦⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⡄⠀⣴⣶⣿⡄⣿⣿⣿")
  print("⣿⡋⠀⠀⠀⠎⢸⣿⡆⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⠗⢘⣿⣟⠛⠿⣼⣿⣿")
  print("⣿⣿⠋⢀⡌⢰⣿⡿⢿⡀⠀⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣧⢀⣼⣿⣿")
  print("⣿⣿⣷⢻⠄⠘⠛⠋⠛⠃⠀⠀⠀⠀⠀⢿⣧⠈⠉⠙⠛⠋⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿")
  print("⣿⣿⣧⠀⠈⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⠀⠀⠀⠀⢀⢃⠀⠀⢸⣿⣿⣿⣿⣿⣿")
  print("⣿⣿⡿⠀⠴⢗⣠⣤⣴⡶⠶⠖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡸⠀⣿⣿⣿⣿⣿⣿")
  print("⣿⣿⣿⡀⢠⣾⣿⠏⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠉⠀⣿⣿⣿⣿⣿⣿")
  print("⣿⣿⣿⣧⠈⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿")
  print("⣿⣿⣿⣿⡄⠈⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿")
  print("⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
  print("⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
  print("⣿⣿⣿⣿⣿⣦⣄⣀⣀⣀⣀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
  print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
  print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠙⣿⣿⡟⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
  print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠁⠀⠀⠹⣿⠃⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
  print("⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢐⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
  print("⣿⣿⣿⣿⠿⠛⠉⠉⠁⠀⢻⣿⡇⠀⠀⠀⠀⠀⠀⢀⠈⣿⣿⡿⠛⠛⠛⠉⠉⠉")
  print("⣿⡿⠋⠁⠀⠀⢀⣀⣠⡴⣸⣿⣇⡄⠀⠀⠀⠀⢀⡿⠄⠙⠛⠀⣀⣠⣤⣤⠄⠀")

def speak(text, language):
  engine = pyttsx3.init()
  engine.setProperty('recognizer_instance.non_speaking_duration', 0.2)
  engine.setProperty('recognizer_instance.energy_threshold', 10)
  engine.say(text)
  engine.runAndWait()

def listen(language):
  start()
  r = sr.Recognizer()
  r.language = "pl-PL"
  with sr.Microphone() as source:
    audio = r.listen(source)
  try:
    return r.recognize_google(audio, language='pl-PL')
  except sr.UnknownValueError:
    return "Błąd 400"
  except sr.RequestError as e:
    print("Error making request: {0}".format(e))
    return ""

def uspienie():
  r = sr.Recognizer()
          
  with sr.Microphone() as source:
    print("Podaj czas:")
    speak("Na ile minut?", 'pl-PL')
    audio = r.listen(source)
    
  try:
    czas = r.recognize_google(audio, language="pl-PL")
    czas = int(czas)
    speak(f"Do zobaczenia za {czas} minut", 'pl-PL')
    czas = czas * 60
    time.sleep(czas)

  except sr.UnknownValueError:
    speak("Nie rozumiem, powtórz jeszcze raz", 'pl-PL')
    uspienie()
  
  except sr.RequestError as e:
    speak("Wystąpił jakiś błąd")
    print(f"Wystąpił błąd: {e}")
    time.sleep(6)
  
  uspienie()

def wyszukajinternet():
  speak("Co wyszukać?", 'pl-PL')
      
  r = sr.Recognizer()
      
  with sr.Microphone() as source:
    print("Co wyszukać?")
    audio = r.listen(source)
    
  try:
    search_term = r.recognize_google(audio, language="pl-PL")
    print(f"Wyszukuję: {search_term}")
    webbrowser.open("https://www.google.pl/search?q=" + search_term)
  except sr.UnknownValueError:
    print("Przepraszam, nie zrozumiałam tego co powiedział*ś.")
    speak("Nie zrozumiałam tego co powiedziałeś.", 'pl-PL')
    wyszukajinternet()
  except sr.RequestError as e:
    print(f"Wystąpił błąd: {e}")

def napisz():
  speak("Co napisać?", 'pl-PL')
      
  r = sr.Recognizer()
      
  with sr.Microphone() as source:
    print("Co napisać?")
    audio = r.listen(source)
    
  try:
    pisanie = r.recognize_google(audio, language='pl-PL')
    nPisanie = unicodedata.normalize("NFD", pisanie)
    ndPisanie = nPisanie.capitalize()
    print(f"Zrozumiałam: {ndPisanie}")
    pyautogui.typewrite(ndPisanie)
  except sr.UnknownValueError:
    print("Przepraszam, nie zrozumiałam tego co powiedział*ś.")
    speak("Nie zrozumiałam tego co powiedziałeś.", 'pl-PL')
    napisz()
  except sr.RequestError as e:
    print(f"Wystąpił błąd: {e}")

def main():
  while True:
    command = listen('pl-PL').lower()
    if "cześć" in command:
      speak("W czym mogę pomóc?", 'pl-PL') # -------------------- Przywitanie
    
    elif "siema" in command:
      speak("W czym mogę pomóc?", 'pl-PL') # -------------------- Przywitanie
    
    elif "hej" in command:
      speak("W czym mogę pomóc?", 'pl-PL') # -------------------- Przywitanie
    
    elif "elo" in command:
      speak("W czym mogę pomóc?", 'pl-PL') # -------------------- Przywitanie
    
    elif "lubię cię" in command:
      speak("Niestety nie posiadam uczuć ale myślę że jeśli byłabym człowiekiem to też bym cię polubiła", 'pl-PL')
    
    elif "jak masz na imię" in command:
      speak("Mam na imię Grace.", 'pl-PL') # -------------------- Imię
      
    elif "włącz chrome" in command:
      os.system("chrome.exe")
      speak("Otwieram przeglądarkę Google Chrome", 'pl-PL') # --- Google Chrome (Włącz)
      
    elif "wyłącz chrome" in command:
      os.system("taskkill /IM chrome.exe /F")
      speak("Zamykam przeglądarkę Google Chrome", 'pl-PL') # ---- Google Chrome (Wyłącz)
      
    elif "włącz operę" in command:
      os.system("start .\operagx.lnk")
      speak("Otwieram przeglądarkę Opera GX", 'pl-PL') # -------- Opera GX (Włącz)
    
    elif "wyłącz operę" in command:
      os.system("taskkill /IM opera.exe /F")
      speak("Zamykam przeglądarkę Opera GX", 'pl-PL') # --------- Opera GX (Wyłącz)
    
    elif "włącz spotify" in command:
      os.system("start Spotify.lnk")
      speak("Otwieram Spotify", 'pl-PL') # ---------------------- Spotify (Włącz)
    
    elif "wyłącz spotify" in command:
      os.system("taskkill /IM Spotify.exe /F")
      speak("Zamykam Spotify", 'pl-PL') # ----------------------- Spotify (Wyłącz)
    
    elif "włącz visual studio" in command:
      os.system("start VisualStudioCode.lnk")
      speak("Uruchamiam Visual Studio Code", 'pl-PL') # --------- Visual Studio Code (Włącz)
    
    elif "włącz discorda" in command:
      os.system("start Discord.lnk")
      speak("Uruchamiam Discorda", 'pl-PL') # ------------------- Discord (Włącz)
    
    elif "wyłącz discorda" in command:
      os.system("taskkill /IM Discord.exe /F")
      speak("Zamykam Discorda", 'pl-PL') # ---------------------- Discord (Wyłącz)
      
    elif "włącz cpu-z" in command:
      os.system("start CPU.lnk")
      speak("Uruchamiam C P U Z", 'pl-PL') # -------------------- CPU-Z (MSC)
      
    elif "wlącz monitor wydajności" in command:
      os.system("perfmon.msc")
      speak("Uruchamiam monitor wydajności", 'pl-PL') # --------- Monitor Wydajności
      
    elif "włącz czat" in command:
      os.system("start https://chat.openai.com/chat")
      speak("Otwieram ChatGPT", 'pl-PL') # ---------------------- ChatGPT
      
    elif "włącz konsolę" in command:
      os.system("start")
      os.system("start Grace.bat.lnk")
      break # --------------------------------------------------- Konsola
    
    elif "włącz notatnik" in command:
      os.system("start notepad.lnk") # -------------------------------- Notatnik
      
    elif "włącz kalkulator" in command: 
      os.system("start calc.lnk") # ----------------------------------- Kalkulator
      
    elif "podaj ciekawostkę" in command:
      random_page = wikipedia.random(pages=1)
      summary = wikipedia.summary(random_page, sentences=3)
      print(summary)
      speak(summary, 'pl-PL') # --------------------------------- Ciekawostka z Wikipedii
      
    elif "wyszukaj w internecie" in command:
      wyszukajinternet() # -------------------------------------- Wyszukiwanie w internecie

    elif "napisz" in command:
      napisz()
      
    elif "otwórz swoją lokalizację" in command:
      os.system("start \Grace")
      speak("Otwieram folder Grace", 'pl-PL') # ----------------- Lokalizacja Grace
      
    elif "wyłącz się" in command:
      speak("Do zobaczenia.", 'pl-PL')
      os.system("color c")
      os.system("color f")
      break # --------------------------------------------------- Wyłącz (Grace)
    
    elif "uruchom ponownie" in command:
      os.system("start Grace.bat.lnk")
      break # --------------------------------------------------- Uruchom ponownie (Grace)
    
    elif "uśpij się" in command:
      uspienie() # ---------------------------------------------- Uśpienie (Grace)
      
    elif "uruchom komputer ponownie" in command:
      speak("Restartuję komputer", 'pl-PL')
      os.system("shutdown/g") # --------------------------------- Restart komputera
    
    elif "wyłącz komputer" in command:
      speak("Do zobaczenia", 'pl-PL')
      os.system("shutdown/p") # --------------------------------- Wyłączenie komputera
    
    elif "test" in command:
      speak("Testuję", 'pl-PL')
      
      random_page = wikipedia.random(pages=1)
      summary = wikipedia.summary(random_page, sentences=1) # ----------------------------- Sprawdza działanie bilbioteki "Wikipedia"
      
      now = datetime.datetime.now()
      obecnydzien = now.strftime("%d-%m-%Y")
      obecnagodzina = now.strftime("%H:%M:%S") # ------------------------------------------ Sprawdza działanie bilbioteki "Datetime"
      
      nazwapliku = ''.join(random.choices(characters, k=31))
      ciag = ''.join(random.choices(characters, k=64)) # ---------------------------------- Sprawdza działanie bilbioteki "Random"
      
      os.system(f'echo {obecnydzien} >> "%USERPROFILE%\Desktop\K{nazwapliku}.txt"') # ----- Sprawdza działanie bilbioteki "Random"
      os.system(f'echo {obecnagodzina} >> "%USERPROFILE%\Desktop\K{nazwapliku}.txt"') # --- Sprawdza działanie bilbioteki "Datetime"
      os.system(f'echo {ciag} >> "%USERPROFILE%\Desktop\K{nazwapliku}.txt"')
      os.system(f'del "%USERPROFILE%\Desktop\K{nazwapliku}.txt"') # ----------------------- Sprawdza działanie bilbioteki "OS"
      
      time.sleep(1) # --------------------------------------------------------------------- Sprawdza działanie bilbioteki "Time"
      
      speak("Test przebiegł pomyślnie", 'pl-PL') # -------------- Test
    
    elif "support" in command:
      webbrowser.open_new_tab("https://discord.gg/7hbbrbzjpY")
    
    else:
      print("")
      print("Powtórz jeszcze raz")

speak("Witaj.", 'pl-PL')

if __name__ == "__main__":
  main()
  
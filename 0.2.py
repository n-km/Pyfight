#Bitte hier den Namen ändern
name = ("user")
#Bitte hier das Geschlecht ändern
#(Entweder 'Junge' oder 'Mädchen')
geschlecht = ("###")

#Jetzt können Sie das Programm schließen



import time
import os
clear = lambda: os.system('cls')
print("Name:", name)
print("Geschlecht:", geschlecht)
sure = input("Stimmt das so? (J/N)")
    if sure == (""):
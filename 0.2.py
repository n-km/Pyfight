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
visitenkarteName = ("Name:", name)
print("Geschlecht:", geschlecht)
visitenkarteGeschlecht = ("Geschlecht:", geschlecht)
sure = input("Stimmt das so? (J/N)")
if sure == ("J"):
    visitenkarte = (visitenkarteName, visitenkarteGeschlecht)
    print("Ok, deine Visitenkarte wurde erstellt")
if sure == ("N"):
    exit("Du bist nicht einverstanden")
time.sleep(2)
print("User aktiv:", visitenkarte)
import time
import os
clear = lambda: os.system('cls')
#Startet Programm
print("Programm startet...")
time.sleep(1)
clear()
#Einleitung
print("/")
time.sleep(0.1)
clear()
print("/*")
time.sleep(0.1)
clear()
print("/**")
time.sleep(0.1)
clear()
print("/***")
time.sleep(0.1)
clear()
print("/****")
time.sleep(0.1)
clear()
print("/*****")
time.sleep(0.1)
clear()
print("/******")
time.sleep(0.1)
clear()
print("/*******")
time.sleep(0.1)
clear()
print("/********")
time.sleep(0.1)
clear()
print("/*********")
time.sleep(0.1)
clear()
print("/**********")
time.sleep(0.1)
clear()
print("/***********")
time.sleep(0.1)
clear()
print("/************")
time.sleep(0.1)
clear()
print("/*************")
time.sleep(0.1)
clear()
print("/**************")
time.sleep(0.1)
clear()
print("/**************")
time.sleep(0.1)
clear()
print("/***************")
time.sleep(0.1)
clear()
print("/****************")
time.sleep(0.1)
clear()
print("/*****************")
time.sleep(0.1)
clear()
print("/******************")
time.sleep(0.1)
clear()
print("/*******************/")
time.sleep(1)
clear()
print("*/Pyfght/*")
print("Registrierung:")
name = input("* Der Name lautet:")
clear()
print("Name wurde eingetragen", name)
time.sleep(2)
clear()
print("Du musst deine ultimative Kraft auswählen.")
print("Dir stehen folgende zur Verfügung:")
print("A - Feuer (Ein Feuerstrahl, der für 10 Sekunden lang pro Sekunde 5 Schaden verursacht)")
print("B - Wasser (Ein Wasserstrahl, der 30 Schaden verursacht, senkt Angriffe von einer Gegnerischen Karte um 10 Schaden)")
print("C - Gift (Ein Biss, wo jedes Mal, wenn der Gegner angegriffen hat, verliert seine Karte 10 Lebespunkte)")
ulti = input("Geben Sie (A), (B) oder (C) an:")
if ulti == ("C"):
    print("Deine Ultimative Kraft ist Feuer.")
if ulti == ("B"):
    print("Deine Ultimative Kraft ist Wasser.")
if ulti == ("C"):
    print("Deine Ultimative Kraft ist Gift.")
else:
    clear()
    print("Da du keine Ultimative Kraft ausgewählt hast, musst du das Programm Neustarten.")
    time.sleep(5)
    clear()
    print("Das Programm schließt automatisch in 3 Sekunden")
    time.sleep(1)
    print("Das Programm schließt automatisch in 2 Sekunden")
    time.sleep(1)
    print("Das Programm schließt automatisch in 1 Sekunden")
    time.sleep(1)
    print("Das Programm schließt automatisch in 0 Sekunden")
    time.sleep(0.3)
    exit("Keine Ultimative Kraft ausgewählt")

time.sleep(0.5)
print("Danke für deine Daten.")
time.sleep(2)
clear()
print("Wir erstellen deine Visitenkarte.")
print("(Ultimative Kraft wird gespeichert)")
time.sleep(0.3)
clear()
print("Wir erstellen deine Visitenkarte.. ")
print("(Ultimative Kraft wird gespeichert)")
visitenkarteUlti = ("Ultimative Kraft:", ulti)
time.sleep(0.3)
clear()
print("Wir erstellen deine Visitenkarte... ")
print("(Ultimative Kraft wurde gespeichert)")
time.sleep(0.3)
clear()
print("Wir erstellen deine Visitenkarte... ")
print("(Name wird gespeichert)")
visitenkarteName = ("Name:",  name)
time.sleep(0.3)
clear()
print("Wir erstellen deine Visitenkarte.")
print("(Visitenkarte wird gedruckt)")
visitenkarte = (visitenkarteName, visitenkarteUlti)
time.sleep(0.3)
clear()
print("Visitenkarte erfolgreich erstellt.")
time.sleep(1)
print(visitenkarte)
print("Sie haben den Setup-Prozess erfolgreich absolviert.")
input("Drücken Sie 'ENTER', um das Spiel zu starten...")
clear()
print("Dialog (Du musst 'ENTER' drücken,  um den Dialog zu folgen):")
input("Du gehst an einer Informatikschule, die mitten in einer futuristischen Stadt ist...")
input("Eines Tages bekommst du die Möglichkeit, dir ein elektronisches Haustier auszusuchen...")
input("Was nimmt du?...")
input("Ist es A - Ein mit Messern ausgestattetes Haustier (Assasine)...")
input("Ist es B - Ein mit Schild und Schwert ausgerüstetes Haustier (Tank)...")
input("Ist es C - Ein mit Bogen ausgestattetes Haustier (Bow)...")
print("Wähle behutsam dein Haustier aus. Bitte nur A B oder C eingeben.")
pet1 = input("->")
if pet1 == ("A"):
    clear()
    print("Herzlichen Glückwunsch!")
    print("Ihr neues Haustier ist Assassine!")
    time.sleep(0.5)
    print("Ihr Haustier wird direkt in Ihr Inventar registriert.")
    pet1 = ("Assassine(Lvl.1)")
    inventar = ("Ihr Inventar:", pet1)
    print(inventar)
    input("Bestätigen Sie mit 'ENTER'...")
if pet1 == ("B"):
    clear()
    print("Herzlichen Glückwunsch!")
    print("Ihr neues Haustier ist Tank!")
    time.sleep(0.5)
    print("Ihr Haustier wird direkt in Ihr Inventar registriert.")
    pet1 = ("Tank(Lvl.1)")
    inventar = ("Ihr Inventar:", pet1)
    print(inventar)
    input("Bestätigen Sie mit 'ENTER'...")
if pet1 == ("C"):
    clear()
    print("Herzlichen Glückwunsch!")
    print("Ihr neues Haustier ist Bow!")
    time.sleep(0.5)
    print("Ihr Haustier wird direkt in Ihr Inventar registriert.")
    pet1 = ("Bow(Lvl.1)")
    inventar = ("Ihr Inventar:", pet1)
    print(inventar)
    input("Bestätigen Sie mit 'ENTER'...")

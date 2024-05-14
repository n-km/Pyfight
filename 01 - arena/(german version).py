import time
import os
clear = lambda: os.system('cls')

name = "Developer" # Muss was eingegeben sein!
# A - Feuer
# B - Wasser
# C - Gift
ulti = "C" # A, B oder C
# A - Assassine
# B - Tank
# C - Bow
pet1 = "B" # A, B oder C
pet1lvl = 1
# Text-Arts


if pet1 == "A":
    selflife = 70
    selfdamage = 25
if pet1 == "B":
    selflife = 150
    selfdamage = 25
if pet1 == "C":
    selflife = 70
    selfdamage = 45

if name == "":
    input("Sie haben vergessen, Ihre Daten einzutragen.(ENTER zum schließen)...")
    exit()
if ulti == "":
    input("Sie haben vergessen, Ihre Daten einzutragen.(ENTER zum schließen)...")
    exit()
if pet1 == "":
    input("Sie haben vergessen, Ihre Daten einzutragen.(ENTER zum schließen)...")
    exit()
if ulti == "A":
    ulti = "Feuer"
if ulti == "B":
    ulti = "Wasser"
if ulti == "C":
    ulti = "Gift"
if pet1 == "A":
    pet1 = "Assassine"
if pet1 == "B":
    pet1 = "Tank"
if pet1 == "C":
    pet1 = "Bow"
print("Name:", name)
print("Ulti:", ulti)
print("Haustier:", pet1)
print("PetLvl:", pet1lvl)
request = input("Richtig so? j/n")
if request == "j":
    print("ok.")
    time.sleep(0.5)
if request == "n":
    print("ok.")
    time.sleep(0.5)
    exit()
if request == "":
    print("Du musst eine Antwort geben!")
    time.sleep(0.5)
    exit()
clear()
print("Sie befinden sich in den Arena-Modus.")
print("Wollen Sie spielen? j/n")
play = input("->")
if play == "n":
    exit()
if play == "j":
    clear()
    input("Ihr gegner ist ein Assassine...")
    enemylife = 70
    enemydamage = 25
    print("Lebenspunkte:", enemylife)
    print("Angriffsschaden:", enemydamage)
    wantfight = input("Wollen Sie angreifen? j/n")
    if wantfight == ("j"):
        if pet1 == ("Tank"):
            print(pet1)
            clear()
            print("Gegner: Assassine")
            print("Lebenspunkte:", enemylife)
            print("Angriffsschaden:", enemydamage)
            print("Sie:", pet1)
            print("Lebenspunkte:", selflife)
            print("Angriffsschaden:", selfdamage)
            print("⋘※※※※※※※※※※⋙")
            print("[A]-Angreifen (25)")
            print("[B]-Schild (0)")
            fight = input("|->")
            if fight == "A":
                enemylife = (enemylife-selfdamage)
                print("Gegnerlebenspunkte:" ,enemylife)
            if fight == "B":
                print("Schild wird verwendet")
                shieldactive = ("on")
            if selflife == 0:
                print("Du hast verloren.")
            if enemylife == 0:
                print("Du hast gewonnen.")
            if selflife > 0:
                print("")
        if pet1 == ("Assassine"):
            print(pet1)
            clear()
        if pet1 == ("Bow"):
            print(pet1)
            clear()
    if wantfight == ("n"):
        exit()

input("Hier endet das Programm, da hier noch Baustelle ist...")
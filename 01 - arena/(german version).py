import time
import os
clear = lambda: os.system('cls')

name = "name" # Muss was eingegeben sein!
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

def print_tank():
    print(" ()____()  ")
    print("/--o--o--\ ")
    print("\---__---/ ")
    print("/--------\ ")
    print("---------- ")
    print("\-,,--,,-/ ")
def print_inventory():
    print(name)
    print(ulti)
    print(pet1, pet1lvl)



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
if pet1 == "Tank":
    print_tank()
print("PetLvl:")
input(pet1lvl)
clear()
print("Sie befinden sich in den Arena-Modus.")
print("Wollen Sie spielen? j/n")
play = input("->")
if play == "n":
    exit()
if play == "j":
    clear()
    input("Ihr gegner ist ein Assassine...")
    enemylife = 100
    print("Assassine:", enemylife)


input("Hier endet das Programm, da hier noch Baustelle ist...")
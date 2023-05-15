# SEM IMPORTNI  #   VŽDY   # nejaké PYTHON MODULS Napr : from time import sleep , random , pyautogui , NEZABUDNI NA TO ! #

#
from time import sleep
import os
#

#
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[34m'
#orange = '\033[033m'
orange = '\033[38;5;208m'
magenta = '\033[35m'
cyan = '\033[36m'
reset = '\033[0m'
#

# Sen som dal definíciu, ktorá uloží (premenné) OUTPUT lepšie povedané do textového súboru menom : Dotazník.txt

def save_output(output):
    with open ("Dotaznik.txt", "w") as file:
        file.write(output)

def checkFile():
    if not os.path.exists("Dotaznik.txt"):
        with open("Dotaznik.txt", "w") as file:
            file.write("")

output = ""

checkFile()

print("\n")
print("čau rád ťa zase vidím viem, že si práve prišiel zo školy : \n")
print("ak máš čas tak vyplň aspoň tento formulár : \n")
a = input(f"Napíš svoje meno a priezvisko :{green} {reset}")
b = input(f"Napíš svoju adresu :{green} {reset}")
c = input(f"Tvoje telefone číslo :{green} {reset}")
d = input(f"rodne číslo :{green} {reset}")
e = input(f"číslo MAMINY :{green} {reset}")
f = input(f"číslo OTCA :{green} {reset}")
print("ak si vyplnil formulár čaká ta už iba prekvapenie \n")
print(f"{red}Prepocitavame to ... {reset}")
sleep(2)
print("Pockajte PROSÍM !\n")
sleep(1)

# VYPISOVANIE
print(f"{orange}Meno a Priezvisko {reset}:" , a + "\n")
print(f"{orange}Adresa {reset}:" , b + "\n")
print(f"{orange}Telefonne cislo : {reset}:" , c + "\n")
print(f"{orange}Rodne cislo {reset}:" , d + "\n")
print(f"{orange}Cislo MAMINY {reset}:" , e + "\n")
print(f"{orange}E-mail :{orange}: ,"\n")

# ZAPISOVANIE DO Textoveho suboru

output += ("        : Vsetky Vase udaje su TU : ")
output += ("")
output += ("---------------------------------------\n")
output += ("- Meno a Priezvisko : " + a + " - ")
output += ("\n---------------------------------------\n")
output += ("")

output += ("")
output += ("\n---------------------------------------\n")
output += ("Adresa : " + b + " - ")
output += ("\n---------------------------------------\n")
output += ("")

output += ("")
output += ("---------------------------------------\n")
output += ("Telefonne cislo : " + c + " - ")
output += ("\n---------------------------------------\n")
output += ("")

output += ("")
output += ("---------------------------------------\n")
output += ("Rodne cislo : " + d + " - ")
output += ("\n---------------------------------------\n")
output += ("")

output += ("")
output += ("---------------------------------------\n")
output += ("Cislo MAMINY : " + e + " - ")
output += ("\n---------------------------------------\n")
output += ("")

output += ("")
output += ("---------------------------------------\n")
output += ("Cislo OTCA :" + f + " - ")
output += ("\n---------------------------------------\n")
output += ("")

output += ("\nDakujeme za pouzivanie Nasho Dotaznika :D\nPrajeme Vam Pekny den.\n")

save_output(output)

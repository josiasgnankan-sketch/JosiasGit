from datetime import *
import os
import time

VERT = "\033[92m"
BLEU = "\033[94m"
JAUNE = "\033[93m"
ROUGE = "\033[91m"
RESET = "\033[0m"

def date_now():
    thedate=date.today()
    afficher_boite("date_aujourd'hui", thedate.strftime("%d/%m/%Y"))
    

def affiche_hour():
    thedate= datetime.now()
    afficher_boite("l'heure",thedate.strftime("%H:%M:%S"))

def affiche_hour_date():
    thedate=datetime.now()
    afficher_boite("HEURE ET LA DATE",thedate.strftime("%A,%B %Y %H:%M:%S"))
    

def afficher_information():
    print("====INFORMATION====")
    thedate=datetime.now()
    
    print("╔══════════════════════════════════════╗")
    print("║       INFORMATIONS DÉTAILLÉES       ║")
    print("╠══════════════════════════════════════╣")
    print(f"║ Jour : {thedate.strftime('%A'):<27} ║")
    print(f"║ Mois : {thedate.strftime('%B'):<27} ║")
    print(f"║ Année : {thedate.strftime('%Y'):<26} ║")
    print(f"║ Jour de l'année : {thedate.strftime('%j'):<16} ║")
    print(f"║ Jour de la semaine : {thedate.strftime('%u'):<13} ║")
    print(f"║ Semaine de l'année : {thedate.strftime('%U'):<13} ║")
    print("╚══════════════════════════════════════╝")

def afficher_boite(titre, contenu):
    print("╔══════════════════════════════════════╗")
    print(f"║ {titre:^36} ║")
    print("╠══════════════════════════════════════╣")
    print(f"║ {contenu:^36} ║")
    print("╚══════════════════════════════════════╝")

def horloge():
    while True:
        os.system("clear")

        maintenant = datetime.now()

        print("╔══════════════════════════════════════╗")
        print("║          HORLOGE EN DIRECT          ║")
        print("╠══════════════════════════════════════╣")
        print(f"║              {maintenant.strftime('%H:%M:%S')}              ║")
        print("╚══════════════════════════════════════╝")

        print()
        print("Tapez q puis Entrée pour quitter.")

        choix = input("Votre choix : ")

        if choix.lower() == "q":
            break

def menu():
  
    while True:
       
        print(BLEU+" ╔══════════════════════════════════════╗"+RESET)
        print(BLEU+" ║       GESTIONNAIRE DE DATE           ║"+RESET)
        print(BLEU+" ╠══════════════════════════════════════╣"+RESET)
        print(" ║                                      ║")
        print(VERT+" ║  [1] Date d'aujourd'hui              ║"+RESET)
        print(VERT+" ║  [2] Heure actuelle                  ║"+RESET)
        print(VERT+" ║  [3] Date et heure                   ║"+RESET)
        print(JAUNE+" ║  [4] Informations                    ║"+RESET)
        print(ROUGE+" ║  [5] Horloge                         ║"+RESET)
        print(" ║        [6] Quitter                            ║")
        print(" ╚══════════════════════════════════════╝")
        choix=input("Entrez votre choix :")
        if choix=="1":
          date_now()
          input("\nAppuyez sur Entrée pour revenir au menu...")
        elif choix=="2":
            affiche_hour()
            input("\nAppuyez sur Entrée pour revenir au menu...")
        elif choix=="3":
            affiche_hour_date()
            input("\nAppuyez sur Entrée pour revenir au menu...")
        elif choix=="4":
            afficher_information()
            input("\nAppuyez sur Entrée pour revenir au menu...")
        elif choix=="5":
            horloge()
        elif choix=="6":
            print("Au-revoir !")
            break
        else:
            menu()
if __name__=="__main__":
   menu()
    

        
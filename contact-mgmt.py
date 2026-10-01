FILENAME="contact.txt"
#afficher les contacts
def afficher_contact(contacts):
    if not contacts:
        return
    print(f"Vos {len(contacts)} contacts:")
    for i,( nom,telephone) in enumerate(contacts,1):
        print(f"{i}_{nom}-{telephone}")
def charger_contacts():
    contacts=[]
    try:
     with open( FILENAME , "r" , encoding="UTF-8") as fichier:
         print("Vous avez ouvert ce fichier")
         for ligne in fichier:
           ligne=ligne.strip()
           if ligne:
               nom,telephone=ligne.split(";")
               contacts.append([nom,telephone])
               print(f"{len(contacts)} contacts chargé ")
               #charger les contacts pour pouvoir les récupérés

    except FileNotFoundError:
         print("Nouveau fichier de contacts ")
    return contacts

#ajouter les contacts
def ajout_contact(contacts):
    print("Entrez votre nom ainsi que votre contacts")
    nom=input("nom:")
    Telephone=input("Téléphone:")
    if nom and Telephone:
        contacts.append([nom, Telephone])
        print(f"{nom} ajouté !")
    else:
        print("Nom et téléphonnes obligatoire")



#sauver les contacts et quitter
def menu():
    print("Que voulez-vous faire ?")
    contacts=charger_contacts()

    while True:
        print("1 - voir les contacts")
        print("2 - Ajouter les contacts")
        print("3 - Sauver les contacts")
        print("4 - Modifier un contact")
        print("5 - Supprimer un contact")

        choix=input("Entrez votre choix: ")
        if choix== "1":
            afficher_contact(contacts)
        elif choix=="2":
            ajout_contact(contacts)
        elif choix=="3":
            sauvegarder(contacts)
            break
        elif choix=="4":
            modify(contacts)
        elif choix=="5":
            drop(contacts)
        else:
            print("Quelle opération voudriez-vous faire ?")

def sauvegarder(contacts):
    with open(FILENAME,"w",encoding="UTF-8") as fichier:
        for nom,telephone in contacts:
            fichier.write(f"{nom};{telephone}\n")
    print (f"{len(contacts)}contacts enregistré")

def modify(contacts):
        selected=input("quelle contacts voudriez-vous modifier ?")
        for i, (nom,Telephone ) in enumerate(contacts):
            if selected==nom:
                nouveau_nom=input("Entrez le nouveau nom:")
                nouveau_contacts=input("Entrez votre nouveau contact")
                contacts[i][0]=nouveau_nom
                contacts[i][1]=nouveau_contacts
                sauvegarder(contacts)
                print("contact modifié !")
        print ("contact introuvable")

        return

def drop(contacts):
    selected=input("Quelle contacts voudriez-vous supprimer ?:")
    for i,(nom,Telephone) in enumerate(contacts):
        if selected==nom:
            del contacts[i]
            sauvegarder(contacts)
            print("contact supprimé")
            return



    
            
if __name__=="__main__":
   menu()
   
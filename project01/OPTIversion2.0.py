import hashlib
import json
import os.path

capitalalphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
smallalphabets = "abcdefghijklmnopqrstuvwxyz"
specialchar = "!@#$%^&*"
digits = "0123456789"

# Charger les mots de passe existants depuis le fichier JSON
if os.path.exists("passwords.json"):
    with open("passwords.json", "r") as f:
        passwords = json.load(f)
else:
    passwords = {}

def valid_password(mdp):
    l, u, p, d = 0, 0, 0, 0  
    if len(mdp) < 8:
        return False
    for i in mdp:
        if i in smallalphabets:
            l += 1
        if i in capitalalphabets:
            u += 1
        if i in digits:
            d += 1
        if i in specialchar:
            p += 1
    return (l >= 1 and u >= 1 and p >= 1 and d >= 1 and l + p + u + d == len(mdp))

def add_hachage(hashed_password):
    passwords[hashed_password] = ""
    with open("passwords.json", "w") as f:
        json.dump(passwords, f, indent=2) 
        

while True:
    print('\033[1;37m\n__________________[ MENU ]___________________ :')
    print('\033[1;33m \n1.\033[0m  Ajouter un mot de passe')
    print('\033[1;33m2. \033[0m Afficher les mots de passe enregistrés')
    print('\033[1;33m3. \033[0m Quitter')
    print('\033[1;37m_____________________________________________')
    choix = input("\033[1;34m\nSaisir une option : \033[0m")

    if choix == "1":
        while True:
            mdp = input("\033[1;34m\nChoisir un mot de passe : \033[0m ")

            if valid_password(mdp):

                hashed_password = hashlib.sha256(mdp.encode()).hexdigest() # hachage
                if hashed_password in passwords:
                    print("\033[1;41m\nMot de passe déjà enregistré.\033[0m")
                    print("\033[1;33mVeuillez saisir une des options proposées.\033[0m")
                    break

                else:
                    print("\033[1;32m\nMot de passe valide.\033[0m")
                    dl_choice = input("\033[1;33mSouhaitez-vous l'enregistrer ?\033[0m  \033[1;37m1 : OUI, 2 : NON\033[0m")

                    if dl_choice == "1":
                         add_hachage(hashed_password)
                         print("\033[1;32m\nMot de passe enregistré avec succès !\033[0m")
                         break

                    else:
                        print("\033[1;33m\nRetour au menu, veuillez choisir une des options proposées :\033[0m")
                        break
            else:
                print("\033[1;41m\nMot de passe invalide.\033[0m")
                print("\033[1;31mVeuillez entrer un mot de passe de minimum 8 caractères.\033[0m")
                print("\033[1;31mContenant au moins une lettre minuscule, une lettre majuscule, un chiffre et un caractère spécial parmi ceux-ci : ! @ # $ % ^ & *\033[0m")
   

    elif choix == "2":
            if passwords:
                 for hashed_password in passwords:
                     print("\033[1;32m\nMOTS DE PASSE :\033[0m",hashed_password)
            else:
                print("\033[1;41m\nAucun mot de passe enregistré.\033[0m")
                print("\033[1;33mVeuillez choisir une des options proposées.\033[0m")

    # EXIT
    elif choix == "3":
        break

    else:
        print("\033[1;41m\nCOMMANDE INVALIDE\033[0m")
        print("\033[1;33mAppuyez sur une des touches 1 / 2 / 3  de votre clavier !")


# PERMETTRE D ENLEVER LE " " APRES LE HACHAGE DANS LE .JSON

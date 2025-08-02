#!/data/data/com.termux/files/usr/bin/python3

import os
import sys
import hashlib
import getpass
from style import display_banner

# Configuration
PASSWORD_FILE = "/data/data/com.termux/files/usr/etc/termux_password.hash"
MAX_ATTEMPTS = 3
LOCK_FILE = "/data/data/com.termux/files/usr/etc/termux_lock"

def clear_screen():
    os.system('clear')

def create_password():
    clear_screen()
    display_banner()
    print("\n\033[1;36m[+] Création du mot de passe pour Termux\033[0m")
    
    while True:
        pwd = getpass.getpass("\033[1;34mEntrez votre nouveau mot de passe: \033[0m")
        confirm_pwd = getpass.getpass("\033[1;34mConfirmez le mot de passe: \033[0m")
        
        if pwd == confirm_pwd:
            if len(pwd) < 4:
                print("\033[1;31mLe mot de passe doit contenir au moins 4 caractères!\033[0m")
                continue
            
            # Hacher le mot de passe avec SHA-256
            hashed_pwd = hashlib.sha256(pwd.encode()).hexdigest()
            
            # Enregistrer le mot de passe haché
            with open(PASSWORD_FILE, 'w') as f:
                f.write(hashed_pwd)
            
            print("\n\033[1;32m[+] Mot de passe enregistré avec succès!\033[0m")
            print("\033[1;33m[!] Redémarrez Termux pour activer la protection\033[0m")
            break
        else:
            print("\033[1;31mLes mots de passe ne correspondent pas. Réessayez!\033[0m")

def check_password():
    if not os.path.exists(PASSWORD_FILE):
        return True
    
    if os.path.exists(LOCK_FILE):
        print("\033[1;31mTrop de tentatives échouées. Termux est verrouillé.\033[0m")
        print("\033[1;33mSupprimez le fichier", LOCK_FILE, "pour réessayer.\033[0m")
        sys.exit(1)
    
    attempts = 0
    with open(PASSWORD_FILE, 'r') as f:
        stored_hash = f.read().strip()
    
    while attempts < MAX_ATTEMPTS:
        clear_screen()
        display_banner()
        print("\n\033[1;36m[+] Termux Protégé - Authentification Requise\033[0m")
        print(f"\033[1;33mTentative {attempts + 1}/{MAX_ATTEMPTS}\033[0m")
        
        pwd = getpass.getpass("\033[1;34mEntrez le mot de passe: \033[0m")
        input_hash = hashlib.sha256(pwd.encode()).hexdigest()
        
        if input_hash == stored_hash:
            return True
        else:
            print("\033[1;31mMot de passe incorrect!\033[0m")
            attempts += 1
    
    # Si toutes les tentatives échouent
    with open(LOCK_FILE, 'w') as f:
        f.write("locked")
    print("\033[1;31mTrop de tentatives échouées. Termux verrouillé.\033[0m")
    sys.exit(1)

def change_password():
    if check_password():
        create_password()

def remove_password():
    if os.path.exists(PASSWORD_FILE):
        os.remove(PASSWORD_FILE)
        print("\033[1;32m[+] Protection par mot de passe désactivée\033[0m")
    else:
        print("\033[1;33m[!] Aucune protection par mot de passe active\033[0m")

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == "--setup":
            create_password()
        elif sys.argv[1] == "--change":
            change_password()
        elif sys.argv[1] == "--remove":
            remove_password()
        elif sys.argv[1] == "--help":
            show_help()
        else:
            print("\033[1;31mOption non reconnue\033[0m")
            show_help()
    else:
        # Mode normal - vérification du mot de passe
        if os.path.exists(PASSWORD_FILE):
            if check_password():
                # Lancer le shell normal
                os.system('/data/data/com.termux/files/usr/bin/login')

def show_help():
    print("\033[1;36mTermux Password Protector - Aide\033[0m")
    print("\033[1;34mOptions disponibles:\033[0m")
    print("  --setup    : Configurer la protection par mot de passe")
    print("  --change   : Changer le mot de passe")
    print("  --remove   : Supprimer la protection par mot de passe")
    print("  --help     : Afficher ce message d'aide")

if __name__ == "__main__":
    main()

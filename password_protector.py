#!/data/data/com.termux/files/usr/bin/python3

import os
import sys
import hashlib
import termios
import tty
from style import display_banner, show_warning

PASSWORD_FILE = "/data/data/com.termux/files/usr/etc/termux_password.hash"
MAX_ATTEMPTS = 3
LOCK_FILE = "/data/data/com.termux/files/usr/etc/termux_lock"

def getpass(prompt):
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        sys.stdout.write(prompt)
        sys.stdout.flush()
        password = ""
        while True:
            ch = sys.stdin.read(1)
            if ch == '\r' or ch == '\n':
                break
            password += ch
            sys.stdout.write('*')
            sys.stdout.flush()
        return password
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
        print()

def clear_screen():
    os.system('clear')

def create_password():
    clear_screen()
    display_banner()
    print("\n\033[1;36m[+] Création du mot de passe pour Termux\033[0m")
    
    while True:
        pwd = getpass("\033[1;34mEntrez votre nouveau mot de passe: \033[0m")
        confirm_pwd = getpass("\033[1;34mConfirmez le mot de passe: \033[0m")
        
        if pwd == confirm_pwd:
            if len(pwd) < 4:
                print("\033[1;31mLe mot de passe doit contenir au moins 4 caractères!\033[0m")
                continue
            
            hashed_pwd = hashlib.sha256(pwd.encode()).hexdigest()
            
            with open(PASSWORD_FILE, 'w') as f:
                f.write(hashed_pwd)
            
            print("\n\033[1;32m[+] Mot de passe enregistré avec succès!\033[0m")
            break
        else:
            print("\033[1;31mLes mots de passe ne correspondent pas. Réessayez!\033[0m")

def check_password():
    if not os.path.exists(PASSWORD_FILE):
        return True
    
    if os.path.exists(LOCK_FILE):
        show_warning()
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
        
        pwd = getpass("\033[1;34mEntrez le mot de passe: \033[0m")
        input_hash = hashlib.sha256(pwd.encode()).hexdigest()
        
        if input_hash == stored_hash:
            return True
        else:
            show_warning()
            attempts += 1
    
    with open(LOCK_FILE, 'w') as f:
        f.write("locked")
    show_warning()
    print("\033[1;31mTrop de tentatives échouées. Termux verrouillé.\033[0m")
    sys.exit(1)

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == "--setup":
            create_password()
        elif sys.argv[1] == "--change":
            if check_password():
                create_password()
        elif sys.argv[1] == "--remove":
            if os.path.exists(PASSWORD_FILE):
                os.remove(PASSWORD_FILE)
                print("\033[1;32m[+] Protection par mot de passe désactivée\033[0m")
        elif sys.argv[1] == "--help":
            print("\033[1;36mOptions:\033[0m")
            print("  --setup   : Configurer le mot de passe")
            print("  --change  : Changer le mot de passe")
            print("  --remove  : Supprimer la protection")
    else:
        if os.path.exists(PASSWORD_FILE):
            if check_password():
                os.system('/data/data/com.termux/files/usr/bin/login')

if __name__ == "__main__":
    main()

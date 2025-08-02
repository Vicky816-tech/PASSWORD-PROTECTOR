#!/data/data/com.termux/files/usr/bin/bash

echo "[*] Installation de Termux Password Protector"

# Vérifier si Python est installé
if ! command -v python3 &> /dev/null; then
    echo "[!] Python3 n'est pas installé. Installation en cours..."
    pkg install python -y
fi

# Copier les fichiers
echo "[*] Copie des fichiers..."
mkdir -p /data/data/com.termux/files/usr/etc/
cp password_protector.py /data/data/com.termux/files/usr/bin/termux-auth
cp style.py /data/data/com.termux/files/usr/etc/

# Rendre les fichiers exécutables
chmod +x /data/data/com.termux/files/usr/bin/termux-auth

# Configurer le shell personnalisé
echo "[*] Configuration du shell personnalisé..."
mv /data/data/com.termux/files/usr/bin/login /data/data/com.termux/files/usr/bin/login.real
echo '#!/data/data/com.termux/files/usr/bin/bash' > /data/data/com.termux/files/usr/bin/login
echo 'exec termux-auth "$@"' >> /data/data/com.termux/files/usr/bin/login
chmod +x /data/data/com.termux/files/usr/bin/login

# Configurer le mot de passe
echo "[*] Configuration du mot de passe initial..."
termux-auth --setup

echo "[+] Installation terminée avec succès!"
echo "[!] Redémarrez Termux pour activer la protection"

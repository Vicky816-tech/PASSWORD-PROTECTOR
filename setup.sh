#!/data/data/com.termux/files/usr/bin/bash

echo "[*] Installation de Termux Password Protector"

# Vérifier et configurer le dépôt si nécessaire
if ! termux-change-repo 2>/dev/null; then
    echo "[*] Configuration du dépôt par défaut..."
    termux-change-repo
fi

# Vérifier les dépendances
pkg update -y
pkg install git python -y

# Copier les fichiers
echo "[*] Copie des fichiers..."
mkdir -p /data/data/com.termux/files/usr/etc/
cp password_protector.py /data/data/com.termux/files/usr/bin/termux-auth
cp style.py /data/data/com.termux/files/usr/etc/

# Configurer les permissions
chmod 755 /data/data/com.termux/files/usr/etc/style.py
chmod +x /data/data/com.termux/files/usr/bin/termux-auth

# Backup et remplacement du shell
echo "[*] Configuration du shell..."
if [ ! -f /data/data/com.termux/files/usr/bin/login.real ]; then
    mv /data/data/com.termux/files/usr/bin/login /data/data/com.termux/files/usr/bin/login.real
fi

echo '#!/data/data/com.termux/files/usr/bin/sh' > /data/data/com.termux/files/usr/bin/login
echo 'exec termux-auth "$@"' >> /data/data/com.termux/files/usr/bin/login
chmod +x /data/data/com.termux/files/usr/bin/login

# Initialisation
echo "[*] Configuration initiale..."
termux-auth --setup

echo "[+] Installation terminée avec succès!"
echo "[!] Redémarrez Termux pour activer la protection"

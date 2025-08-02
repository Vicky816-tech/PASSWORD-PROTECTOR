#!/data/data/com.termux/files/usr/bin/bash

echo "[*] Désinstallation de Termux Password Protector"

# Restaurer le shell original
if [ -f /data/data/com.termux/files/usr/bin/login.real ]; then
    echo "[*] Restauration du shell original..."
    rm -f /data/data/com.termux/files/usr/bin/login
    mv /data/data/com.termux/files/usr/bin/login.real /data/data/com.termux/files/usr/bin/login
fi

# Supprimer les fichiers
echo "[*] Suppression des fichiers..."
rm -f /data/data/com.termux/files/usr/bin/termux-auth
rm -f /data/data/com.termux/files/usr/etc/termux_password.hash
rm -f /data/data/com.termux/files/usr/etc/termux_lock
rm -f /data/data/com.termux/files/usr/etc/style.py

echo "[+] Désinstallation terminée avec succès!"
echo "[!] Redémarrez Termux pour appliquer les changements"

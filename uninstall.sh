#!/data/data/com.termux/files/usr/bin/bash

echo "[*] Désinstallation de Termux Password Protector"

if [ -f /data/data/com.termux/files/usr/bin/login.real ]; then
    rm -f /data/data/com.termux/files/usr/bin/login
    mv /data/data/com.termux/files/usr/bin/login.real /data/data/com.termux/files/usr/bin/login
fi

rm -f /data/data/com.termux/files/usr/bin/termux-auth
rm -f /data/data/com.termux/files/usr/etc/termux_password.hash
rm -f /data/data/com.termux/files/usr/etc/termux_lock
rm -f /data/data/com.termux/files/usr/etc/style.py

echo "[+] Désinstallation terminée avec succès!"
echo "[!] Redémarrez Termux pour appliquer les changements"

#!/data/data/com.termux/files/usr/bin/bash

echo "[*] Installation de Termux Password Protector"

pkg update -y
pkg install python -y

mkdir -p /data/data/com.termux/files/usr/etc/
cp password_protector.py /data/data/com.termux/files/usr/bin/termux-auth
cp style.py /data/data/com.termux/files/usr/etc/

chmod +x /data/data/com.termux/files/usr/bin/termux-auth

if [ ! -f /data/data/com.termux/files/usr/bin/login.real ]; then
    mv /data/data/com.termux/files/usr/bin/login /data/data/com.termux/files/usr/bin/login.real
fi

echo '#!/data/data/com.termux/files/usr/bin/sh' > /data/data/com.termux/files/usr/bin/login
echo 'exec termux-auth "$@"' >> /data/data/com.termux/files/usr/bin/login
chmod +x /data/data/com.termux/files/usr/bin/login

echo "[*] Configuration du mot de passe initial..."
termux-auth --setup

echo "[+] Installation terminée avec succès!"
echo "[!] Redémarrez Termux pour activer la protection"

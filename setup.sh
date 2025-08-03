#!/data/data/com.termux/files/usr/bin/bash

# Installation des dépendances
pkg install -y python

# Création des répertoires nécessaires
mkdir -p /data/data/com.termux/files/usr/etc/

# Copie des fichiers
cp password_protector.py /data/data/com.termux/files/usr/bin/termux-auth
cp style.py /data/data/com.termux/files/usr/etc/

# Configuration des permissions
chmod 755 /data/data/com.termux/files/usr/bin/termux-auth
chmod 644 /data/data/com.termux/files/usr/etc/style.py

# Backup du shell original
if [ ! -f /data/data/com.termux/files/usr/bin/login.real ]; then
    mv /data/data/com.termux/files/usr/bin/login /data/data/com.termux/files/usr/bin/login.real
fi

# Création du wrapper
echo '#!/data/data/com.termux/files/usr/bin/sh' > /data/data/com.termux/files/usr/bin/login
echo 'exec /data/data/com.termux/files/usr/bin/termux-auth "$@"' >> /data/data/com.termux/files/usr/bin/login
chmod 755 /data/data/com.termux/files/usr/bin/login

# Configuration initiale
echo "Configuration du mot de passe :"
python3 /data/data/com.termux/files/usr/bin/termux-auth --setup

echo "Installation terminée avec succès!"
echo "Redémarrez Termux pour activer la protection"

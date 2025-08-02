# 🔒 Termux Password Protector 🔒
**PROJET OFFICIEL DEDSEC | OWNER: SPOTY MTF**  

![DEDSEC Logo](https://img.icons8.com/color/96/000000/anonymous-mask.png)

## 📝 Description
Un système de sécurité pour Termux qui protège l'accès à votre terminal par mot de passe. Développé par la **TEAM DEDSEC** pour une sécurité maximale.

## ✨ Fonctionnalités
- 🔑 Protection par mot de passe SHA-256
- ⚠️ Blocage après 3 tentatives échouées
- 🎨 Interface stylisée avec logo DEDSEC
- ♻️ Compatible avec toutes les versions récentes de Termux

## 🚀 Installation
Copiez-collez ces commandes dans Termux :

```bash
# Mise à jour du système
pkg update -y && pkg upgrade -y

# Installation des dépendances
pkg install -y git python

# Téléchargement du projet
git clone https://github.com/spotymtf/PASSWORD-PROTECTOR.git
cd PASSWORD-PROTECTOR

# Installation
chmod +x setup.sh
./setup.sh

# Cours 5 

Installation de node sur ubuntu, executez le script suivant : 
```bash
# sudo apt uninstall node npm si installé
sudo apt install curl && curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
source ~/.bashrc
nvm install v22
node -v
npm -v
```

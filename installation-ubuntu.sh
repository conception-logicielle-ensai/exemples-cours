# Mise a jour de l'index des paquets existant pour l'installation via apt
echo "Pour utiliser le compte administrateur du poste (sudo), vous devez entrer votre motdepasse (ensai)"
sudo apt update
echo "mise a jour systeme"
sudo apt upgrade -y
echo "installation outils-base git-all c++"
sudo apt install ca-certificates git-all build-essential curl libpq-dev -y

# installation vscode via snap
sudo snap install code --classic
echo "Installation extensions vscode"
code --install-extension ms-kubernetes-tools.vscode-kubernetes-tools
code --install-extension ms-python.debugpy
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance
code --install-extension redhat.vscode-yaml
code --install-extension rvest.vs-code-prettier-eslint
# Installation de python via pyenv (d'après https://github.com/pyenv/pyenv)
echo "version python3 systeme"
python3 --version 
curl -fsSL https://pyenv.run | bash # pyenv automatic installer
pyenv install 3.13
pyenv global 3.13
echo "version python3 & pip apres installation via pyenv"
python3 --version
pip --version
# installation de nvm pour installer node et npmjs
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
source ~/.bashrc
nvm install --lts
echo "version de node et de npm"
node -v && npm -v 
npm install --global prettier
# installation selenium geckodriver
mkdir -p ~/Downloads
curl -Lo ~/Downloads/geckodriver.tar.gz https://github.com/mozilla/geckodriver/releases/download/v0.35.0/geckodriver-v0.35.0-linux64.tar.gz
tar -xvzf ~/Downloads/geckodriver.tar.gz -C ~/Downloads/
sudo chmod +x ~/Downloads/geckodriver
sudo mv ~/Downloads/geckodriver /usr/local/bin/
echo "installation du geckodriver"
geckodriver --version

# installation docker
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y
sudo service docker restart
sudo docker --version

# installation kubectl
curl -Lo ~/Downloads/kubectl "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" 
chmod +x ~/Downloads/kubectl
sudo mv ~/Downloads/kubectl /usr/local/bin/kubectl

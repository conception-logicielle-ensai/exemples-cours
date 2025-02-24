print_section() {
    local message=$1  # Récupère le message passé en argument
    local separator="++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

    echo "\n\n$separator"
    echo "++++ $message +++++"
    echo "$separator\n\n"
}


print_section "Récupération des informations sur les packages"
sudo apt update -y
sudo apt upgrade -y
print_section "Installation de vscode"
sudo snap install code --classic
print_section "Installation extensions vscode"
code --install-extension ms-kubernetes-tools.vscode-kubernetes-tools
code --install-extension ms-python.debugpy
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance
code --install-extension redhat.vscode-yaml
code --install-extension rvest.vs-code-prettier-eslint
print_section "installation de python"
sudo apt install  -y python3-pip git-all python3-virtualenv
print_section "version de python et de pip:"
python3 --version
pip --version
print_section "Installation d'outils de dev"
sudo apt install -y curl libpq-dev
print_section "Installation de node et de npm"
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
source ~/.bashrc
nvm install v22
echo "version de node et de npm"
node -v && npm -v 
npm install --global prettier
print_section "Installation d'un geckodriver"
mkdir -p ~/downloads
curl -Lo ~/downloads/geckodriver.tar.gz https://github.com/mozilla/geckodriver/releases/download/v0.35.0/geckodriver-v0.35.0-linux64.tar.gz
tar -xvzf ~/downloads/geckodriver.tar.gz -C ~/downloads/
sudo chmod +x ~/downloads/geckodriver
sudo mv geckodriver /usr/local/bin/
echo "version du geckodriver"
geckodriver --version
print_section "Installation de chrome"
if [[ $(getconf LONG_BIT) = "64" ]]
then
    echo "64bit Detected" &&
    echo "Installing Google Chrome" &&
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb &&
    sudo dpkg -i google-chrome-stable_current_amd64.deb &&
    rm -f google-chrome-stable_current_amd64.deb
else
    echo "32bit Detected" &&
    echo "Installing Google Chrome" &&
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_i386.deb &&
    sudo dpkg -i google-chrome-stable_current_i386.deb &&
    rm -f google-chrome-stable_current_i386.deb
fi

print_section "Installation de chromium"
sudo apt-get install chromium-browser
print_section "Installation de chromedriver"
curl -Lo ~/downloads/chromedriver.zip https://storage.googleapis.com/chrome-for-testing-public/133.0.6943.53/linux64/chromedriver-linux64.zip
unzip -o ~/downloads/chromedriver.zip -d ~/downloads
mv ~/downloads/chromedriver-linux64/chromedriver ~/downloads/chromedriver
sudo chmod +x ~/downloads/chromedriver
sudo mv ~/downloads/chromedriver /usr/bin/chromedriver
print_section "desinstallation de firefox via snap, reinstallation de firefox via apt
echo "kill"
pkill firefox
sudo snap remove firefox
sudo install -d -m 0755 /etc/apt/keyrings
wget -q https://packages.mozilla.org/apt/repo-signing-key.gpg -O- | sudo tee /etc/apt/keyrings/packages.mozilla.org.asc > /dev/null
echo "deb [signed-by=/etc/apt/keyrings/packages.mozilla.org.asc] https://packages.mozilla.org/apt mozilla main" | sudo tee -a /etc/apt/sources.list.d/mozilla.list > /dev/null
echo "
Package: *
Pin: origin packages.mozilla.org
Pin-Priority: 1000

Package: firefox*
Pin: release o=Ubuntu
Pin-Priority: -1' | sudo tee /etc/apt/preferences.d/mozilla"
echo "installation de firefox"
sudo apt update && sudo apt remove firefox
sudo apt install firefox

print_section "installation de docker"
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo service docker restart

print_section "installation de kubectl"

curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.16.0/bin/linux/amd64/kubectl
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/kubectl

windowsUser=$1

mkdir -p ~/.kube
ln -sf "/mnt/c/users/$windowsUser/.kube/config" ~/.kube/config


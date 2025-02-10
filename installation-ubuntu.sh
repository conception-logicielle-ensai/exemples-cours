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
unzip ~/downloads/chromedriver.zip -d ~/downloads
mv ~/downloads/chromedriver-linux64/chromedriver ~/downloads/chromedriver
sudo chmod +x ~/downloads/chromedriver
sudo mv ~/downloads/chromedriver /usr/bin/chromedriver

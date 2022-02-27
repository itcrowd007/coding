#!/bin/bash

apt update && apt upgrade -y 

apt install tor

sed  '/ControlPort/s/^#//g' -i /etc/tor/torrc
sed 's/#CookieAuthentication 1/CookieAuthentication 0/' -i /etc/tor/torrc
echo "ExitNodes {ru}" >> /etc/tor/torrc
/etc/init.d/tor restart

curl ifconfig.me; echo

torify curl ifconfig.me ; echo


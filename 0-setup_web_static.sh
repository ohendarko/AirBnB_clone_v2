#!/usr/bin/env bash
# Sets up your web servers for the deployment of web_static

apt-get update
apt -y install nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "<html><body>Fake File</body></html>" | tee /data/web_static/releases/test/index.html

#Symbolic links
ln -sf /data/web_static/releases/test/ /data/web_static/current

#Ownership
chown -R ubuntu:ubuntu /data/

#Nginx configs
sudo sed -i '39 i\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-enabled/default

sudo service nginx restart

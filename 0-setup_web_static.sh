#!/usr/bin/env bash
# Sets up your web servers for the deployment of web_static

apt-get update
apt-get -y install nginx
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "<html><body>Fake File</body></html>" > /data/web_static/releases/test/index.html

#Symbolic links
rm -rf /data/web_static/current
ln -s /data/web_static/releases/test/ /data/web_static/current

#Ownership
chown -R ubuntu:ubuntu /data/

#Nginx configs
sudo sed -i '39 i\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-enabled/default

sudo service nginx restart
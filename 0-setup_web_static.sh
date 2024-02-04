#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

sudo apt-get update
sudo apt-get -y install nginx
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "<html><body>Fake File</body></html>" > /data/web_static/releases/test/index.html

#Symbolic links
sudo rm -rf /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

#Ownership
sudo chown -R ubuntu:ubuntu /data/

#Nginx configs
echo "
server {
  listen 80;
  server_name _;

  location /hbnb_static/ {
    alias /data/web_static/current/;
    index index.html;
  }
}
" | sudo tee /etc/nginx/sites-available/default

sudo service nginx restart
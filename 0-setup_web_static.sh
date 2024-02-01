#!/usr/bin/env bash
# Script sets up my web servers for the deployment of web_static.
sudo apt-get update
sudo apt-get install nginx -y
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo 'Hello Webserver' | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '18i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart

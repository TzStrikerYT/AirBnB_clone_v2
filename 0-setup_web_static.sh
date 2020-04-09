#!/usr/bin/env bash
# Write a Bash script that sets up your web servers for the deployment of web_static
sudo apt-get update -y
sudo apt-get install nginx -y
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo echo -e '<html>\n<head>\n</head>\n<body>\nHolberton School\n</body>\n</html>' > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "38i location /hbnb_static {\nalias /data/web_static/current;\n}" /etc/nginx/sites-enabled/default
sudo service ngnix start

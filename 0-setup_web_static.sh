#!/usr/bin/env bash
# Sets up the web servers for the deployment of web_static

apt-get update
apt-get -y install nginx
mkdir -p /data/web_static/releases/test /data/web_static/shared/
echo '<html>
  <head>
  </head>
  <body>
    Hello World!: I am Aoudair Chakib from alx-se
  </body>
</html>' > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i "s/location */location \/hbnb_static/" /etc/nginx/sites-available/default
sed -i '/location \/hbnb_static/ a \		alias \/data\/web_static\/current\/;' /etc/nginx/sites-available/default
service nginx restart

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
echo 'server {
	listen 80 default_server;
	listen [::]:80 default_server;

	server_name _;
	index index.html index.htm;
	error_page 404 /404.html;
	add_header X-Served-By \$hostname;

	location / {
		root /var/www/html/;
		try_files \$uri \$uri/ =404;
	}

	location /hbnb_static/ {
		alias /data/web_static/current;
		try_files \$uri \$uri/ =404;
	}
}' > /etc/nginx/sites-available/default
service nginx restart

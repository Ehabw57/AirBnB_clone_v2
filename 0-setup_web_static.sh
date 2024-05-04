#!/usr/bin/env bash
# Sets up  my web server for deployment
# Install Nginx
apt-get update -y
apt-get install nginx -y
service nginx start

# Create the folders if it does'nt exists
mkdir -p /data/web_static/{releases/test,shared}

# Create a fake HTML file
echo "Hello Web" > /data/web_static/releases/test/index.html

# Create a forced symbolic link 
ln -sf /data/web_static/releases/test /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
chown -R ubuntu:ubuntu /data

# Update and restart Nginx
echo "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    location /hbnb_static {
        alias /data/web_static/current;
    }

    location /redirect_me {
        return 301 https://google.com;
    }

    error_page 404 /404.html;
    location = /404.html {
        root /var/www/html;
        internal;
    }
}" > /etc/nginx/nginx.conf
nginx -s reload

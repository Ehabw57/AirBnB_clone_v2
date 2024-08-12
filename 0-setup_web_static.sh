#!/usr/bin/env bash
# this is a bashscript to set up webservers for the deployment of web_static

# install nginx
sudo apt-get -y update
sudo apt-get -y install nginx
sudo service nginx start

# creating folders if it's doesn't already exists
sudo mkdir -p /data/web_static/{releases/test,shared}

# creating fake HTML file
echo "Hello Web" | sudo tee /data/web_static/releases/test/index.html

# creating new simbolic link to test folder
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# change ownership of folder /data/
sudo chown -hR ubuntu:ubuntu /data/


# Update the Nginx configuration to serve the content
configs="server {
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
}
"

sudo echo "$configs" | sudo tee /etc/nginx/sites-available/default

# restarting nginx
sudo service nginx restart

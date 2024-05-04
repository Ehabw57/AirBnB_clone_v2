#!/usr/bin/env bash
# Sets up  my web server for deployment
# Install Nginx
apt-get update -y
apt-get install nginx -y

# Some path variables
test_path=/data/web_static/releases/test
shared_path=/data/web_static/shared

# Create the folders if it does'nt exists
if [ ! -d $test_path ]; then
    mkdir -p $test_path
fi
if [ ! -d $shared_path ]; then
    mkdir -p $shared_path
fi

# Create a fake HTML file
echo "Hello Web" > $test_path/index.html

# Create a forces symbolic link 
ln -sf $test_path /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
chown -R ubuntu:ubuntu /data

# Update and restart Nginx
echo "events {
}
http {
        server {
                listen 80;
                location /hbnb_static {
                        alias /data/web_static/current/;
                }
        }
}" > /etc/nginx/nginx.conf
nginx -s reload

#!/usr/bin/env bash
# preparing my web servers

if [ ! -x usr/sbin/nginx ]; then
    sudo apt-get update -y -qq && sudo apt-get install -y nginx
fi

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

fake_html=\
"
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
ubuntu@89-web-01:~/$ curl localhost/hbnb_static/index.html
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
"

sudo chown -R ubuntu:ubuntu /data/
sudo chown -R ubuntu:ubuntu /data/web_static/

echo "$fake_html" > /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo sed -i '51i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

sudo service nginx restart

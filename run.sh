#!/bin/sh

# Change it to your repo directory
cd ~/ZeroNet_WordPress2ZeroBlog/

# Read config from config.ini
znpath=$(awk -F "=" '/zeronet_project_path/ {print $2}' config.ini)
znaddr=$(awk -F "=" '/zeronet_site_address/ {print $2}' config.ini)
znkey=$(awk -F "=" '/zeronet_site_privatekey/ {print $2}' config.ini)


python3 sync.py

# [TODO] Don't publish zeroblog if no new post found. 
if [ $? -eq 0 ]; then
    python $znpath/zeronet.py siteSign --publish $znaddr $znkey
    echo "updated to ZeroBlog."
else
    echo "No new post yet, exit."
fi

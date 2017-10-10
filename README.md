# BacoPy

## Installation (Raspbian) - Note: Restart required after installing libssl-dev

```
sudo apt-get update
sudo apt-get install build-essential tk-dev
sudo apt-get install libncurses5-dev libncursesw5-dev libreadline6-dev
sudo apt-get install libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev
sudo apt-get install libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev
wget https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tar.xz
sudo tar -xvf Python-3.5.2.tar.xz
cd Python-3.5.2
sudo ./configure
sudo make -j 4
sudo make altinstall -j 4
sudo apt install git
git clone https://github.com/MrHDR/BacoPy.git
sudo python3.5 -m pip install praw
sudo python3.5 -m pip install -U discord.py
sudo python3.5 -m pip install psutil
```

## Requirements
Python 3.5

Praw

Discord.py

psutil

A Discord Developer Account

A Reddit Developer Account

## Planned Features

Permission system

User Blacklist

Dynamic Command List

Allow Searching in addition to having it grab a random image/gif

Reverse Image Searches

## Known issues
No warning for missing permissions (when removing messages that start with the set prefix and using clear)

Bot can currently talk in all channels, to fix this simply make a custom role for the bot, and prevent it from being able to read messages in all channels except for target channel.

# BacoPy

## Installation (Raspbian)

```
sudo apt install libssl-dev
wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0a1.tar.xz
sudo tar -xvf Python-3.7.0a1.tar.xz
cd Python-3.7.0a1
sudo ./configure
sudo make
sudo make altinstall
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

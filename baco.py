import discord
import asyncio
import sys
import os
import time
import datetime
import psutil
import json

print('Starting up...')
start_time = time.time()
time = time.time()
current_time = datetime.datetime.now().time()
current_time.isoformat()

if os.path.isfile('config.json') == False:
    sys.exit('Fatal Error: config.json is not present.\nIf you didn\'t already, rename config.example.json to config.json and try again.')
else:
    print('config.json present, continuing...')
if os.path.isfile('commands.json') == False:
    sys.exit('Fatal Error: commands.json is not present.\nIf you didn\'t already, rename config.example.json to config.json and try again.')
else:
    print('commands.json present, continuing...')

with open('config.json', 'r', encoding='utf-8') as config_file:
    config = config_file.read()
    config = json.loads(config)
    print('Loaded configuration.')
with open('commands.json', 'r', encoding='utf-8') as commands_file:
    commands = commands_file.read()
    commands = json.loads(commands)
    print('Loaded commands.')

token = (config['Token'])
if token == '':
    sys.exit('Token not provided, please open config.json and place your token.')
pfx = (config['Prefix'])

client = discord.Client()

# Commands
cmd_pcstats = (commands['cmd_pcstats'])
cmd_help = (commands['cmd_help'])
cmd_hentai = (commands['cmd_hentai'])
cmd_r34 = (commands['cmd_r34'])
cmd_nsfw = (commands['cmd_nsfw'])

# I love spaghetti!

@client.event
async def on_ready():
    print('\nLogin Details:')
    print('---------------------')
    print('Logged in as:')
    print(client.user.name)
    print('Bot User ID:')
    print(client.user.id)
    print('---------------------\n')
    print('---------------------------------------')
    print('Running discord.py version ' + discord.__version__)
    print('---------------------------------------\n')
    print('STATUS: Finished Loading!')
    print('-------------------------\n')
    print('-----------------------------------------')
    print('Author: HDR')
    print('Version: Dev 0.1')
    print('Build Date: 31 March 2017.')
    print('-----------------------------------------\n')

@client.event
async def on_message(message):
    initiator_data = ('by ' + str(message.author) + ' ,UserID: ' + message.author.id + '. Server: ' + message.server.id)
    client.change_status(game=None)
    if message.content.startswith(pfx + cmd_help):
        cmd_name = 'Help'
        await client.send_message(message.channel, '" --pcstats "\n" --help "\n" --hentai "\n" --r34 "\n" --nsfw "')
        print('CMD [' + pfx + cmd_name + '] > ' + initiator_data)
    elif message.content.startswith(pfx + cmd_hentai):
        await client.send_message(message.channel, 'To be Added')
        cmd_name = 'Hentai'
        print('CMD [' + pfx + cmd_name + '] > ' + initiator_data)
    elif message.content.startswith(pfx + cmd_pcstats):
        cmd_name = 'PC Stats'
        await client.send_message(message.channel,
                                  '**MEM Stats:** \n' + str(psutil.virtual_memory()) + '\n\n **CPU Stats:** \n' + str(
                                      psutil.cpu_stats()) + '\n\n **CPU Percent:** \n' + str(
                                      psutil.cpu_percent(percpu=True)))
        print('CMD [' + pfx + cmd_name + '] > ' + initiator_data)
    elif message.content.startswith('<@' + client.user.id + '>'):
        cmd_name = 'BOT Mentioned'
        await client.send_message(message.channel, 'What do you want slut?')
        print('CMD [' + pfx + cmd_name + '] > ' + initiator_data)
    elif message.content.startswith(pfx + cmd_r34):
        cmd_name = 'r34'
        await client.send_message(message.channel, 'To be Added')
    elif message.content.startswith(pfx + cmd_nsfw):
        cmd_name = 'nsfw'
        await client.send_message(message.channel, 'To be Added')
client.run(token)
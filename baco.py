import discord
import asyncio
import sys
import os
import time
import datetime
import psutil
import json
import praw

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

rclientid = (config['reddit_client_id'])
if rclientid == '':
    sys.exit('Reddit Client ID not provided, please edit config.json.')
rclientsecret = (config['reddit_client_secret'])
if rclientsecret == '':
    sys.exit('Reddit Client Secret not provided, please edit config.json.')
rpassword = (config['reddit_password'])
if rpassword == '':
    sys.exit('Reddit Password not provided, please edit config.json.')
rusername = (config['reddit_username'])
if rusername == '':
    sys.exit('Reddit Username not provided, please edit config.json')
ruseragent = (config['reddit_useragent'])
if ruseragent == '':
    sys.exit('Reddit UserAgent not provided, please edit config.json')

r = praw.Reddit(client_id=rclientid,
                client_secret=rclientsecret,
                password=rpassword,
                user_agent=ruseragent,
                username=rusername)
				
client = discord.Client()

# Commands
cmd_stats = (commands['cmd_stats'])
cmd_help = (commands['cmd_help'])
cmd_hentai = (commands['cmd_hentai'])
cmd_r34 = (commands['cmd_r34'])
cmd_nsfw = (commands['cmd_nsfw'])
cmd_gif = (commands['cmd_gif'])

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
    print('Version: Dev 0.7')
    print('Build Date: 1 April 2017.')
    print('-----------------------------------------\n')

@client.event
async def on_message(message):
    initiator_data = ('by ' + str(message.author) + ' ,UserID: ' + message.author.id + '. Server: ' + message.server.id)
    client.change_status(game=None)
    if message.content.startswith(pfx + cmd_help):
        cmd_name = 'Help'
        await client.send_message(message.channel, '**--stats**\n**--help**\n**--hentai**\n**--r34**\n**--nsfw**\n**--gif**')
        print('CMD [' + pfx + cmd_name + '] > ' + initiator_data)
    elif message.content.startswith(pfx + cmd_hentai):
        hen = r.subreddit('hentai')
        posts = hen.random()
        await client.send_message(message.channel, posts.url)
        cmd_name = 'Hentai'
        print('CMD [' + pfx + cmd_name + '] > ' + initiator_data)
    elif message.content.startswith(pfx + cmd_stats):
        cmd_name = 'Stats'
        def getCPUtemp():
            res = os.popen('vcgencmd measure_temp').readline()
            return(res.replace("temp=","").replace("'C\n",""))
        CPU_temp = str(getCPUtemp())

        def getCPUuse():
            return(str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip(\
        )))
        CPU_load = str(getCPUuse())

        RAM_usage = str(psutil.virtual_memory().percent)
        await client.send_message(message.channel,
                                  '**CPU Load:** \n' + CPU_load + '% \n' + '**CPU Temp:** \n' + CPU_temp + '°C \n' + '***RAM Usage:***\n' + RAM_usage + '%')
        print('CMD [' + pfx + cmd_name + '] > ' + initiator_data)
    elif message.content.startswith('<@' + client.user.id + '>'):
        cmd_name = 'BOT Mentioned'
        await client.send_message(message.channel, 'What do you want slut?')
        print('CMD [' + pfx + cmd_name + '] > ' + initiator_data)
    elif message.content.startswith(pfx + cmd_r34):
        r34 = r.subreddit('rule34')
        posts = r34.random()
        await client.send_message(message.channel, posts.url)
        cmd_name = 'r34'
    elif message.content.startswith(pfx + cmd_nsfw):
        nsfw = r.subreddit('nsfw')
        posts = nsfw.random()
        await client.send_message(message.channel, posts.url)
        cmd_name = 'nsfw'
    elif message.content.startswith(pfx + cmd_gif):
        gif = r.subreddit('gifs')
        posts = gif.random()
        await client.send_message(message.channel, posts.url)
        cmd_name = 'gif'
client.run(token)
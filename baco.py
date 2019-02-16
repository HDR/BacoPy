import discord
import sys
import os
import time
import psutil
import json
import praw

print('Starting up...')
start_time = time.time()

if os.path.isfile('config.json') == False:
    sys.exit('Fatal Error: config.json is not present.')
else:
    print('config.json present, continuing...')
if os.path.isfile('commands.json') == False:
    sys.exit('Fatal Error: commands.json is not present.')
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
ruseragent = (config['reddit_useragent'])
if ruseragent == '':
    sys.exit('Reddit UserAgent not provided, please edit config.json')

r = praw.Reddit(client_id=rclientid,
                client_secret=rclientsecret,
                user_agent=ruseragent)
client = discord.Client()

# Commands
cmd_stats = (commands['cmd_stats'])
cmd_help = (commands['cmd_help'])
cmd_hentai = (commands['cmd_hentai'])
cmd_r34 = (commands['cmd_r34'])
cmd_nsfw = (commands['cmd_nsfw'])
cmd_gif = (commands['cmd_gif'])
cmd_clear = (commands['cmd_clear'])


class BacoPy(discord.Client):
    def __init__(self):
        super().__init__()

    async def on_ready(self):
        print('---------------------')
        print('Logged in as:')
        print(self.user.name)
        print('Bot User ID:')
        print(self.user.id)
        print('---------------------\n')
        print('---------------------------------------')
        print('Running discord.py version ' + discord.__version__)
        print('---------------------------------------\n')
        print('-------------------------')
        print('STATUS: Finished Loading!')
        print('-------------------------\n')
        print('-----------------------------------------')
        print('Author: HDR')
        print('Version: 1.1')
        print('Build Date: 16 February 2019')
        print('-----------------------------------------\n')

    async def on_message(self, message):
        initiator_data = ('by ' + str(message.author) + ' ,UserID: ' + message.author.id + '. Server: ' + message.server.id)
        self.change_status(game=None)
        if message.content.startswith(pfx + cmd_help):
            cmd_name = 'Help'
            await self.send_message(message.channel, '**--stats**\n**--help**\n**--hentai**\n**--r34**\n**--nsfw**\n**--gif**')
            print('CMD [' + pfx + cmd_name + '] > ' + initiator_data)
        elif message.content.startswith(pfx + cmd_hentai):
            hen = r.subreddit('hentai')
            posts = hen.random()
            await self.send_message(message.channel, posts.url)
            cmd_name = 'Hentai'
            print('CMD [' + pfx + cmd_name + '] > ' + initiator_data)
        elif message.content.startswith(pfx + cmd_stats):
            cmd_name = 'Stats'
            temps = psutil.sensors_temperatures()
            core0 = str("Core 0: " + "+" + str(temps)[46:50] + "C\n")
            core1 = str("Core 1: " + "+" + str(temps)[112:116] + "C\n")
            core2 = str("Core 2: " + "+" + str(temps)[178:182] + "C\n")
            core3 = str("Core 3: " + "+" + str(temps)[244:248] + "C")
            CPU_temp = core0 + core1 + core2 + core3
            def cpu_percentage():
                CPU_Pct=str(round(float(os.popen('''grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage }' ''').readline()),2))
                return(CPU_Pct)
            CPU_load = str(cpu_percentage())
            RAM_usage = str(psutil.virtual_memory().percent)
            getruntime = round(time.time() - start_time, 10) / (60)
            runtimeint = int(getruntime)
            runtime = str(runtimeint)
            await self.send_message(message.channel,
                                      '**Runtime:**\n' + runtime + ' Minutes \n**CPU Load:** \n' + CPU_load + '% \n' + '**CPU Temp:** \n' + CPU_temp + '\n' + '**RAM Usage:**\n' + RAM_usage + '%')
            print('CMD [' + pfx + cmd_name + '] > ' + initiator_data)
        elif message.content.startswith('<@' + self.user.id + '>'):
            cmd_name = 'BOT Mentioned'
            await self.send_message(message.channel, 'What?')
            print('CMD [' + pfx + cmd_name + '] > ' + initiator_data)
        elif message.content.startswith(pfx + cmd_r34):
            r34 = r.subreddit('rule34')
            posts = r34.random()
            await self.send_message(message.channel, posts.url)
            cmd_name = 'r34'
            print('CMD [' + pfx + cmd_name + '] > ' + initiator_data)
        elif message.content.startswith(pfx + cmd_nsfw):
            nsfw = r.subreddit('nsfw')
            posts = nsfw.random()
            await self.send_message(message.channel, posts.url)
            cmd_name = 'nsfw'
            print('CMD [' + pfx + cmd_name + '] > ' + initiator_data)
        elif message.content.startswith(pfx + cmd_gif):
            gif = r.subreddit('nsfw_gif+HENTAI_GIF').random()
            #gif = r.subreddit('nsfw_gif')
            await self.send_message(message.channel, gif.url)
            cmd_name = 'gif'
            print('CMD [' + pfx + cmd_name + '] > ' + initiator_data)
        elif message.content.startswith(pfx + cmd_clear):
            def is_me(m):
                return m.author == self.user
            deleted = await self.purge_from(message.channel, limit=100, check=is_me)
            await self.send_message(message.channel, 'Deleted {} message(s)'.format(len(deleted)))
            cmd_name = 'clear'
            print('CMD [' + pfx + cmd_name + '] > ' + initiator_data)
        elif message.content.startswith('debugtest'):
            getruntime = round(time.time() - start_time, 10) / (60)
            runtime = int(getruntime)
            await self.send_message(message.channel, runtime)
            await self.send_message(message.channel, commands)
        if message.content.startswith(pfx):
            await self.delete_message(message)
bot = BacoPy()
bot.run(token)

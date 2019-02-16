from discord.ext import commands
import psutil
import os
import time

start_time = time.time()

class Stats(object):
	"""Reports server stats."""
	
	def __init__(self, bot):
		self.bot = bot
		
	@commands.command()
	async def stats(self, ctx):
		"""Reports server stats."""
		
		await ctx.channel.trigger_typing()
		
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
		await ctx.send('**Runtime:** ' + runtime + ' Minutes \n**CPU Load:** ' + CPU_load + '% \n' + '**CPU Temps:** \n' + CPU_temp + '\n' + '**RAM Usage:** ' + RAM_usage + '%')
		
def setup(bot):
	bot.add_cog(Stats(bot))
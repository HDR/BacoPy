from discord.ext import commands
import praw
from config import get_section
from collections import deque

r = praw.Reddit(client_id=get_section("reddit").get("client_id"), client_secret=get_section("reddit").get("client_secret"), user_agent=get_section("reddit").get("useragent"))

class Reddit(object):
	"""Nsfw commands."""
	
	def __init__(self, bot):
		self.bot = bot
		
	@commands.command()
	async def nsfw(self, ctx):
		"""Grabs a random popular /r/nsfw post"""
		await ctx.channel.trigger_typing()
		nsfw = r.subreddit('nsfw').random()
		await ctx.message.delete()
		await ctx.send(ctx.message.author.mention + " " + nsfw.url)
	@commands.command()
	async def gif(self, ctx):
		"""Grabs a random popular /r/nsfw_gif or /r/HENTAI_GIF post"""
		await ctx.channel.trigger_typing()
		gif = r.subreddit('nsfw_gif+HENTAI_GIF').random()
		await ctx.message.delete()
		await ctx.send(ctx.message.author.mention + " " + gif.url)
	@commands.command()
	async def r34(self, ctx):
		"""Grabs a random popular /r/rule34 post"""
		await ctx.channel.trigger_typing()
		r34 = r.subreddit('rule34').random()
		await ctx.message.delete()
		await ctx.send(ctx.message.author.mention + " " + r34.url)
	@commands.command()
	async def hentai(self, ctx):
		"""Grabs a random popular /r/hentai post"""
		await ctx.channel.trigger_typing()
		hentai = r.subreddit('hentai').random()
		await ctx.message.delete()
		await ctx.send(ctx.message.author.mention + " " + hentai.url)
	@commands.command()
	async def surprise(self, ctx):
		"""You're surprised by this command"""
		await ctx.channel.trigger_typing()
		surprise = r.subreddit('traphentai+delicioustraps+gonewild+nsfw+nsfw_gif+HENTAI_GIF+legalteens+ass+rule34+futanari+hugeboobs+funsized+nsfwcosplay+pornin15seconds+realgirls+asiansgonewild+biggerthanyouthought+petitegonewild+bustypetite+holdthemoan+trashyboners+hentai+ass+watchitfortheplot+milf+adorableporn+onoff+tittydrop+amateur+pawg+gonewildcurvy+happyembarrassedgirls+massivecock+cumsluts+girlsfinishingthejob+asstastic+curvy+gonewild30plus+ecchi+thick+anal+freeuse+bigboobsgw+blowjobs+workgonewild+festivalsluts+juicyasians+yiff+palegirls+stacked+altgonewild+tightdresses+nsfwhardcore+overwatch_porn').random()
		await ctx.message.delete()
		await ctx.send(ctx.message.author.mention + " " + surprise.url)
		
def setup(bot):
	bot.add_cog(Reddit(bot))
from discord.ext import commands
import praw
from config import get_section
from collections import deque

r = praw.Reddit(client_id=get_section("reddit").get("client_id"), client_secret=get_section("reddit").get("client_secret"), user_agent=get_section("reddit").get("useragent"))

class Reddit(object):
	"""Nsfw commands."""
	
	def __init__(self, bot):
		self.bot = bot
		self.last_images = deque(maxlen=10)
		
	@commands.command()
	async def nsfw(self, ctx):
		"""Grabs a random popular /r/nsfw post"""
		await ctx.channel.trigger_typing()
		nsfw = r.subreddit('nsfw').random()
		await ctx.send(nsfw.url)
	@commands.command()
	async def gif(self, ctx):
		"""Grabs a random popular /r/nsfw_gif or /r/HENTAI_GIF post"""
		await ctx.channel.trigger_typing()
		gif = r.subreddit('nsfw_gif+HENTAI_GIF').random()
		await ctx.send(gif.url)
	@commands.command()
	async def r34(self, ctx):
		"""Grabs a random popular /r/rule34 post"""
		await ctx.channel.trigger_typing()
		r34 = r.subreddit('rule34').random()
		await ctx.send(gif.url)
	@commands.command()
	async def hentai(self, ctx):
		"""Grabs a random popular /r/hentai post"""
		await ctx.channel.trigger_typing()
		hentai = r.subreddit('hentai').random()
		await ctx.send(hentai.url)

def setup(bot):
	bot.add_cog(Reddit(bot))
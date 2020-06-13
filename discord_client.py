from discord.ext import commands
from config import config

client = commands.Bot(command_prefix=config['prefix'])

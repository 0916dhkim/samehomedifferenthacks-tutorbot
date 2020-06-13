from discord_client import client
from data import mentorAdapter
from discord.ext.commands import Context


# Command to mark the author as busy.
@client.command()
async def busy(ctx: Context):
    mentorAdapter.set_busy(ctx.author, True)
    await ctx.message.channel.send("You are busy!")

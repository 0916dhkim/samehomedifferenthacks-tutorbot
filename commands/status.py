from discord_client import client
from data import mentorAdapter
from discord.ext.commands import Context


# Command to check the author's busy status.
@client.command(
    help="Print your status."
)
async def status(ctx: Context):
    is_busy = mentorAdapter.check_busy(ctx.author)
    if is_busy:
        await ctx.message.channel.send("You are busy!")
    else:
        await ctx.message.channel.send("You are free!")

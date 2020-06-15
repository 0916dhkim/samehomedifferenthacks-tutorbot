from discord_client import client
from data import mentorAdapter
from discord.ext.commands import Context


# Command to mark the author as free (not busy).
@client.command(
    help=(
        "Receive SOS signals.\n"
        "You will receive SOS signals "
        "only when you are free."
    )
)
async def free(ctx: Context):
    mentorAdapter.set_busy(ctx.author, False)
    await ctx.message.channel.send("You are free!")

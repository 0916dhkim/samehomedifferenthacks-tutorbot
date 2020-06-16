from discord_client import client
from data import mentorAdapter
from discord.ext.commands import Context


# Command to check the author's busy status.
@client.command(help="Print your status.")
async def status(ctx: Context):
    message = ""
    is_busy = mentorAdapter.check_busy(ctx.author)
    role_names = map(
        lambda r: r.name,
        filter(lambda r: r != ctx.guild.default_role, ctx.author.roles)
    )
    if is_busy:
        message += "(busy) You are not available to answer questions."
    else:
        message += "(free) You are open for questions."
    message += "\nYour roles: "
    message += f"{', '.join(role_names)}"
    await ctx.message.channel.send(message)

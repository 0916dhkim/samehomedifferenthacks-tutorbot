from discord_client import client
from discord.ext.commands import Context
from discord import utils


# Command to add roles to the author.
@client.command(
    help="Remove roles.",
    usage="[ROLE]..."
)
async def unregister(ctx: Context, *args: str):
    for role_name in args:
        role = utils.get(ctx.author.guild.roles, name=role_name)
        if role is not None:
            await ctx.author.remove_roles(role)
    await ctx.message.channel.send("You have been successful unregistered.")

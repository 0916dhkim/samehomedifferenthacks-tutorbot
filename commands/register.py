from discord_client import client
from discord.ext.commands import Context
from discord import utils


# Command to add roles to the author.
@client.command(
    help=(
        "Add your technical stack.\n"
        "Identify yourself as a mentor "
        "by providing your technical stack. "
        "This command will assign discord server "
        "roles to you."
    ),
    usage="[ROLE]..."
)
async def register(ctx: Context, *args: str):
    for role_name in args:
        role = utils.get(ctx.author.guild.roles, name=role_name)
        if role is not None:
            await ctx.author.add_roles(role)
    await ctx.message.channel.send("Registration successful.")

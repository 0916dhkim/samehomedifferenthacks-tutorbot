from discord_client import client
from discord.ext.commands import Context
from discord import utils
from typing import List


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
    added_role_names: List[str] = []
    for role_name in args:
        role = utils.get(ctx.author.guild.roles, name=role_name)
        if role is not None:
            added_role_names.append(role_name)
            await ctx.author.add_roles(role)
    message = (
        "Registration successful.\n"
        f"Added roles: {','.join(added_role_names)}"
    )
    await ctx.message.channel.send(message)

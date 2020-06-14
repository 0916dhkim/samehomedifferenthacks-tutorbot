from discord_client import client
from discord.ext.commands import Context
from discord import Role, Member, utils
from data import mentorAdapter
from typing import List


# Return true if target member contains all required roles
def hasAllRoles(member: Member, *roles: Role) -> bool:
    required = set(roles)
    for r in member.roles:
        required.discard(r)
    return len(required) == 0


# Filter Members by required roles.
async def filterMembersByRequirements(
    members: List[Member], *roles: Role
) -> List[Member]:
    return list(filter(lambda m: hasAllRoles(m, *roles), members))


# Command to notify mentors for help.
@client.command()
async def sos(ctx: Context, *args: str):
    free_members = list(
        set(ctx.author.guild.members) - mentorAdapter._busy_members
    )
    roles: List[Role] = []
    for role_name in args:
        role = utils.get(ctx.author.guild.roles, name=role_name)
        if role is not None:
            roles.append(role)

    mentors = await filterMembersByRequirements(free_members, *roles)
    message = (
        f"{ctx.author.mention} needs your HELP!\n"
        f"Available Mentors: {''.join(map(lambda m: m.mention, mentors))}"
    )
    await ctx.message.channel.send(message)

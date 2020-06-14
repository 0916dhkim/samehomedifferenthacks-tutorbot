from discord_client import client
from discord.ext.commands import Context
from discord import Role, Member
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
    return list(
        filter(
            lambda m: hasAllRoles(m, *roles),
            members
        )
    )


# Command to notify mentors for help.
@client.command()
async def sos(ctx: Context):

    roles = ctx.author.guild.roles
    await ctx.message.channel.send("roles: ")
    for r in roles:
        await ctx.message.channel.send(r)

    members = ctx.author.guild.members
    await ctx.message.channel.send("members: ")
    for m in members:
        await ctx.message.channel.send(m.name)

    await ctx.message.channel.send("busy members: ")
    busyMembers = mentorAdapter._busy_members
    for b in busyMembers:
        await ctx.message.channel.send(b)

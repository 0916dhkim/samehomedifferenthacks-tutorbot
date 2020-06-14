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
async def filterMembersByRequirements(members: List[Member], *roles: Role) -> List[Member]:
    return list(
        filter(
            lambda m: hasAllRoles(m, *roles),
            members
        )
    )


# Command to notify mentors for help.
@client.command()
async def sos(ctx: Context, *args: str):
    free_members = set(ctx.author.guild.members) - mentorAdapter._busy_members
    list(free_members)
    print(free_members)

    # always causes runtime warning on first call, then doesnt
    x = filterMembersByRequirements(free_members, args)
    print(x)

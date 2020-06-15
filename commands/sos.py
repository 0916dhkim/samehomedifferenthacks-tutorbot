from discord_client import client
from discord.ext.commands import Context
from discord import Role, Member, utils
from data import mentorAdapter
from typing import List

# Token for separating roles and question
SEPARATOR_SET = set([":", "--"])


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
@client.command(
    help=(
        "Get help for your question.\n"
        "Notify mentors who have specified roles "
        "about your question."
    ),
    usage="[ROLE]... [-- [QUESTION]]"
)
async def sos(ctx: Context, *args: str):
    # Separate args into role names and question.
    role_names: List[str] = []
    question_words: List[str] = []
    after_separator: bool = False
    for arg in args:
        if arg in SEPARATOR_SET:
            after_separator = True
            continue
        if after_separator:
            question_words.append(arg)
        else:
            role_names.append(arg)

    # Calculate free members.
    free_members = list(
        set(ctx.author.guild.members) - mentorAdapter._busy_members
    )

    # Filter matching mentors.
    roles: List[Role] = []
    for role_name in role_names:
        role = utils.get(ctx.author.guild.roles, name=role_name)
        if role is not None:
            roles.append(role)

    mentors = await filterMembersByRequirements(free_members, *roles)

    # Send message.
    message = (
        f"{ctx.author.mention} needs your HELP!\n"
        f"Question: {' '.join(question_words)}\n"
        f"Available Mentors: {' '.join(map(lambda m: m.mention, mentors))}"
    )
    await ctx.message.channel.send(message)

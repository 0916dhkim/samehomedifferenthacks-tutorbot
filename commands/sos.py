from discord_client import client
from discord.ext.commands import Context
from data import mentorAdapter

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

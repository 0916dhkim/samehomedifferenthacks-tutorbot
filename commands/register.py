from discord_client import client
from discord.ext.commands import Context
from discord import utils


def create_mentor_card(db_data):
    card_mentor = (
        "<strong>{} {}</strong>\n"
        + "Primary language: <strong>{}</strong> "
        + "Additional languages: <strong>{}</strong> "
        + 'Discord link: <a href="{}">{}</a>'
    ).format(
        db_data[0], db_data[1], db_data[2], db_data[3], db_data[4], db_data[4]
    )
    return card_mentor


def question_card(quest_data):
    question = """
Hello! Me {} name is. \n
I apologize for distracting you.
but if there is free time please help\n
In general, the essence of the problem: {} \n
Brief Description of the Question: {} \n
Additional Information!
The main language of development: {}
    """.format(
        quest_data["name"],
        quest_data["title"],
        quest_data["question"],
        quest_data["lang"],
    )
    return question


def mentors_card(obj):
    card = ""
    for i in range(len(obj)):
        card += (
            "▫️ {} {} \n Primary language: {}\n "
            + "Additional languages: {}\n Link: {}\n\n"
        ).format(obj[i][0], obj[i][1], obj[i][2], obj[i][3], obj[i][4])
    return card


@client.command()
async def register(ctx: Context, *args: str):
    for role_name in args:
        role = utils.get(ctx.author.guild.roles, name=role_name)
        if role is not None:
            await ctx.author.add_roles(role)
    await ctx.message.channel.send("Registration successful.")

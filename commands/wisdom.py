from discord_client import client
from discord.ext.commands import Context
from discord import utils
import random


# Command to add roles to the author.
@client.command(
    help="Get your daily dose of wisdom."
)
async def wisdom(ctx):
    responses = [
        'Concentrate on what I know is true while I wait for the mud to settle and the water to become clear.',
        'Train yourself to let go of everything you fear to lose.',
        'You can only find what you bring in.',
        'Do or do not. There is no try.',
        'The more we learn, the more we discover how much we do not know.'
        ]

    await ctx.message.channel.send(random.choice(responses))

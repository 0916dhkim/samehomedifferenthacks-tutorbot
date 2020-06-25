# This module is for handling discord events.

import logging
import asyncio
from config import config
from discord_client import client
from discord import TextChannel
from commands import add_commands


def main():
    logging.basicConfig(level=logging.INFO)
    token = config["token"]
    add_commands()
    client.run(token)


# Send greetings to all discord servers
async def send_greetings():
    tasks = []
    message = "Tutorbot is updated and now online."
    for guild in client.guilds:
        if len(guild.text_channels) != 0:
            # Find default text channel.
            default_channel: TextChannel = guild.text_channels[0]
            tasks.append(
                default_channel.send(message)
            )
    await asyncio.wait(tasks)


@client.event
async def on_ready():
    print("Ready to start mentoring")
    await send_greetings()


@client.event
async def on_message(message):
    if message.author.bot:
        return
    ctx = await client.get_context(message)
    if ctx.valid:
        await client.process_commands(message)

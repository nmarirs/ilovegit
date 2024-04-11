import discord
import os
from dotenv import load_dotenv
import random

def random_joke():
    with open("./jokes.txt", "r") as f:
        jokes = f.readlines()
        joke = random.choice(jokes)
        return joke

class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")

    async def on_message(self, message):
        print(f"Message from {message.author}: {message.content}")
        if "$joke" in message.content:
            await message.channel.send(random_joke())
        elif "git" in message.content and not message.author.bot:
            await message.channel.send("Excuse me, would you like to hear about our lord and savior Git, the free and open source version control system? https://git-scm.com/")
        elif "mercurial" in message.content:
            await message.channel.send("Ewwwwwww blasphemy. Imagine being so dense")
        elif "subversion" in message.content or "svn" in message.content:
            await message.channel.send("Ratio this man. svn more like I'd rather jump off a cliff")



intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

load_dotenv()
TOKEN = os.getenv("TOKEN")
client.run(TOKEN)

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
        if not message.author.bot:
            if "$joke" in message.content:
                await message.channel.send(random_joke())
            elif "git" in message.content:
                await message.channel.send("Excuse me, would you like to hear about our lord and savior Git, the free and open source version control system? https://git-scm.com/")
            elif "mercurial" in message.content or "hg" in message.content:
                await message.channel.send("Ewwwwwww blasphemy. Imagine being so dense")
            elif "subversion" in message.content or "svn" in message.content:
                await message.channel.send("Ratio this man. svn more like I'd rather jump off a cliff")
            elif "don't be this guy" in message.content or "github" in message.content.lower():
                await message.channel.send("""I am new to GitHub and I have lots to say

    I DONT GIVE A FUCK ABOUT THE FUCKING CODE! i just want to download this stupid fucking application and use it https://github.com/sherlock-project/sherlock#installation

    WHY IS THERE CODE??? MAKE A FUCKING .EXE FILE AND GIVE IT TO ME. these dumbfucks think that everyone is a developer and understands code. well i am not and i don't understand it. I only know to download and install applications. SO WHY THE FUCK IS THERE CODE? make an EXE file and give it to me. STUPID FUCKING SMELLY NERDS
    """);



intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

load_dotenv()
TOKEN = os.getenv("TOKEN")
client.run(TOKEN)

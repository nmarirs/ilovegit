import discord
import os
from dotenv import load_dotenv

class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")

    async def on_message(self, message):
        print(f"Message from {message.author}: {message.content}")
        if "git" in message.content and not message.author.bot:
            await message.channel.send("Excuse me, would you like to hear about our lord and savior Git, the free and open source version control system? https://git-scm.com/")


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

load_dotenv()
TOKEN = os.getenv("TOKEN")
client.run(TOKEN)

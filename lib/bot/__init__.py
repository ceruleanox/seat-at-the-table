from datetime import datetime

from discord import Intents
from discord import Embed, File
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext.commands import Bot as BotBase

PREFIX = "+"
OWNER_IDS = [728827786051190865]

class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        self.scheduler = AsyncIOScheduler()


        super().__init__(
            command_prefix=PREFIX, 
            owner_ids=OWNER_IDS,
            intents=Intents.all(),
        )

    def run(self, version):
        self.VERSION = version
                
        with open("./lib/bot/token.0", "r", encoding="utf-8") as tf:
            self.TOKEN = tf.read()
            
        print("running bot...")
        super().run(self.TOKEN, reconnect=True)

    async def on_connect(self):
        print("bot connected")

    async def on_disconnect(self):
        print("bot disconnected")

    async def on_ready(self):
        if not self.ready:
            self.ready = True
            self.guild = self.get_guild(779824317407559711)
            print("bot ready")

            channel = self.get_channel(779887490814443560)
            # await channel.send("It's a good day to help hackathon life go right!")

            embed = Embed(
                title="It's a good day to help hackathon life go right!", 
                description="Hello world! So wonderful to have you join me and other hackathoners today. My name is SATT Bot - that's short for Seat at the Table. I'll be the first to bring you a chair because I believe we all deserve a seat at the table.",
                colour=0xFF7F50,
                timestamp=datetime.utcnow()
            )

            embed.set_author(name="Seat at the Table", icon_url=self.guild.icon_url) 
            embed.set_footer(text="You have perspectives and visions to offer the world of technology. So go ahead, take a seat at the table. We welcome you!")
            embed.set_thumbnail(url=self.guild.icon_url)
            embed.set_image(url=self.guild.icon_url)
            await channel.send(embed=embed)

            # await channel.send(file=File("[path]"))

        else:
            print("bot reconnected")

    async def on_message(self, message):
        pass

bot = Bot()
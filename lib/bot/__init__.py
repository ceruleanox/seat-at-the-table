from datetime import datetime
from glob import glob
from asyncio import sleep

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from discord import Intents
from discord import Embed, File
from discord.ext.commands import Bot as BotBase
from discord.ext.commands import CommandNotFound

from ..db import db

PREFIX = "+"
OWNER_IDS = [728827786051190865]
COGS = [path.split("\\")[-1][:-3] for path in glob("./lib/cogs/*.py")]

class Ready(object):
    def __init__(self):
        for cog in COGS:
            setattr(self, cog, False)

    def ready_up(self,cog):
        setattr(self, cog, True)
        print(f" [cog] cog ready")

    def all_ready(self):
        return all([getattr(self, cog) for cog in COGS])
class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.cogs_ready = Ready()
        self.guild = None
        self.scheduler = AsyncIOScheduler()

        db.autosave(self.scheduler)

        super().__init__(
            command_prefix=PREFIX, 
            owner_ids=OWNER_IDS,
            intents=Intents.all(),
        )

    def setup(self):
        for cog in COGS:
            self.load_extension(f"lib.cogs.{cog}")
            print(f" {cog} cog loaded")
            
        print("setup complete")

    def run(self, version):
        self.VERSION = version

        print("running setup...")
        self.setup()

        with open("./lib/bot/token.0", "r", encoding="utf-8") as tf:
            self.TOKEN = tf.read()
            
        print("running bot...")
        super().run(self.TOKEN, reconnect=True)

    async def quick_checkin(self):
        channel = self.get_channel(779887490814443560)
        await self.stdout.send("Ping! Just checking in to see how you're doing - are you in the zone? If so, carry on! If you\'re feeling stuck, check in with your teammates or reach out a mentor. We've got you!")

    async def on_connect(self):
        print("bot connected")

    async def on_disconnect(self):
        print("bot disconnected")

    async def on_error(self, err, *args, **kwargs):
        if err == "on_command_error":
            await args[0].send("something went wrong")

        channel = self.get_channel(779887490814443560)
        await self.stdout.send("an error occurred")
        
        raise

    async def on_command_error(self, ctx, exc):
        if isinstance(exc, CommandNotFound):
            await ctx.send("wrong command sent")

        else:
            raise exc.original

    async def on_ready(self):
        if not self.ready:
            self.ready = True
            self.guild = self.get_guild(779824317407559711)
            self.stdout = self.get_channel(779887490814443560)
            self.scheduler.add_job(self.quick_checkin, CronTrigger(second="0")) # CronTrigger(day_of_week=... hour=/minute=/second=)
            self.scheduler.start()

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
            
            while not self.cogs_ready.all_ready():
                await sleep(0.5)

            self.ready = True
            print("bot ready")

            # await channel.send(file=File("[path]"))

        else:
            print("bot reconnected")

    async def on_message(self, message):
        pass

bot = Bot()
from discord.ext.commands import Cog

class test_cog(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
       if not self.bot.ready:
           self.bot.cogs_ready.ready_up("test_cog")
       # await self.bot.stdout.send("test cog ready")
       # print("test cog ready")

def setup(bot):
    bot.add_cog(test_cog(bot))
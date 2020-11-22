from discord.ext.commands import Cog

class test(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener
    async def on_ready(self):
        self.bot.stdout.send("test cog ready")
        print("test cog ready")

def setup(bot):
    bot.add_cog(test_cog(bot))
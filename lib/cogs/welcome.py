from discord import Forbidden
from discord.ext.commands import Cog
from discord.ext.commands import command

from ..db import db

class Welcome(Cog):
      def __init__(self, bot):
            self.bot = bot

	@Cog.listener()
  async def on_ready(self):
    if not self.bot.ready:
          self.bot.cogs_ready.ready_up("welcome")

def setup(bot):
  bot.add_cog(Welcome(bot))
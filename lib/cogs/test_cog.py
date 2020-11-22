import discord
import asyncio
from random import choice, randint
from typing import Optional

from aiohttp import request

from discord import Member, Embed
from discord.ext.commands import Cog
from discord.ext.commands import Bot
from discord.ext.commands import command

class test_cog(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("test_cog")


def setup(bot):
    bot.add_cog(test_cog(bot))

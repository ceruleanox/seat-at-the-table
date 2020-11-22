import discord

client = discord.Client()

'''
@client.event
async def on_ready():
    print("Bot is logged in")
'''

@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 780101938079203350:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        if payload.emoji.name == 'sunrise':
            role = discord.utils.get(guild.roles, name='peer mentor')
        elif payload.emoji.name== 'star'
            role = discord.utils.get(guild.roles, name='peer mentee')
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)
        
        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
                print("done")
            else:
                print("Member not found")
        else:
            print("role not found")

@client.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 780101938079203350:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        if payload.emoji.name == 'sunrise':
            role = discord.utils.get(guild.roles, name='peer mentor')
        elif payload.emoji.name== 'star'
            role = discord.utils.get(guild.roles, name='peer mentee')
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)
        
        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)
                print("done")
            else:
                print("Member not found")
        else:
            print("role not found")


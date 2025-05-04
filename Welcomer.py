import discord
from discord.ext import commands
import random
import asyncio
from datetime import datetime

#---------------------------------------
embed_color = 0xc80c0c # replace with your hashcode color for the embed
channel_id = None # replace with your welcome channel id
role_id = None # replace with the role id you want for autorole leave as "none" if you dont want it
#---------------------------------------

#-----------------DO NOT TOUCH-------------------- 
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.guilds = True
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_member_join(member: discord.Member):
    """Automatically assigns a role to new members and sends a welcome message."""
    if member.bot:
        return
    guild = member.guild

    welcome_channel = bot.get_channel(channel_id)
    role = guild.get_role(role_id)

    def get_ordinal(n):
        if 10 <= n % 100 <= 20:
            suffix = 'th'
        else:
            suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
        return f"{n}{suffix}"
    if role:
        try:
            await member.add_roles(role, reason="Auto role assignment on join")
        except discord.Forbidden:
            print("Missing permissions to assign role.")
        except Exception as e:
            print(f"An error occurred when assigning role: {e}")
    else:
        print("Role not found.")
    if welcome_channel:
        try:
            members_sorted = sorted(
                [m for m in guild.members if not m.bot],
                key=lambda m: m.joined_at
            )
            position = members_sorted.index(member) + 1
            ordinal_position = get_ordinal(position)

            welcome_embed = discord.Embed(
                title="Welcome to Assault Leaks!",
                description=f"Hello {member.mention}, you are the **{ordinal_position}** member!",
                color=embed_color,
                timestamp=datetime.utcnow()
            )
            await welcome_channel.send(embed=welcome_embed)
        except discord.Forbidden:
            print("Unable to send welcome message.")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Welcome channel not found.")

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"{bot.user.name} is online!")

#-----------------you can edit this-------------------- 
    statuses = ["Assault Leaks", ".gg/AssaultLeaks"]
#this with shuffle the bots status every 10 secs you can add more but make sure to keep the last one without a ","
    #-----------------DO NOT TOUCH-------------------- 
    async def shuffle_status():
        while True:
            status = random.choice(statuses)
            await bot.change_presence(activity=discord.Game(name=status))
            await asyncio.sleep(10) 

    bot.loop.create_task(shuffle_status())

bot.run('') # replace with your token
# do not share your token with anyone

import discord
from discord.ext import commands
from utils.storage import load, save
import os

DATA_FOLDER = "data"
SHADOW_FILE = os.path.join(DATA_FOLDER, "shadowban.json")

class Invisible(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.shadowbanned = load(SHADOW_FILE)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if str(message.author.id) in self.shadowbanned:
            await message.delete()

    @commands.command(name="shadowban")
    @commands.has_permissions(manage_messages=True)
    async def shadowban(self, ctx, member: discord.Member):
        self.shadowbanned[str(member.id)] = True
        save(SHADOW_FILE, self.shadowbanned)

    @commands.command(name="unshadowban")
    @commands.has_permissions(manage_messages=True)
    async def unshadowban(self, ctx, member: discord.Member):
        self.shadowbanned.pop(str(member.id), None)
        save(SHADOW_FILE, self.shadowbanned)

    @commands.command(name="jail")
    @commands.has_permissions(manage_roles=True)
    async def jail(self, ctx, member: discord.Member):
        role = discord.utils.get(ctx.guild.roles, name="Jailed")
        if not role:
            role = await ctx.guild.create_role(name="Jailed")
            for ch in ctx.guild.channels:
                await ch.set_permissions(role, view_channel=False)
        await member.edit(roles=[role])

    @commands.command(name="ghost")
    @commands.has_permissions(kick_members=True)
    async def ghost(self, ctx, member: discord.Member):
        await member.kick(reason="ghosted")

def setup(bot):
    bot.add_cog(Invisible(bot))


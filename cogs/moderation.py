import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="kick")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)

    @commands.command(name="ban")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)

    @commands.command(name="unban")
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, user):
        name, disc = user.split("#")
        for ban in await ctx.guild.bans():
            if (ban.user.name, ban.user.discriminator) == (name, disc):
                await ctx.guild.unban(ban.user)

    @commands.command(name="c")
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int, member: discord.Member = None):
        def check(m):
            return m.author == member if member else True
        await ctx.channel.purge(limit=amount, check=check)

    @commands.command(name="mute")
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member: discord.Member):
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        if not role:
            role = await ctx.guild.create_role(name="Muted")
            for ch in ctx.guild.channels:
                await ch.set_permissions(role, send_messages=False, speak=False)
        await member.add_roles(role)

    @commands.command(name="unmute")
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, member: discord.Member):
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        if role in member.roles:
            await member.remove_roles(role)

def setup(bot):
    bot.add_cog(Moderation(bot))


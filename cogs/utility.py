from discord.ext import commands

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="freeze")
    @commands.has_permissions(manage_channels=True)
    async def freeze(self, ctx):
        for role in ctx.guild.roles:
            await ctx.channel.set_permissions(role, send_messages=False)

    @commands.command(name="clone")
    @commands.has_permissions(manage_channels=True)
    async def clone(self, ctx):
        await ctx.channel.clone()

def setup(bot):
    bot.add_cog(Utility(bot))


from discord.ext import commands

class Chaos(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.echo = set()
        self.uwu = set()
        self.clown = set()

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        uid = message.author.id

        if uid in self.echo:
            await message.channel.send(message.content)

        if uid in self.uwu:
            await message.channel.send(
                message.content.replace("r", "w").replace("l", "w")
            )

        if uid in self.clown:
            await message.add_reaction("🤡")

def setup(bot):
    bot.add_cog(Chaos(bot))


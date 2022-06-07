from discord.ext import commands
import random
class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(name='ohayo', help='Ohaiyo List')
    # @bot.command(name='ohayo', help='Ohaiyo List')
    async def ohayo(ctx):
        ohaiyo_messages = ["Haro~bo~", "Nya-hello~!", "Sui-chan wa~ Kyou mo Kawaii~!!", "Konsomē", "Konkapu",
                        "Konbankitsune~", "Konbanwasshoi!", "Alona", "Haachama-chama~!", "Konaqua!", "Konshio ",
                        "Konnakiri!", "Ola! Choco!", "Chiwassu ", "Konbanmion! ", "Mogu mogu~ Okayu!", "Ooayo",
                        "Konpeko, konpeko, konpeko! Hololive san-kisei no Usada Pekora-peko! domo, domo!",
                        "Konrushi~", "Konnui", "Konbanmassuru ", "Ahoy!", "Konkanata",
                        "Good Morning MotherFuckers", "Konbandododooo ", "Konyappi", "Minna~Oru~?", "Konlamy ",
                        "Kon-nene!", " La Lion~・RaRa-ion ", "Poruka oru ka? Oru yo!", "Hey guys~"]
        random_num = random.randrange(len(ohaiyo_messages))
        await ctx.send('{} {}'.format(ohaiyo_messages[random_num], ctx.author.mention))

    @commands.command((name='otsukare', help='Otsukare List')
    # @bot.command(name='otsukare', help='Otsukare List')
    async def otsukare(ctx):
        otsukare_messages = ["Haro~bo~", "Nya-hello~!", "Sui-chan wa~ Kyou mo Kawaii~!!", "Konsomē", "Konkapu",
                            "Konbankitsune~", "Konbanwasshoi!", "Alona", "Haachama-chama~!", "Konaqua!", "Konshio ",
                            "Konnakiri!", "Ola! Choco!", "Chiwassu ", "Konbanmion! ", "Mogu mogu~ Okayu!", "Ooayo",
                            "Konpeko, konpeko, konpeko! Hololive san-kisei no Usada Pekora-peko! domo, domo!",
                            "Konrushi~", "Konnui", "Konbanmassuru ", "Ahoy!", "Konkanata",
                            "Good Morning MotherFuckers", "Konbandododooo ", "Konyappi", "Minna~Oru~?", "Konlamy ",
                            "Kon-nene!", " La Lion~・RaRa-ion ", "Poruka oru ka? Oru yo!", "Hey guys~"]
        random_num = random.randrange(len(otsukare_messages))
        await ctx.send('{} {}'.format(otsukare_messages[random_num], ctx.author.mention))

def setup(bot):
    bot.add_cog(Greetings(bot))
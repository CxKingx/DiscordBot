import discord
#https://cog-creators.github.io/discord-embed-sandbox/
# https://support.discord.com/hc/en-us/articles/210298617-Markdown-Text-101-Chat-Formatting-Bold-Italic-Underline-
def functionlist():
  embed=discord.Embed(title="Chance Questions", description=" ", color=0xda0b0b)
  embed.add_field(name="^lc name1 name2", value="Chance of both subjects in love with each other", inline=False)
  embed.add_field(name="^askchance question", value="Ask  the chance of something happening", inline=False)
  embed.add_field(name="^random", value="give a random value from 0 - 10000", inline=False)
  embed.add_field(name="^choose a;b;c.....", value="Pick 1 choice between all the things you gave", inline=False)
  return embed
  #await ctx.send(embed=embed)
  
def weeblist():
  embed=discord.Embed(title="Picture weeb stuff", description=" ", color=0xfb05ff)
  embed.add_field(name="^aniquote", value="Gives a random quote from an anime character", inline=True)
  embed.add_field(name="^cry", value="Gives a cry gif", inline=False)
  embed.add_field(name="^trap", value="Gives a hentai trap gif", inline=True)
  embed.add_field(name="^neko", value="Gives a neko gif", inline=True)
  embed.add_field(name="^nekoh", value="Gives a hentai neko gif", inline=True)
  embed.add_field(name="^pat @someone", value="Pat that person", inline=True)
  embed.add_field(name="^punch @someone", value="punch that person", inline=True)
  embed.add_field(name="^hug @someone", value="Hug that person", inline=True)
  embed.add_field(name="^bite @someone", value="Bite that person", inline=True)
  embed.add_field(name="^kiss @someone", value="Kiss that person", inline=True)
  embed.add_field(name="^slap @someone", value="Slap that person", inline=True)
  embed.add_field(name="^cuddle @someone", value="Cuddle that person", inline=True)
  embed.add_field(name="^bonk @someone", value="Bonk that person", inline=True)
  embed.add_field(name="^yeet @someone", value="yeet that person", inline=True)
  embed.add_field(name="^boob", value="Gives a Boob gif", inline=True)
  embed.add_field(name="^hentai1", value="Gives a hentai gif", inline=True)
  embed.add_field(name="^hentai2", value="Gives a hentai gif", inline=True)
  return embed
def normalCommands():
  embed=discord.Embed(title="Other Commands and replies", description=" ", color=0xFFFF00)
  embed.add_field(name="^avatar", value="Get your own profile picture", inline=True)
  embed.add_field(name="^avatar @Someone", value="Get mentioned profile picture", inline=True)
  embed.add_field(name="ohayo", value="Return a greeting from hololive", inline=True)
  embed.add_field(name="otsukare", value="Return a otsukare phrase from hololive", inline=True)
  embed.add_field(name="should i listen to argo?", value="burmese detected opinion rejected", inline=True)
  embed.add_field(name="do i party with ritsu", value="Don\'t, you will lose mmr", inline=True)
  return embed
import asyncio
import os
import discord
from discord.ext import commands
# import validators
import random
import requests
# import youtube_dl
import sqlite3
# Test From Pycharm
from ChanceFunctions import ChanceFunc
from DatabaseFunctions import getDotaID, registerDotaID, deleteDotaID, registerImage, getImage, deleteimage, \
    CreateDatabases
from helplist import functionlist, weeblist, normalCommands
from apifunction import WaifuPic
from ReactionsFunction import WaitReaction

# Secret Discord Token
my_secret = os.environ['DISCORD_TOKEN']
# print(my_secret)


# client = discord.Client()
bot = commands.Bot(command_prefix='^', intents=discord.Intents.all())
waifuPic = WaifuPic()
chancefunc = ChanceFunc()
CreateDatabases()


@bot.event
async def on_ready():
    print('We have logged in as  {0.user}'.format(bot))
    # print('alo')


@bot.command(name='test', help='Hello')
async def test(ctx, message: str):
    print(ctx)
    print(str(ctx))
    print(message)
    await ctx.send(f'Hello {ctx.message.author.name}!')


@bot.command()
async def args(ctx, *args):
    response = ""
    for arg in args:
        response = response + " " + arg

        # SENDS A MESSAGE TO THE CHANNEL USING THE CONTEXT OBJECT.
    await ctx.channel.send(response)
    await ctx.channel.send(len(args))
    await ctx.channel.send(args[0])


## Not sure if we want to use ^ on this
@bot.command(name='hello', help='Hello')
async def say_hello(ctx):
    await ctx.send(f'Hello {ctx.message.author.name}!')


## Not sure if we want to use ^ on this
@bot.command(name='bye', help='Bye')
async def say_bye(ctx):
    await ctx.send(f'See you later {ctx.message.author.name}!')


@bot.command(name='random', help='Random number Generator')
async def rdm_number(ctx):
    await ctx.send(f'This is ur random number: {random.randrange(10000)}')


## Not sure if we want to use ^ on this
@bot.command(name='morning', help='Good Morning List')
async def morning(ctx):
    morning_messages = ["Good Morning", "おはようございます", "Selamat Pagi", "Pagi Anjeng", "Pagi Cuk"]
    random_num = random.randrange(len(morning_messages))
    await ctx.send('{} {}'.format(morning_messages[random_num], ctx.author.mention))


@bot.command(name='ohayo', help='Ohaiyo List')
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


@bot.command(name='otsukare', help='Otsukare List')
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


@bot.command(name='askchance', help='Ask a chance of something happening')
async def askchance(ctx, *args):
    message = " ".join(args)
    print(" ".join(args))
    # print('msg is ' + message)
    chancefunc.setMessage(message)

    print('newmsg is' + str(chancefunc.getMessage()))
    await ctx.send(chancefunc.askchance())


@bot.command(name='choose', help='Choose from your given options')
async def ChooseChoices(ctx, *args):
    if len(args) > 1:
        ctx.send('arguments are wrong, please use ^choose a;b;c;d')
    else:
        message = " ".join(args)
        chancefunc.setMessage(message)
        print('newmsg is' + str(chancefunc.getMessage()))
        await ctx.send(embed=chancefunc.choosechoices())


@bot.command(name='bite', help='Bite Someone')
async def bite(ctx, message: str):
    image = waifuPic.fetchanimubite()
    title_msg = str(ctx.author.name) + " bite " + message
    embedVar = discord.Embed(description=title_msg, color=0x00ff00)
    embedVar.set_image(url=list(image.values())[0])
    await ctx.send(embed=embedVar)


@bot.command(name='bonk', help='Bonk someone')
async def bonk(ctx, message: str):
    image = waifuPic.fetchanimubonk()
    title_msg = str(ctx.author.name) + " bonked " + message
    embedVar = discord.Embed(description=title_msg, color=0x00ff00)
    embedVar.set_image(url=list(image.values())[0])
    await ctx.send(embed=embedVar)


@bot.command(name='pat', help='Pat someone')
async def pat(ctx, message: str):
    image = waifuPic.fetchanimupat()
    title_msg = str(ctx.author.name) + " patted " + message
    embedVar = discord.Embed(description=title_msg, color=0x00ff00)
    embedVar.set_image(url=list(image.values())[0])
    await ctx.send(embed=embedVar)


@bot.command(name='yeet', help='Yeet someone')
async def yeet(ctx, message: str):
    image = waifuPic.fetchanimuyeet()
    title_msg = str(ctx.author.name) + " yeeted " + message
    embedVar = discord.Embed(description=title_msg, color=0x00ff00)
    embedVar.set_image(url=list(image.values())[0])
    await ctx.send(embed=embedVar)


@bot.command(name='kiss', help='Kiss someone')
async def kiss(ctx, message: str):
    image = waifuPic.fetchanimukiss()
    title_msg = str(ctx.author.name) + " kissed " + message
    embedVar = discord.Embed(description=title_msg, color=0x00ff00)
    embedVar.set_image(url=list(image.values())[0])
    await ctx.send(embed=embedVar)


@bot.command(name='slap', help='Slap someone')
async def slap(ctx, message: str):
    image = waifuPic.fetchanimuslap()
    title_msg = str(ctx.author.name) + " slapped " + message
    embedVar = discord.Embed(description=title_msg, color=0x00ff00)
    embedVar.set_image(url=list(image.values())[0])
    await ctx.send(embed=embedVar)


@bot.command(name='cuddle', help='Cuddle someone')
async def cuddle(ctx, message: str):
    image = waifuPic.fetchanimucuddle()
    title_msg = str(ctx.author.name) + " cuddled " + message
    embedVar = discord.Embed(description=title_msg, color=0x00ff00)
    embedVar.set_image(url=list(image.values())[0])
    await ctx.send(embed=embedVar)


@bot.command(name='hug', help='Hug someone')
async def bonk(ctx, message: str):
    image = waifuPic.fetchanimuhug()
    title_msg = str(ctx.author.name) + " hugged " + message
    embedVar = discord.Embed(description=title_msg, color=0x00ff00)
    embedVar.set_image(url=list(image.values())[0])
    await ctx.send(embed=embedVar)


@bot.command(name='punch', help='Punch someone')
async def bonk(ctx, message: str):
    image = waifuPic.fetchanimupunch()
    title_msg = str(ctx.author.name) + " punched " + message
    embedVar = discord.Embed(description=title_msg, color=0x00ff00)
    embedVar.set_image(url=list(image.values())[0])
    await ctx.send(embed=embedVar)


@bot.command(name='hi5', help='Hi5 someone')
async def bonk(ctx, message: str):
    image = waifuPic.fetchanimuhi5()
    title_msg = str(ctx.author.name) + " hi-5 " + message
    embedVar = discord.Embed(description=title_msg, color=0x00ff00)
    embedVar.set_image(url=list(image.values())[0])
    await ctx.send(embed=embedVar)


@bot.command(name='cry', help='Gives Cry Image')
async def cry(ctx):
    image = waifuPic.fetchanimucry()
    embedVar = discord.Embed(description="cry <:sadge:846384793431048203>", color=0x00ff00)
    embedVar.set_image(url=list(image.values())[0])
    await ctx.send(embed=embedVar)


@bot.command(name='megumin', help='Gives megumin Image')
async def megumin(ctx):
    image = waifuPic.fetchanimumegumin()
    embedVar = discord.Embed(description="Explooosion", color=0x00ff00)
    embedVar.set_image(url=list(image.values())[0])
    await ctx.send(embed=embedVar)


@bot.command(name='shinobu', help='Gives shinobu Image')
async def shinobu(ctx):
    image = waifuPic.fetchanimushinobu()
    embedVar = discord.Embed(description="Ara Ara", color=0x00ff00)
    embedVar.set_image(url=list(image.values())[0])
    await ctx.send(embed=embedVar)


@bot.command(name='neko', help='Gives neko Image')
async def neko(ctx):
    image = waifuPic.fetchanimunekosfw()
    embedVar = discord.Embed(description="Neko Nyaaaa", color=0x00ff00)
    embedVar.set_image(url=list(image.values())[0])
    await ctx.send(embed=embedVar)

def checkNSFW(ctx):
    if ctx.channel.is_nsfw():
        return True
    else:
        return False

@bot.command(name='nekoh', help='Gives neko hentai Image')
async def neko(ctx):
    if checkNSFW(ctx):
        image = waifuPic.fetchanimuneko()
        embedVar = discord.Embed(description="Neko Nyaaaa", color=0x00ff00)
        embedVar.set_image(url=list(image.values())[0])
        await ctx.send(embed=embedVar)
    else :
        await ctx.send('Please use dis command in a NSFW Channel')

@bot.command(name='hentai', help='Gives hentai Image1')
async def hentai1(ctx):
    if checkNSFW(ctx):
        image = waifuPic.fetchanimuhentai()
        embedVar = discord.Embed(description="kimochiii...  <:booba:846383152838082571>", color=0x00ff00)
        embedVar.set_image(url=list(image.values())[0])
        await ctx.send(embed=embedVar)
    else :
        await ctx.send('Please use dis command in a NSFW Channel')

@bot.command(name='hentai2', help='Gives hentai Image1')
async def hentai2(ctx):
    if checkNSFW(ctx):
        image = waifuPic.fetchanimuwaifunsfw()
        embedVar = discord.Embed(description="kimochiii...  <:booba:846383152838082571>", color=0x00ff00)
        embedVar.set_image(url=list(image.values())[0])
        await ctx.send(embed=embedVar)
    else :
        await ctx.send('Please use dis command in a NSFW Channel')

@bot.command(name='trap', help='Gives Trap Hentai Image')
async def trap(ctx):
    if checkNSFW(ctx):
        image = waifuPic.fetchanimutrap()
        embedVar = discord.Embed(description="kimochiii...  <:booba:846383152838082571>", color=0x00ff00)
        embedVar.set_image(url=list(image.values())[0])
        await ctx.send(embed=embedVar)
    else :
        await ctx.send('Please use dis command in a NSFW Channel')

@bot.command(name='boob', help='Gives Boob Hentai Image')
async def trap(ctx):
    if checkNSFW(ctx):
        image = waifuPic.fetchanimuboob()
        embedVar = discord.Embed(description="Booba...  <:booba:846383152838082571>", color=0x00ff00)
        embedVar.set_image(url=list(image.values())[0])
        await ctx.send(embed=embedVar)
    else :
        await ctx.send('Please use dis command in a NSFW Channel')

# @bot.command(name = 'id', help = 'Get the user Dota2 ID')
# async def get_id(ctx):
#     discord_id = ctx.guild.members
#     print(discord_id)
#     if getDotaID(discord_id) is not Null:
#         await ctx.send(embed=embedVar2)
#     else:
#         await ctx.send(embed=embedVar)
# await message.channel.send(embed=embedVar)


# if message.mentions:
#     embedVar2 = getDotaID(message.mentions[0].id)
#     await message.channel.send(embed=embedVar2)
#     return
# else:
#     embedVar = getDotaID(message.author.id)
#     await message.channel.send(embed=embedVar)
#     return

# Kind of Dangerous cuz the bot have admin so can give practically any roles
@bot.command(name='giverole', pass_context=True)
async def giverole(ctx, user: discord.Member, role: discord.Role):
    await user.add_roles(role)
    # await ctx.send(f"hey {ctx.author.name}, {user.name} has been giving a role called: {role.name}")


@bot.command(name='removerole', pass_context=True)
async def giverole(ctx, user: discord.Member, role: discord.Role):
    await user.remove_roles(role)
    # await ctx.send(f"hey {ctx.author.name}, {user.name} has been remove a role called: {role.name}")


# https://stackoverflow.com/questions/48846859/how-to-check-if-a-user-has-provided-an-argument-discord-py
@bot.command(name='avatar', help='Gets the your avatar / the person\'s avatar you metioned')
async def avatar(ctx, user: discord.Member = None):
    # if mentioned
    if user:
        print('get avatar ' + str(user))
        embedVar = discord.Embed(title=user, color=0x00ff00)
        embedVar.set_image(url=user.avatar_url)
        await ctx.send(embed=embedVar)
    else:  # not mention get self
        print('get avatar ' + str(ctx.author))
        embedVar2 = discord.Embed(title=ctx.author, color=0x00ff00)
        embedVar2.set_image(url=ctx.author.avatar_url)
        await ctx.send(embed=embedVar2)


# @client.command(name='avatar',aliases=['Avatar','av'])
# async def av_cmd(ctx,user:discord.Member):
#     mbed = discord.Embed(
#         color=discord.colour(0xffff),
#         title=f'{user}'
#     )
#     mbet.set_image(url=)

# kept_message=None
# userTotal=0
# @client.event
# async def on_reaction_remove(reaction,user):
#     await reaction.message.channel.send("on_raw_reaction_remove called")
# @client.event
# async def on_reaction_add(reaction, user):
#     global userTotal
#     await reaction.message.channel.send('Total reaction is '+str(reaction.count)+' emoji is '+str(reaction))
#     if reaction.message == kept_message and userTotal<10 and str(reaction) == '<:watamepog:781536094591123546>':
#         #await reaction.message.channel.send(str(user)+" Reacted on the Que Message and total is"+str(reaction.count))
#         new_Que_message = que_message+' '+str(user)
#         embedVar = discord.Embed(title=new_Que_message,
#                                  description='',
#                                  color=0x00ff00)
#         #await kept_message.edit(content = (kept_message.content+' \n'+str(user)))
#         await kept_message.edit(embed=embedVar)
#         userTotal=userTotal+1
#         if userTotal==4:
#             await reaction.message.channel.send("Que pop ")
#


# @client.event
# async def on_message(message):
#     global kept_message
#     global que_message
#     username = str(message.author).split('#')[0]
#     user_message = str(message.content)
#     split_message = user_message.split()
#     channel = str(message.channel.name)
#     channelID = str(message.channel.id)
#     channel_nsfw = message.channel.is_nsfw()
#     print(f'{username}: {user_message} ({channel}) (ID: {channelID})')
#     chancefunc = ChanceFunc(split_message)
#     waifupic = WaifuPic()
#     print(split_message)
#     print(len(split_message))
#     print(message.author.id)

#     if message.author == client.user:
#         if message.content == 'Que pop':
#             await message.channel.send("Deleting Que ")
#             kept_message=None
#             userTotal=0
#         return
#     print(message)
#     if message.content == 'testResponse':
#         sent_message = await message.channel.send("Waiting for response...")
#         try:
#             res = await client.wait_for(
#                 "message",
#                 check=lambda x: x.channel.id == message.channel.id
#                                 and message.author.id == x.author.id
#                                 and x.content.lower() == "yes"
#                                 or x.content.lower() == "no",
#                 timeout=5,
#             )
#         except Exception as e:
#             await sent_message.edit(content=f"{message.author} No reply in time")
#         if res.content.lower() == "yes":
#             await sent_message.edit(content=f"{message.author} said yes!")
#         else:
#             await sent_message.edit(content=f"{message.author} said no!")
#         return

#     if message.content == 'testReaction':

#         kept_message2= await message.channel.send("Waiting for response...")
#         try:
#             reaction, user = await client.wait_for(
#                 "reaction_add",

#                 timeout=15,
#                 check=None,
#             )

#         except asyncio.TimeoutError:
#             await message.channel.send('no react')
#         else:
#             await message.channel.send('a react')
#         return


#     # if message.content == 'testQ':
#     #     emoji = '<:watamepog:781536094591123546>'
#     #     que_message="Starting Que, press any reaction try"
#     #     embedVar = discord.Embed(title=que_message,
#     #                              description='',
#     #                              color=0x00ff00)
#     #     kept_message = await message.channel.send(embed=embedVar)
#     #     await kept_message.add_reaction(emoji)
#     #     return
#     # if message.content == 'endQ':
#     #     await message.channel.send("Q end")
#     #     kept_message=None

#     if split_message[0] == '^id':
#         if message.mentions:
#             embedVar2 = getDotaID(message.mentions[0].id)
#             await message.channel.send(embed=embedVar2)
#             return
#         else:
#             embedVar = getDotaID(message.author.id)
#             await message.channel.send(embed=embedVar)
#             return

#     if (split_message[0] == '^register') and (len(split_message) == 3):
#         if split_message[1] == 'main':
#             embedVar = registerDotaID(message.author.id, split_message[1], split_message[2])
#             await message.channel.send(embed=embedVar)
#         elif split_message[1] == 'smurf':
#             embedVar = registerDotaID(message.author.id, split_message[1], split_message[2])
#             await message.channel.send(embed=embedVar)
#         else:
#             await message.channel.send('Wrong syntax, please give "^register main/smurf DotaID"')
#         return
#     elif (split_message[0] == '^register') and (len(split_message) != 3):
#         await message.channel.send('Wrong syntax, please give "^register main/smurf DotaID"')
#         return

#     adminfunction = ['^forceregister', '^deleteid', '^forceupdate']
#     if message.author.id == 241817188665786369 and split_message[0] == '^forceregister' and (len(split_message) == 4):
#         embedVar = registerDotaID(split_message[1], split_message[2], split_message[3])
#         await message.channel.send('Force Register ')
#         await message.channel.send(embed=embedVar)
#     elif message.author.id == 241817188665786369 and split_message[0] == '^deleteid' and (len(split_message) == 2):
#         await message.channel.send('Delete ID ')
#         embedVar = deleteDotaID(split_message[1])
#         await message.channel.send(embed=embedVar)

#     elif message.author.id != 241817188665786369 and any(x == user_message.lower() for x in adminfunction):
#         await message.channel.send('Function only available to CxKingx')
#         return

#     if (split_message[0] == '^save') and (len(split_message) == 3):
#         savestatus = registerImage(split_message[1],split_message[2])
#         await message.channel.send(savestatus)
#     elif (split_message[0] == '^save') and (len(split_message) != 3):
#         await message.channel.send('Wrong Syntax, please use ^save imgname imglink')

#     if (split_message[0] == '^get') and (len(split_message) == 2):
#         imagemessage = getImage(split_message[1])
#         await message.channel.send(imagemessage)
#     elif (split_message[0] == '^get') and (len(split_message) != 2):
#         await message.channel.send('Wrong Syntax, please use ^get imgname')

#     if (split_message[0] == '^delete') and (len(split_message) == 2):
#         imagemessage = deleteimage(split_message[1])
#         await message.channel.send(imagemessage)
#     elif (split_message[0] == '^get') and (len(split_message) != 2):
#         await message.channel.send('Wrong Syntax, please use ^deleteimage imgname')

#     if (split_message[0] == '^lc') and (len(split_message) == 3):
#         if (split_message[1] != "") and (split_message[2] != ""):
#             embedVar = chancefunc.lovecalculator()
#             await message.channel.send(embed=embedVar)
#             return
#     elif (split_message[0] == '^lc') and (len(split_message) != 3):
#         await message.channel.send('Wrong syntax, please give "lc name1 name2"')
#         return

#     if (split_message[0] == '^askchance'):
#         chancestring = chancefunc.askchance()
#         await message.channel.send(chancestring)

#     if (split_message[0] == '^choose'):
#         embedVar = chancefunc.choosechoices()
#         await message.channel.send(embed=embedVar)
#         return

#     if user_message.lower() == 'hello':
#         await message.channel.send(f'Hello {username}!')
#         return
#     elif user_message.lower() == 'bye':
#         await message.channel.send(f'See you later {username}!')
#         return
#     elif user_message.lower() == '^random':
#         response = f'This is ur random number: {random.randrange(10000)}'
#         await message.channel.send(response)
#         return

#     # Dont reveal this one to the server or its gonna be chaos
#     if split_message[0] == '|':
#         splitmsg = user_message.split("|")
#         await message.delete()
#         await message.channel.send(splitmsg[1])
#         return


#     if (split_message[0].lower() == 'good') and (split_message[1].lower() == 'luck'):
#         GoodLuckMessages = ["Good Luck ", "Don't Commit UnLiving", "がんばろう", "Pasti Isa la", "Mek ngene tok ae lo"]
#         GoodLuckGifs = ["https://tenor.com/view/-gif-5021037",
#                         "https://tenor.com/view/good-luck-on-finals-anime-gif-10492580",
#                         "https://tenor.com/view/ngnl-no-game-life-good-luck-cute-girl-gif-16052910",
#                         "https://tenor.com/view/lucky-star-thumbs-up-cute-wink-anime-gif-17593886",
#                         "https://tenor.com/view/kanna-tamachi-ganbatte-kanna-ganbatte-chibi-gif-19602318",
#                         "https://tenor.com/view/myheroacedemia-anime-yes-hyped-lets-go-gif-10089435",
#                         "https://tenor.com/view/haruhi-suzumiya-cheer-lets-go-ganbaru-gif-11895168"
#                         ]
#         random_num = random.randrange(len(GoodLuckMessages))
#         random_num2 = random.randrange(len(GoodLuckGifs))
#         if (len(split_message)) == 2:
#             await message.channel.send(f'{GoodLuckMessages[random_num]}')
#             await message.channel.send(f'{GoodLuckGifs[random_num2]}')
#         elif '<@' in split_message[2]:
#             await message.channel.send(f'{GoodLuckMessages[random_num]} {split_message[2].lower()}')
#             await message.channel.send(f'{GoodLuckGifs[random_num2]}')
#         return

#     if user_message.lower() == '!anywhere':
#         await message.channel.send('waw hello <:watamepog:781536094591123546> ')
#         return

#     if split_message[0] == '^pat':
#         if (len(split_message[1]) != 0):
#             content = waifupic.fetchanimupat()
#             titlemsg = username + " patted " + split_message[1]
#             embedVar = discord.Embed(description=titlemsg, color=0x00ff00)
#             embedVar.set_image(url=list(content.values())[0])
#             await message.channel.send(embed=embedVar)
#             return

#     if split_message[0] == '^bite':
#         if (len(split_message[1]) != 0):
#             content = waifupic.fetchanimubite()
#             titlemsg = username + " bite " + split_message[1]
#             embedVar = discord.Embed(description=titlemsg, color=0x00ff00)
#             embedVar.set_image(url=list(content.values())[0])
#             await message.channel.send(embed=embedVar)
#             return

#     if split_message[0] == '^bonk':
#         if (len(split_message[1]) != 0):
#             content = waifupic.fetchanimubonk()
#             titlemsg = username + " bonked " + split_message[1]
#             embedVar = discord.Embed(description=titlemsg, color=0x00ff00)
#             embedVar.set_image(url=list(content.values())[0])
#             await message.channel.send(embed=embedVar)
#             return

#     if split_message[0] == '^yeet':
#         if (len(split_message[1]) != 0):
#             content = waifupic.fetchanimuyeet()
#             titlemsg = username + " yeeted " + split_message[1]
#             embedVar = discord.Embed(description=titlemsg, color=0x00ff00)
#             embedVar.set_image(url=list(content.values())[0])
#             await message.channel.send(embed=embedVar)
#             return
#     if split_message[0] == '^kiss':
#         if (len(split_message[1]) != 0):
#             content = fetchanimukiss()
#             titlemsg = username + " kissed " + split_message[1]
#             embedVar = discord.Embed(description=titlemsg, color=0x00ff00)
#             embedVar.set_image(url=list(content.values())[0])
#             await message.channel.send(embed=embedVar)
#             return
#     if split_message[0] == '^slap':
#         if (len(split_message[1]) != 0):
#             content = waifupic.fetchanimuslap()
#             titlemsg = username + " slapped " + split_message[1]
#             embedVar = discord.Embed(description=titlemsg, color=0x00ff00)
#             embedVar.set_image(url=list(content.values())[0])
#             await message.channel.send(embed=embedVar)
#             return
#     if split_message[0] == '^cuddle':
#         if (len(split_message[1]) != 0):
#             content = waifupic.fetchanimucuddle()
#             titlemsg = username + " cuddled " + split_message[1]
#             embedVar = discord.Embed(description=titlemsg, color=0x00ff00)
#             embedVar.set_image(url=list(content.values())[0])
#             await message.channel.send(embed=embedVar)
#             return
#     if split_message[0] == '^hug':
#         if (len(split_message[1]) != 0):
#             content = waifupic.fetchanimuhug()
#             titlemsg = username + " hugged " + split_message[1]
#             embedVar = discord.Embed(description=titlemsg, color=0x00ff00)
#             embedVar.set_image(url=list(content.values())[0])
#             await message.channel.send(embed=embedVar)
#             return

#     if split_message[0] == '^punch':
#         if (len(split_message[1]) != 0):
#             content = waifupic.fetchanimupunch()
#             titlemsg = username + " punched " + split_message[1]
#             embedVar = discord.Embed(description=titlemsg, color=0x00ff00)
#             embedVar.set_image(url=list(content.values())[0])
#             await message.channel.send(embed=embedVar)
#             return

#     if split_message[0] == '^hi5':
#         if (len(split_message[1]) != 0):
#             content = waifupic.fetchanimuhi5()
#             titlemsg = username + " high fived " + split_message[1]
#             embedVar = discord.Embed(description=titlemsg, color=0x00ff00)
#             embedVar.set_image(url=list(content.values())[0])
#             await message.channel.send(embed=embedVar)
#             return
#     if split_message[0] == '^cry':
#         content = waifupic.fetchanimucry()
#         embedVar = discord.Embed(description="cry <:sadge:846384793431048203>", color=0x00ff00)
#         embedVar.set_image(url=list(content.values())[0])
#         await message.channel.send(embed=embedVar)
#         return

#     if split_message[0] == '^megumin':
#         content = waifupic.fetchanimumegumin()
#         # titlemsg=username+" hugged "+split_message[1]
#         embedVar = discord.Embed(description="Exploosion", color=0x00ff00)
#         embedVar.set_image(url=list(content.values())[0])
#         await message.channel.send(embed=embedVar)
#         return
#     if split_message[0] == '^shinobu':
#         content = waifupic.fetchanimushinobu()
#         # titlemsg=username+" hugged "+split_message[1]
#         embedVar = discord.Embed(color=0x00ff00)
#         embedVar.set_image(url=list(content.values())[0])
#         await message.channel.send(embed=embedVar)
#         return
#     if split_message[0] == '^neko':
#         content = waifupic.fetchanimunekosfw()
#         # titlemsg=username+" hugged "+split_message[1]
#         embedVar = discord.Embed(description="Neko neko nyaa <:booba:846383152838082571>", color=0x00ff00)
#         embedVar.set_image(url=list(content.values())[0])
#         await message.channel.send(embed=embedVar)
#         return

#     if split_message[0] == '^hentaitest':
#         if channel_nsfw:
#             await message.channel.send('dis is NSFW')
#         else:
#             await message.channel.send('dis is SFW')

#     hentaicommandlist = ['^boob', '^hentai', '^hentai2', '^nekoh', '^trap']
#     if channel_nsfw and (any(x == user_message.lower() for x in hentaicommandlist)):
#         if split_message[0] == '^boob':
#             content = waifupic.fetchanimuboob()
#             # titlemsg=username+" hugged "+split_message[1]
#             embedVar = discord.Embed(description="Booba <:booba:846383152838082571>", color=0x00ff00)
#             embedVar.set_image(url=list(content.values())[0])
#             await message.channel.send(embed=embedVar)
#             return

#         if split_message[0] == '^trap':
#             content = waifupic.fetchanimutrap()
#             # titlemsg=username+" hugged "+split_message[1]
#             embedVar = discord.Embed(description="Traps <:booba:846383152838082571>", color=0x00ff00)
#             embedVar.set_image(url=list(content.values())[0])
#             await message.channel.send(embed=embedVar)
#             return

#         if split_message[0] == '^hentai2':
#             content = waifupic.fetchanimuwaifunsfw()
#             # titlemsg=username+" hugged "+split_message[1]
#             embedVar = discord.Embed(description="Booba <:booba:846383152838082571>", color=0x00ff00)
#             embedVar.set_image(url=list(content.values())[0])
#             await message.channel.send(embed=embedVar)
#             return
#         if split_message[0] == '^nekoh':
#             content = waifupic.fetchanimuneko()
#             # titlemsg=username+" hugged "+split_message[1]
#             embedVar = discord.Embed(description="Neko neko nyaa <:booba:846383152838082571>", color=0x00ff00)
#             embedVar.set_image(url=list(content.values())[0])
#             await message.channel.send(embed=embedVar)
#             return

#         if split_message[0] == '^hentai':
#             content = waifupic.fetchanimuhentai()
#             # titlemsg=username+" hugged "+split_message[1]
#             embedVar = discord.Embed(description="kimochi  <:booba:846383152838082571>", color=0x00ff00)
#             embedVar.set_image(url=list(content.values())[0])
#             await message.channel.send(embed=embedVar)
#             return

#     elif (any(x == user_message.lower() for x in hentaicommandlist)):
#         await message.channel.send('Use this command in <#869473431228399626> please')

#     if split_message[0] == '^aniquote':
#         content = waifupic.fetchanimuquote()
#         titlemsg = list(content.values())[1] + " - " + list(content.values())[2]
#         msg = list(content.values())[0]
#         embedVar = discord.Embed(title=titlemsg, description=msg, color=0x00ff00)
#         await message.channel.send(embed=embedVar)
#         return

#     if split_message[0] == '^avatar':
#         if message.mentions:

#             mentioned_avatar = message.mentions[0].avatar_url
#             # message.server.get_member(mentionded_id).avatar_url

#             embedVar2 = discord.Embed(title=message.mentions[0].name, color=0x00ff00)
#             embedVar2.set_image(url=mentioned_avatar)
#             await message.channel.send(embed=embedVar2)
#             return
#         else:
#             embedVar = discord.Embed(title=username, color=0x00ff00)
#             embedVar.set_image(url=message.author.avatar_url)
#             # https://stackoverflow.com/questions/51423859/get-profile-picture-from-set-user
#             # user = message.server.get_member("116273596605049942")

#             await message.channel.send(embed=embedVar)
#             return
#             # https://discordpy.readthedocs.io/en/stable/api.html#discord.Message.mentions
#     # if message.mentions:
#     #     await message.channel.send(message.mentions)
#     #     await message.channel.send(message.mentions[0].id)
#     fakulist = ['fak u', 'fuck you', 'fak you', 'fuck u']
#     if any(x == user_message.lower() for x in fakulist):
#         await message.channel.send(f'Well fak u too {username}! ')
#         await message.channel.send(f'https://tenor.com/view/kizuna-ai-fuck-you-mad-gif-13724813')
#         return

#     whoasklist = ['who asked?', 'Who asked', 'Who asked?', 'who ask', 'no one asked your opinion', 'no one asked',
#                   'tell me who asked', 'ok but who asked',
#                   'https://tenor.com/view/thats-crazy-fr-hoe-who-asked-gif-21374201',
#                   'https://tenor.com/view/among-us-killer-bean-tf-asked-who-asked-dance-gif-18838836',
#                   'https://tenor.com/view/who-asked-k-on-yui-anime-anime-girl-gif-24260375',
#                   'https://tenor.com/view/who-asked-yo-bro-gif-22344826',
#                   'https://tenor.com/view/travis-scott-travis-who-asked-astroworld-black-and-white-gif-23755809',
#                   'https://tenor.com/view/who-tf-asked-nasas-radar-dish-who-asked-nobody-asked-gif-17675657',
#                   'https://tenor.com/view/who-asked-nobody-asked-nobody-cares-damn-thats-crazy-gif-20130694',
#                   'https://tenor.com/view/who-asked-me-trying-to-find-who-asked-spongebob-spunch-bob-gif-22526294',
#                   'https://tenor.com/view/who-asked-me-trying-to-find-who-asked-spongebob-spunch-bob-gif-22526294',
#                   'https://tenor.com/view/bean-dance-crazy-aye-dats-fr-crazy-hoe-now-show-me-one-person-who-asked-gif-16195074',
#                   'https://tenor.com/view/asked-gif-19790611']

#     if 'who asked' in user_message or any(x == user_message.lower() for x in whoasklist) or 'did i ask' in user_message:
#         await message.reply('I did')
#         return

#     if user_message.lower() == 'do i party with ritsu':
#         emoji = '<:watamepog:781536094591123546>'
#         await message.channel.send('Don\'t, you will lose mmr')
#         await message.add_reaction(emoji)
#         return

#     if user_message.lower() == 'should i listen to argo?':
#         await message.channel.send('burmese detected opinion rejected')
#         return
#     #

#     if user_message.lower() == '^help':
#         embedchance = functionlist()
#         embedweeb = weeblist()
#         embednormal = normalCommands()
#         await message.channel.send(embed=embedchance)
#         await message.channel.send(embed=embedweeb)
#         await message.channel.send(embed=embednormal)

#         return
#     # if user_message.lower()
#     # await msg.delete()

#     if user_message.lower() == '^testconnect':
#         message_channel = message.author.voice.channel
#         await message_channel.connect()


# For normal response like aye fr, who asked, hello bye fuck you something like that
@bot.event
async def on_member_remove(member):
    print("Noob have left the server")
    # await bot.send_message(member, "Welcome!")
    for channel in member.guild.channels:
        if str(channel) == "Kuul Femili":
            await channel.send(f"""Bye {member.mention}!""")
    await member.send('take the L bozo')


@bot.event
async def on_member_join(member):
    print('joining chanel')
    for channel in member.guild.channels:
        if str(channel) == "Kuul Femili":
            await channel.send(f"""Welcome {member.mention}!""")
    await member.send('Welcome')
    # await bot.send_message(member,"Welcome!")
    # print('asd')


@bot.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    # split_message = user_message.split()
    channel = str(message.channel.name)
    channelID = str(message.channel.id)
    # channel_nsfw = message.channel.is_nsfw()
    print(f'{username}: {user_message} ({channel}) (ID: {channelID})')
    # if message.author == bot.user:
    # return
    if user_message.lower() == 'hello':
        await message.channel.send(f'Hello {username}!')
        # return
        # await bot.process_commands(message)
    if user_message.lower() == 'bye':
        await message.channel.send(f'See you later {username}!')
        # await bot.process_commands(message)
        # return

    # Dont reveal this one to the server or its gonna be chaos
    # Change this to ^remove later but dont reveal dis
    # try:
    #     if split_message[0] == '|':
    #         splitmsg = user_message.split("|")
    #         await message.delete()
    #         await message.channel.send(splitmsg[1])
    # except:
    #     print("An exception occurred")

    await bot.process_commands(message)


bot.run(my_secret)
# client.run(my_secret)

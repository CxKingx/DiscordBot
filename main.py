import asyncio
import datetime
import os
import discord
import humanfriendly
from discord.ext import commands

# import validators
import random
import requests
# import youtube_dl
import sqlite3
# Test From Pycharm
from ChanceFunctions import ChanceFunc
# from DatabaseFunctions import getDotaID, registerDotaID, deleteDotaID, registerImage, getImage, deleteimage, \
# CreateDatabases
from DatabaseFunctions import DatabaseFunctions
from DotaQue import QueSystem
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
dbObject = DatabaseFunctions()
newQue = QueSystem()

@bot.event
async def on_ready():
    print('We have logged in as  {0.user}'.format(bot))
    # print('alo')


# tree = commands.CommandTree(bot)


# @tree.command( name='tester', description='testing')  # guild specific slash command
# async def slash2(interaction: discord.Interaction):
#     await interaction.response.send_message(f"I am working! I was made with Discord.py!", ephemeral=True)
#

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

@bot.command(name='random', help='Random number Generator')
async def rdm_number(ctx):
    await ctx.send(f'This is ur random number: {random.randrange(10000)}')

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

@bot.command(name='scrt', help='Message using the bot')
async def secret(ctx, *args):
    message = " ".join(args)
    print(" ".join(args))
    # print('msg is ' + message)
    await ctx.message.delete()
    await ctx.send(message)

#@bot.command(name='delmsg', help='Delete Message using the bot')
@bot.command(name='delmsg' , hidden=True)
async def delmsg(ctx, messageID):
    await ctx.message.delete()
    original = await ctx.channel.fetch_message(messageID)
    # newmsg = message.channel.fetch_message(split_message[1])
    await original.delete()


@bot.command(name='choose', help='Choose from your given options ^choose a;b;c;d;e;f')
async def ChooseChoices(ctx, *args):
    if len(args) > 1:
        ctx.send('arguments are wrong, please use ^choose a;b;c;d')
    else:
        message = " ".join(args)
        chancefunc.setMessage(message)
        print('newmsg is' + str(chancefunc.getMessage()))
        await ctx.send(embed=chancefunc.choosechoices())

### Mod Functions
@bot.command()
async def timeout(ctx, user: discord.Member, time=None, reason=None):
  time = humanfriendly.parse_timespan(time)
  await user.timeout_for(time)
  #await user.edit(timed_out_until=datetime.timedelta(seconds=time))
  #await user.timeout(until = discord.utils.utcnow() + datetime.timedelta(seconds=time), reason=reason)
  await ctx.send (f"{user} Timeouted for {time}")



### Mod Function End

### Animu Section

@bot.command(name='bite', help='Bite Someone')
async def bite(ctx, user: str):
    image = waifuPic.fetchanimubite()
    title_msg = str(ctx.author.name) + " bite " + user
    embedVar = discord.Embed(description=title_msg, color=0x00ff00)
    embedVar.set_image(url=list(image.values())[0])
    await ctx.send(embed=embedVar)


@bot.command(name='bonk', help='Bonk someone')
async def bonk(ctx, user: str):
    image = waifuPic.fetchanimubonk()
    title_msg = str(ctx.author.name) + " bonked " + user
    embedVar = discord.Embed(description=title_msg, color=0x00ff00)
    embedVar.set_image(url=list(image.values())[0])
    await ctx.send(embed=embedVar)


@bot.command(name='pat', help='Pat someone')
async def pat(ctx, user: str):
    image = waifuPic.fetchanimupat()
    title_msg = str(ctx.author.name) + " patted " + user
    embedVar = discord.Embed(description=title_msg, color=0x00ff00)
    embedVar.set_image(url=list(image.values())[0])
    await ctx.send(embed=embedVar)


@bot.command(name='yeet', help='Yeet someone')
async def yeet(ctx, user: str):
    image = waifuPic.fetchanimuyeet()
    title_msg = str(ctx.author.name) + " yeeted " + user
    embedVar = discord.Embed(description=title_msg, color=0x00ff00)
    embedVar.set_image(url=list(image.values())[0])
    await ctx.send(embed=embedVar)


@bot.command(name='kiss', help='Kiss someone')
async def kiss(ctx, user: str):
    image = waifuPic.fetchanimukiss()
    title_msg = str(ctx.author.name) + " kissed " + user
    embedVar = discord.Embed(description=title_msg, color=0x00ff00)
    embedVar.set_image(url=list(image.values())[0])
    await ctx.send(embed=embedVar)


@bot.command(name='slap', help='Slap someone')
async def slap(ctx, user: str):
    image = waifuPic.fetchanimuslap()
    title_msg = str(ctx.author.name) + " slapped " + user
    embedVar = discord.Embed(description=title_msg, color=0x00ff00)
    embedVar.set_image(url=list(image.values())[0])
    await ctx.send(embed=embedVar)


@bot.command(name='cuddle', help='Cuddle someone')
async def cuddle(ctx, user: str):
    image = waifuPic.fetchanimucuddle()
    title_msg = str(ctx.author.name) + " cuddled " + user
    embedVar = discord.Embed(description=title_msg, color=0x00ff00)
    embedVar.set_image(url=list(image.values())[0])
    await ctx.send(embed=embedVar)


@bot.command(name='hug', help='Hug someone')
async def hug(ctx, user: str):
    image = waifuPic.fetchanimuhug()
    title_msg = str(ctx.author.name) + " hugged " + user
    embedVar = discord.Embed(description=title_msg, color=0x00ff00)
    embedVar.set_image(url=list(image.values())[0])
    await ctx.send(embed=embedVar)


@bot.command(name='punch', help='Punch someone')
async def punch(ctx, user: str):
    image = waifuPic.fetchanimupunch()
    title_msg = str(ctx.author.name) + " punched " + user
    embedVar = discord.Embed(description=title_msg, color=0x00ff00)
    embedVar.set_image(url=list(image.values())[0])
    await ctx.send(embed=embedVar)


@bot.command(name='hi5', help='Hi5 someone')
async def hi5(ctx, user: str):
    image = waifuPic.fetchanimuhi5()
    title_msg = str(ctx.author.name) + " hi-5 " + user
    embedVar = discord.Embed(description=title_msg, color=0x00ff00)
    embedVar.set_image(url=list(image.values())[0])
    await ctx.send(embed=embedVar)


@bot.command(name='cry', help='Gives Cry Image')
async def cry(ctx):
    image = waifuPic.fetchanimucry()
    embedVar = discord.Embed(description="cry <:sadge:846384793431048203>", color=0x00ff00)
    embedVar.set_image(url=list(image.values())[0])
    await ctx.send(embed=embedVar)

@bot.command(name='aniquote', help='Gives a quote from a random anime')
async def aniquote(ctx):
    content = waifuPic.fetchanimuquote()
    titlemsg = list(content.values())[1] + " - " + list(content.values())[2]
    msg = list(content.values())[0]
    embedVar = discord.Embed(title=titlemsg, description=msg, color=0x00ff00)
    await ctx.channel.send(embed=embedVar)

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
async def nekoh(ctx):
    if checkNSFW(ctx):
        image = waifuPic.fetchanimuneko()
        embedVar = discord.Embed(description="Neko Nyaaaa", color=0x00ff00)
        embedVar.set_image(url=list(image.values())[0])
        await ctx.send(embed=embedVar)
    else:
        await ctx.send('Please use dis command in a NSFW Channel')


@bot.command(name='hentai', help='Gives hentai Image1')
async def hentai1(ctx):
    if checkNSFW(ctx):
        image = waifuPic.fetchanimuhentai()
        embedVar = discord.Embed(description="kimochiii...  <:booba:846383152838082571>", color=0x00ff00)
        embedVar.set_image(url=list(image.values())[0])
        await ctx.send(embed=embedVar)
    else:
        await ctx.send('Please use dis command in a NSFW Channel')


@bot.command(name='hentai2', help='Gives hentai Image2')
async def hentai2(ctx):
    if checkNSFW(ctx):
        image = waifuPic.fetchanimuwaifunsfw()
        embedVar = discord.Embed(description="kimochiii...  <:booba:846383152838082571>", color=0x00ff00)
        embedVar.set_image(url=list(image.values())[0])
        await ctx.send(embed=embedVar)
    else:
        await ctx.send('Please use dis command in a NSFW Channel')


@bot.command(name='trap', help='Gives Trap Hentai Image')
async def trap(ctx):
    if checkNSFW(ctx):
        image = waifuPic.fetchanimutrap()
        embedVar = discord.Embed(description="kimochiii...  <:booba:846383152838082571>", color=0x00ff00)
        embedVar.set_image(url=list(image.values())[0])
        await ctx.send(embed=embedVar)
    else:
        await ctx.send('Please use dis command in a NSFW Channel')


@bot.command(name='boob', help='Gives Boob Hentai Image')
async def boob(ctx):
    if checkNSFW(ctx):
        image = waifuPic.fetchanimuboob()
        embedVar = discord.Embed(description="Booba...  <:booba:846383152838082571>", color=0x00ff00)
        embedVar.set_image(url=list(image.values())[0])
        await ctx.send(embed=embedVar)
    else:
        await ctx.send('Please use dis command in a NSFW Channel')

### Animu Section End

### Dota ID Section

@bot.command(name='id', help='Gives Get Dota IDs')
async def getID(ctx, user: discord.Member = None):
    if user:
        embedVar = dbObject.getDotaID(user.id)
        await ctx.send(embed=embedVar)
    else:  # not mention get self
        embedVar2 = dbObject.getDotaID(ctx.author.id)
        await ctx.send(embed=embedVar2)


@bot.command(name='register', help='Register Dota IDs \n ^register main/smurf DotaID')
async def registerID(ctx, *args):
    if len(args) == 2:
        if args[0] == 'main' or args[0] == 'smurf':
            embedVar = dbObject.registerDotaID(ctx.author.id, args[0], args[1])
            await ctx.channel.send(embed=embedVar)
        else:
            await ctx.channel.send('Wrong syntax, please give "^register main/smurf DotaID"')
    else:
        await ctx.channel.send('Wrong syntax, please give "^register main/smurf DotaID"')


@bot.command(name='forceregister', help='Register Dota IDs(Can only be done by CxKingx')
async def registerID(ctx, *args):
    print(args)
    if len(args) == 3 and ctx.author.id ==241817188665786369:
        if args[1] == 'main' or args[1] == 'smurf':
            embedVar = dbObject.registerDotaID(ctx.author.id, args[1], args[2])
            await ctx.channel.send(embed=embedVar)
        else:
            await ctx.channel.send('Wrong syntax, please give "^register main/smurf DotaID"')
    else:
        await ctx.channel.send('Only <@!241817188665786369> can use this')

@bot.command(name='deleteid', help='Delete Dota IDs(Can only be done by CxKingx')
async def DeleteID(ctx, *args):
    print(args)
    if len(args) == 1 and ctx.author.id ==241817188665786369:
        embedVar = dbObject.deleteDotaID(args[0])
        await ctx.channel.send(embed=embedVar)
    else:
        await ctx.channel.send('Only <@!241817188665786369> can use this')

### Dota ID Section End

### Image Database Section

@bot.command(name='get', help='Get Image' ,Category='Images')
async def getImage(ctx, ImageName):
    imagemessage = dbObject.getImage(ImageName)
    await ctx.channel.send(imagemessage)

@bot.command(name='delete', help='Delete Image',Category='Images')
async def deleteImage(ctx, ImageName):
    imagemessage = dbObject.deleteimage(ImageName)
    await ctx.channel.send(imagemessage)

@bot.command(name='imglist', help='Get Image',Category='Images')
async def imageList(ctx):
    embedVar = dbObject.getImageList()
    await ctx.channel.send(embed=embedVar)

@bot.command(name='save', help='Get Image')
async def saveImage(ctx,*args):
    if len(args)==2:
        savestatus =dbObject.registerImage(args[0], args[1])
        await ctx.channel.send(savestatus)
    else:
        await ctx.channel.send('Wrong Syntax, please use ^save imgname imglink')

### Database Image Section end


# Kind of Dangerous cuz the bot have admin so can give practically any roles
@bot.command(name='giverole', pass_context=True, hidden=True)
async def giverole(ctx, user: discord.Member, role: discord.Role):
    await ctx.message.delete()
    await user.add_roles(role)
    # await ctx.send(f"hey {ctx.author.name}, {user.name} has been giving a role called: {role.name}")


@bot.command(name='removerole', pass_context=True, hidden=True)
async def removerole(ctx, user: discord.Member, role: discord.Role):
    await ctx.message.delete()
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

@bot.command(name='check', help='Check someones NPC response')
async def NPC(ctx, user: discord.Member = None):
    if user:
        embedVar = dbObject.GetNPCCounter(user.id)
        await ctx.send(embed=embedVar)
    else:
        embedVar = dbObject.GetNPCCounter(ctx.author.id)
        await ctx.send(embed=embedVar)

@bot.command(name='endQ', help='End a Dota Que')
async def endQ(ctx):
    if newQue.QueExist:
        channel = bot.get_channel(newQue.ChannelID)
        await newQue.messageObject.delete()
        newQue.ResetQue()
    else:
        await ctx.send('no que to end')

@bot.command(name='startQ', help='Start a Dota Que')
async def startQ(ctx):
    if newQue.QueExist:
        await ctx.send('a que is in session , go to <#979725539243880498> to join the que')
    else:
        #guild = bot.get_guild(846380741209620480) #846380741209620483 gen 979033486340010015 bot
        channel = bot.get_channel(newQue.ChannelID)

        embedVar = newQue.StartQue()
        messageObject = await channel.send(embed=embedVar)
        emoji = '<:AYAYA:846389444840128562>'
        await messageObject.add_reaction(emoji)

        print('Que message id is '+str(messageObject.id))
        newQue.RegisterMessage(messageObject)

@bot.command(name='pingQ', help='Ping the Queres')
async def pingQ(ctx):
    remaining_Slot = newQue.QueLimit-len(newQue.CurrentQue)
    await ctx.send('+'+str(remaining_Slot)+' @queres go to <#979725539243880498> to join the que')

@bot.command(name='getQ', help = 'Get Current Que')
async def getQ(ctx):
    embedVar = newQue.GetCurrentQue()
    await ctx.send(embed=embedVar)

@bot.event
async def on_reaction_add(reaction, user):
    # que channel 979725539243880498
    channel = bot.get_channel(newQue.ChannelID)
    if user != bot.user:
        print('reacted on this mesg id ' + str(reaction.message.id))
        print('que msg id is '+str(newQue.messageObject))
        if str(reaction.message.id) == str(newQue.messageObject.id):
            if(newQue.CheckUserInQue(user.id)):
                print('noithing')
            else:
                newQue.AddUser(user.id)
                if (newQue.CheckPop()):
                    #embedVar = newQue.EditQueMessage()
                    #await reaction.message.edit(embed=embedVar)
                    await reaction.message.delete()

                    await channel.send('Que has popped ,participants are')
                    await channel.send(newQue.PopQue())

                    newQue.ResetQue()
                    embedVar = newQue.StartQue()
                    messageObject = await channel.send(embed=embedVar)
                    emoji = '<:AYAYA:846389444840128562>'
                    await messageObject.add_reaction(emoji)

                    print('Que message id is ' + str(messageObject.id))
                    newQue.RegisterMessage(messageObject)

                else:
                    embedVar = newQue.EditQueMessage()
                    await reaction.message.edit(embed=embedVar)


    # For normal response like aye fr, who asked, hello bye fuck you something like that

@bot.event
async def on_raw_reaction_remove(payload):
    guild = bot.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)
    channel = bot.get_channel(979033486340010015)
    print('paylod is '+str(payload))
    if str(payload.message_id) == str(newQue.messageObject.id):
        newQue.RemoveUser(member)
        embedVar = newQue.EditQueMessage()
        print('mesg object is'+ str(newQue.messageObject))
        await newQue.messageObject.edit(embed=embedVar)
    #print('remove reaction')

@bot.event
async def on_member_remove(member):
    print(member)
    print(member.id)
    print(member.name+"  have left the server")
    guild = bot.get_guild(846380741209620480)  # find ID by right clicking on server icon and choosing "copy id" at the bottom
    if guild.get_member(member.id) is None:  # find ID by right clicking on a user and choosing "copy id" at the bottom
        channel = bot.get_channel(846380741209620483)
        await channel.send(f"""{member.name} Has left""")
    else:
        print('notih')
    # the member is not in the server, do something #

    #channel = discord.utils.get(bot.get_all_channels(), guild__name='Drazzers', name='general')
    #channel=bot.get_channel(846380741209620483)
    #channel = discord.utils.get(bot.get_all_channels(), guild__name='Kuul Femili', name='berdiskusi')
    #await channel.send(f"""{member.name} Has left""")

    #await member.send('take the L bozo')



@bot.event
async def on_member_join(member):
    print('joining chanel')
    # channel = discord.utils.get(bot.get_all_channels(), guild__name='Drazzers', name='general')
    # await channel.send(f"""{member.mention} Hello""")
    # for channel in member.guild.channels:
    #     if str(channel) == "Kuul Femili":
    #         await channel.send(f"""Welcome {member.mention}!""")
    if member.id==307535807588204544:
        await member.send("Welcome Home Arthur-sama, we and Alice miss you")
    else:
        await member.send('Welcome to the channel, careful of racist people and smoke')
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
    if message.author == bot.user:
        return

    fakulist = ['fak u', 'fuck you', 'fak you', 'fuck u']
    if any(x == user_message.lower() for x in fakulist):
        await message.channel.send(f'Well fak u too {username}! ')
        await message.channel.send(f'https://tenor.com/view/kizuna-ai-fuck-you-mad-gif-13724813')

    morningTrigger = ['gm', 'morning', 'good morning', 'mornin','ohayo']
    if any(x == user_message.lower() for x in morningTrigger):
        greeting_messages = ["Haro~bo~", "Nya-hello~!", "Sui-chan wa~ Kyou mo Kawaii~!!", "Konsomē", "Konkapu",
                             "Konbankitsune~", "Konbanwasshoi!", "Alona", "Haachama-chama~!", "Konaqua!", "Konshio ",
                             "Konnakiri!", "Ola! Choco!", "Chiwassu ", "Konbanmion! ", "Mogu mogu~ Okayu!", "Ooayo",
                             "Konpeko, konpeko, konpeko! Hololive san-kisei no Usada Pekora-peko! domo, domo!",
                             "Konrushi~", "Konnui", "Konbanmassuru ", "Ahoy!", "Konkanata",
                             "Good Morning MotherFuckers", "Konbandododooo ", "Konyappi", "Minna~Oru~?", "Konlamy ",
                             "Kon-nene!", " La Lion~・RaRa-ion ", "Poruka oru ka? Oru yo!", "Hey guys~","Good Morning",
                             "おはようございます", "Selamat Pagi", "Pagi Anjeng", "Pagi Cuk"]
        random_num = random.randrange(len(greeting_messages))
        await message.channel.send(f'{greeting_messages[random_num]} <@{message.author.id}>')


    NightTrigger = ['bye', 'good night', 'gn', '<:bedge:906981474916507739>', 'oyasumi','otsukare']
    if any(x == user_message.lower() for x in NightTrigger):
        otsukare_messages = ["Otsu-kōn deshita!", "Otsurobo", "OtsuMiko~", "Otsumachi!!", "Otsukapu",
                             "Omatsuriwasshoi!", "Otsuthal", "Otsuruuju!", "otsuaqua!", "Otsuru-n", "Otsunakiri!",
                             "Otsukareito", "Otsubaru", "Otsumion!", "Kanshoku~ Okayu!", "Otsukoron", "Otsupeko",
                             "Otsurushi~", "Otsunui", "Otsukamassuru", "Shukkou", "otsukanata!",
                             "Good Bye Motherfuckers!", "Otsunomaki ~", "Otsuyappi!", "Otsuluna~", "Otsulamy",
                             "Mata-nene!", "O tsurai o~n", "Poruka owaru ka", "Bye Bye"]

        random_num = random.randrange(len(otsukare_messages))
        await message.channel.send(f'{otsukare_messages[random_num]} <@{message.author.id}>')


    whoasklist = ['who asked?', 'who asked', 'who asked ?', 'but who asked', 'no one asked your opinion', 'no one asked',
                  'tell me who asked', 'ok but who asked', 'did i ask','who tf asked','but who tf asked','but no one asked',
                  'who dafook arsked','whos askingtho','whos asking'
                  'https://tenor.com/view/thats-crazy-fr-hoe-who-asked-gif-21374201',
                  'https://tenor.com/view/among-us-killer-bean-tf-asked-who-asked-dance-gif-18838836',
                  'https://tenor.com/view/who-asked-k-on-yui-anime-anime-girl-gif-24260375',
                  'https://tenor.com/view/who-asked-yo-bro-gif-22344826',
                  'https://tenor.com/view/travis-scott-travis-who-asked-astroworld-black-and-white-gif-23755809',
                  'https://tenor.com/view/who-tf-asked-nasas-radar-dish-who-asked-nobody-asked-gif-17675657',
                  'https://tenor.com/view/who-asked-nobody-asked-nobody-cares-damn-thats-crazy-gif-20130694',
                  'https://tenor.com/view/who-asked-me-trying-to-find-who-asked-spongebob-spunch-bob-gif-22526294',
                  'https://tenor.com/view/who-asked-me-trying-to-find-who-asked-spongebob-spunch-bob-gif-22526294',
                  'https://tenor.com/view/bean-dance-crazy-aye-dats-fr-crazy-hoe-now-show-me-one-person-who-asked-gif-16195074',
                  'https://tenor.com/view/asked-gif-19790611',
                  'https://tenor.com/view/thats-crazy-djemilah-djemilah-birnie-crazy-cool-story-bro-gif-19887310']

    if 'who asked' in user_message.lower() or any(x == user_message.lower() for x in whoasklist) or 'who-asked' in user_message.lower():
        embedVar = dbObject.AddAskCounter(message.author.id)
        await message.reply('I did')
        await message.channel.send(embed=embedVar)
#a
    aye_list =['aye fr','ÀŸŸ FR','ÂŸĘ FR','ayefr','ayye','ayez frz','ayez','frz','aye for real','damn thats crazy',
               'fr tho','哎，真的','ayfr','aye frr','a** *r','‎Â‎YE fr','ÀYE FR','Æ FR','ÁŸE FR','ong fr','4Y3 fr',
               'ÁŸE FR','ÂŸĘ FR','RF EYA',':eye::flag_fr:','АYE FRR','👁️🇫🇷','fr ong?','ayz foreal','ayz for real','eye fr',
               'a4 real',
               'https://tenor.com/view/fr-fr-ong-gif-24732056',
               'https://tenor.com/view/lil-uzi-vert-yeah-aye-fr-tho-for-real-gif-17343447',

               ]
    if (any(x == user_message for x in aye_list)) or (any(x in user_message.lower() for x in aye_list))or user_message.lower()=='aye':
        embedVar = dbObject.AddAyeCounter(message.author.id)
        #await message.reply('Thats Crazy bro')
        await message.channel.send(embed=embedVar)
    await bot.process_commands(message)


bot.run(my_secret)
# client.run(my_secret)

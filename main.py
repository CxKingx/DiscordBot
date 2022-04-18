import asyncio
import os
import discord

import random
import requests
# import youtube_dl
import sqlite3
# Test From Pycharm
from DatabaseFunctions import getDotaID, registerDotaID, deleteDotaID
from helplist import functionlist, weeblist, normalCommands
from apifunction import fetchanimuquote, fetchanimuboob, fetchanimucuddle, fetchanimuhentai, fetchanimuhug, \
    fetchanimukiss, fetchanimupat, fetchanimuslap, fetchanimuwaifunsfw, fetchanimubite, fetchanimucry, fetchanimutrap, \
    fetchanimubonk, fetchanimushinobu, fetchanimuneko, fetchanimumegumin, fetchanimuyeet, fetchanimupunch, \
    fetchanimuhi5, fetchanimunekosfw
from ChanceFunctions import lovecalculator, askchance, choosechoices
from ReactionsFunction import WaitReaction

my_secret = os.environ['DISCORD_TOKEN']

con = sqlite3.connect('DrazzBot.db')
cur = con.cursor()
cur.execute(
    '''CREATE TABLE IF NOT EXISTS DotaID (id integer PRIMARY KEY AUTOINCREMENT , DiscordID , MainID , SmurfID)''')
# DiscordID="241817188665786369"
# Main='195476844'
# smrf='183110040'
# cur.execute('''INSERT INTO DotaID ( DiscordID, MainID ,SmurfID) VALUES(?,?,?)''',[DiscordID,Main,smrf])
#
# cur.execute('''INSERT INTO DotaID ( DiscordID, MainID ,SmurfID) VALUES(?,?,?)''',['241817188665786369','195476844','183110040'])
# someone
# cur.execute('''INSERT INTO DotaID ( DiscordID, MainID ,SmurfID) VALUES(?,?,?)''',['211728160834846720','258376469','none'])
# shuri
# cur.execute('''INSERT INTO DotaID ( DiscordID, MainID ,SmurfID) VALUES(?,?,?)''',['354350188170575872','pepega shuri','smurf who?'])
# typhoon
# cur.execute('''INSERT INTO DotaID ( DiscordID, MainID ,SmurfID) VALUES(?,?,?)''',['188565992274788352','typhoon main','typhoon smurf'])
# thisbe
# cur.execute('''INSERT INTO DotaID ( DiscordID, MainID ,SmurfID) VALUES(?,?,?)''',['360783668169670656','thibse main','thisbe smurf'])
# trepi
# cur.execute('''INSERT INTO DotaID ( DiscordID, MainID ,SmurfID) VALUES(?,?,?)''',['294487555267756032','95353172','none'])

con.commit()
con.close()

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as  {0.user}'.format(client))


# @client.command(name='avatar',aliases=['Avatar','av'])
# async def av_cmd(ctx,user:discord.Member):
#     mbed = discord.Embed(
#         color=discord.colour(0xffff),
#         title=f'{user}'
#     )
#     mbet.set_image(url=)

#kept_message=None
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




@client.event
async def on_message(message):
    global kept_message
    global que_message
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    split_message = user_message.split()
    channel = str(message.channel.name)
    channelID = str(message.channel.id)
    channel_nsfw = message.channel.is_nsfw()
    print(f'{username}: {user_message} ({channel}) (ID: {channelID})')
    print(split_message)
    print(len(split_message))
    print(message.author.id)

    if message.author == client.user:
        # if message.content == 'Que pop':
        #     await message.channel.send("Deleting Que ")
        #     kept_message=None
        #     userTotal=0
        return
    #print(message)
    # if message.content == 'testResponse':
    #     sent_message = await message.channel.send("Waiting for response...")
    #     try:
    #         res = await client.wait_for(
    #             "message",
    #             check=lambda x: x.channel.id == message.channel.id
    #                             and message.author.id == x.author.id
    #                             and x.content.lower() == "yes"
    #                             or x.content.lower() == "no",
    #             timeout=5,
    #         )
    #     except Exception as e:
    #         await sent_message.edit(content=f"{message.author} No reply in time")
    #     if res.content.lower() == "yes":
    #         await sent_message.edit(content=f"{message.author} said yes!")
    #     else:
    #         await sent_message.edit(content=f"{message.author} said no!")
    #     return
    #
    # if message.content == 'testReaction':
    #
    #     kept_message2= await message.channel.send("Waiting for response...")
    #     try:
    #         reaction, user = await client.wait_for(
    #             "reaction_add",
    #
    #             timeout=15,
    #             check=None,
    #         )
    #
    #     except asyncio.TimeoutError:
    #         await message.channel.send('no react')
    #     else:
    #         await message.channel.send('a react')
    #     return
    #
    #
    # if message.content == 'testQ':
    #     emoji = '<:watamepog:781536094591123546>'
    #     que_message="Starting Que, press any reaction try"
    #     embedVar = discord.Embed(title=que_message,
    #                              description='',
    #                              color=0x00ff00)
    #     kept_message = await message.channel.send(embed=embedVar)
    #     await kept_message.add_reaction(emoji)
    #     return
    # if message.content == 'endQ':
    #     await message.channel.send("Q end")
    #     kept_message=None

    if split_message[0] == '^id':
        if message.mentions:
            embedVar2 = getDotaID(message.mentions[0].id)
            await message.channel.send(embed=embedVar2)
            return
        else:
            embedVar = getDotaID(message.author.id)
            await message.channel.send(embed=embedVar)
            return

    if (split_message[0] == '^register') and (len(split_message) == 3):
        if split_message[1] == 'main':
            embedVar = registerDotaID(message.author.id, split_message[1], split_message[2])
            await message.channel.send(embed=embedVar)
        elif split_message[1] == 'smurf':
            embedVar = registerDotaID(message.author.id, split_message[1], split_message[2])
            await message.channel.send(embed=embedVar)
        else:
            await message.channel.send('Wrong syntax, please give "^register main/smurf DotaID"')
        return
    elif (split_message[0] == '^register') and (len(split_message) != 3):
        await message.channel.send('Wrong syntax, please give "^register main/smurf DotaID"')
        return

    adminfunction = ['^forceregister', '^deleteid', '^forceupdate']
    if message.author.id == 241817188665786369 and split_message[0] == '^forceregister' and (len(split_message) == 4):
        embedVar = registerDotaID(split_message[1], split_message[2], split_message[3])
        await message.channel.send('Force Register ')
        await message.channel.send(embed=embedVar)
    elif message.author.id == 241817188665786369 and split_message[0] == '^deleteid' and (len(split_message) == 2):
        await message.channel.send('Delete ID ')
        embedVar = deleteDotaID(split_message[1])
        await message.channel.send(embed=embedVar)

    elif message.author.id != 241817188665786369 and any(x == user_message.lower() for x in adminfunction):
        await message.channel.send('Function only available to CxKingx')
        return

    if (split_message[0] == '^lc') and (len(split_message) == 3):
        if (split_message[1] != "") and (split_message[2] != ""):
            embedVar = lovecalculator(split_message)
            await message.channel.send(embed=embedVar)
            return
    elif (split_message[0] == '^lc') and (len(split_message) != 3):
        await message.channel.send('Wrong syntax, please give "lc name1 name2"')
        return

    if (split_message[0] == '^askchance'):
        chancestring = askchance(split_message)
        await message.channel.send(chancestring)

    if (split_message[0] == '^choose'):
        embedVar = choosechoices(split_message)
        await message.channel.send(embed=embedVar)
        return

    if user_message.lower() == 'hello':
        await message.channel.send(f'Hello {username}!')
        return
    elif user_message.lower() == 'bye':
        await message.channel.send(f'See you later {username}!')
        return
    elif user_message.lower() == '^random':
        response = f'This is ur random number: {random.randrange(10000)}'
        await message.channel.send(response)
        return

    # Dont reveal this one to the server or its gonna be chaos
    if split_message[0] == '|':
        splitmsg = user_message.split("|")
        await message.delete()
        await message.channel.send(splitmsg[1])
        return

    if user_message.lower() == 'morning':
        morning_messages = ["Good Morning", "おはようございます", "Selamat Pagi", "Pagi Anjeng", "Pagi Cuk"]
        random_num = random.randrange(len(morning_messages))
        await message.channel.send(f'{morning_messages[random_num]} <@{message.author.id}>')
        return

    if user_message.lower() == 'ohayo':
        greeting_messages = ["Haro~bo~", "Nya-hello~!", "Sui-chan wa~ Kyou mo Kawaii~!!", "Konsomē", "Konkapu",
                             "Konbankitsune~", "Konbanwasshoi!", "Alona", "Haachama-chama~!", "Konaqua!", "Konshio ",
                             "Konnakiri!", "Ola! Choco!", "Chiwassu ", "Konbanmion! ", "Mogu mogu~ Okayu!", "Ooayo",
                             "Konpeko, konpeko, konpeko! Hololive san-kisei no Usada Pekora-peko! domo, domo!",
                             "Konrushi~", "Konnui", "Konbanmassuru ", "Ahoy!", "Konkanata",
                             "Good Morning MotherFuckers", "Konbandododooo ", "Konyappi", "Minna~Oru~?", "Konlamy ",
                             "Kon-nene!", " La Lion~・RaRa-ion ", "Poruka oru ka? Oru yo!", "Hey guys~"]
        random_num = random.randrange(len(greeting_messages))
        await message.channel.send(f'{greeting_messages[random_num]} <@{message.author.id}>')
        return

    if user_message.lower() == 'otsukare':
        otsukare_messages = ["Otsu-kōn deshita!", "Otsurobo", "OtsuMiko~", "Otsumachi!!", "Otsukapu",
                             "Omatsuriwasshoi!", "Otsuthal", "Otsuruuju!", "otsuaqua!", "Otsuru-n", "Otsunakiri!",
                             "Otsukareito", "Otsubaru", "Otsumion!", "Kanshoku~ Okayu!", "Otsukoron", "Otsupeko",
                             "Otsurushi~", "Otsunui", "Otsukamassuru", "Shukkou", "otsukanata!",
                             "Good Bye Motherfuckers!", "Otsunomaki ~", "Otsuyappi!", "Otsuluna~", "Otsulamy",
                             "Mata-nene!", "O tsurai o~n", "Poruka owaru ka", "Bye Bye"]
        random_num = random.randrange(len(otsukare_messages))
        await message.channel.send(f'{otsukare_messages[random_num]} <@{message.author.id}>')
        return

    if (split_message[0].lower() == 'good') and (split_message[1].lower() == 'luck'):
        GoodLuckMessages = ["Good Luck ", "Don't Commit UnLiving", "がんばろう", "Pasti Isa la", "Mek ngene tok ae lo"]
        GoodLuckGifs = ["https://tenor.com/view/-gif-5021037",
                        "https://tenor.com/view/good-luck-on-finals-anime-gif-10492580",
                        "https://tenor.com/view/ngnl-no-game-life-good-luck-cute-girl-gif-16052910",
                        "https://tenor.com/view/lucky-star-thumbs-up-cute-wink-anime-gif-17593886",
                        "https://tenor.com/view/kanna-tamachi-ganbatte-kanna-ganbatte-chibi-gif-19602318",
                        "https://tenor.com/view/myheroacedemia-anime-yes-hyped-lets-go-gif-10089435",
                        "https://tenor.com/view/haruhi-suzumiya-cheer-lets-go-ganbaru-gif-11895168"
                        ]
        random_num = random.randrange(len(GoodLuckMessages))
        random_num2 = random.randrange(len(GoodLuckGifs))
        if (len(split_message)) == 2:
            await message.channel.send(f'{GoodLuckMessages[random_num]}')
            await message.channel.send(f'{GoodLuckGifs[random_num2]}')
        elif '<@' in split_message[2]:
            await message.channel.send(f'{GoodLuckMessages[random_num]} {split_message[2].lower()}')
            await message.channel.send(f'{GoodLuckGifs[random_num2]}')
        return

    if user_message.lower() == '!anywhere':
        await message.channel.send('waw hello <:watamepog:781536094591123546> ')
        return

    if split_message[0] == '^pat':
        if (len(split_message[1]) != 0):
            content = fetchanimupat()
            titlemsg = username + " patted " + split_message[1]
            embedVar = discord.Embed(description=titlemsg, color=0x00ff00)
            embedVar.set_image(url=list(content.values())[0])
            await message.channel.send(embed=embedVar)
            return

    if split_message[0] == '^bite':
        if (len(split_message[1]) != 0):
            content = fetchanimubite()
            titlemsg = username + " bite " + split_message[1]
            embedVar = discord.Embed(description=titlemsg, color=0x00ff00)
            embedVar.set_image(url=list(content.values())[0])
            await message.channel.send(embed=embedVar)
            return

    if split_message[0] == '^bonk':
        if (len(split_message[1]) != 0):
            content = fetchanimubonk()
            titlemsg = username + " bonked " + split_message[1]
            embedVar = discord.Embed(description=titlemsg, color=0x00ff00)
            embedVar.set_image(url=list(content.values())[0])
            await message.channel.send(embed=embedVar)
            return

    if split_message[0] == '^yeet':
        if (len(split_message[1]) != 0):
            content = fetchanimuyeet()
            titlemsg = username + " yeeted " + split_message[1]
            embedVar = discord.Embed(description=titlemsg, color=0x00ff00)
            embedVar.set_image(url=list(content.values())[0])
            await message.channel.send(embed=embedVar)
            return
    if split_message[0] == '^kiss':
        if (len(split_message[1]) != 0):
            content = fetchanimukiss()
            titlemsg = username + " kissed " + split_message[1]
            embedVar = discord.Embed(description=titlemsg, color=0x00ff00)
            embedVar.set_image(url=list(content.values())[0])
            await message.channel.send(embed=embedVar)
            return
    if split_message[0] == '^slap':
        if (len(split_message[1]) != 0):
            content = fetchanimuslap()
            titlemsg = username + " slapped " + split_message[1]
            embedVar = discord.Embed(description=titlemsg, color=0x00ff00)
            embedVar.set_image(url=list(content.values())[0])
            await message.channel.send(embed=embedVar)
            return
    if split_message[0] == '^cuddle':
        if (len(split_message[1]) != 0):
            content = fetchanimucuddle()
            titlemsg = username + " cuddled " + split_message[1]
            embedVar = discord.Embed(description=titlemsg, color=0x00ff00)
            embedVar.set_image(url=list(content.values())[0])
            await message.channel.send(embed=embedVar)
            return
    if split_message[0] == '^hug':
        if (len(split_message[1]) != 0):
            content = fetchanimuhug()
            titlemsg = username + " hugged " + split_message[1]
            embedVar = discord.Embed(description=titlemsg, color=0x00ff00)
            embedVar.set_image(url=list(content.values())[0])
            await message.channel.send(embed=embedVar)
            return

    if split_message[0] == '^punch':
        if (len(split_message[1]) != 0):
            content = fetchanimupunch()
            titlemsg = username + " punched " + split_message[1]
            embedVar = discord.Embed(description=titlemsg, color=0x00ff00)
            embedVar.set_image(url=list(content.values())[0])
            await message.channel.send(embed=embedVar)
            return

    if split_message[0] == '^hi5':
        if (len(split_message[1]) != 0):
            content = fetchanimuhi5()
            titlemsg = username + " high fived " + split_message[1]
            embedVar = discord.Embed(description=titlemsg, color=0x00ff00)
            embedVar.set_image(url=list(content.values())[0])
            await message.channel.send(embed=embedVar)
            return
    if split_message[0] == '^cry':
        content = fetchanimucry()
        embedVar = discord.Embed(description="cry <:sadge:846384793431048203>", color=0x00ff00)
        embedVar.set_image(url=list(content.values())[0])
        await message.channel.send(embed=embedVar)
        return

    if split_message[0] == '^megumin':
        content = fetchanimumegumin()
        # titlemsg=username+" hugged "+split_message[1]
        embedVar = discord.Embed(description="Exploosion", color=0x00ff00)
        embedVar.set_image(url=list(content.values())[0])
        await message.channel.send(embed=embedVar)
        return
    if split_message[0] == '^shinobu':
        content = fetchanimushinobu()
        # titlemsg=username+" hugged "+split_message[1]
        embedVar = discord.Embed(color=0x00ff00)
        embedVar.set_image(url=list(content.values())[0])
        await message.channel.send(embed=embedVar)
        return
    if split_message[0] == '^neko':
        content = fetchanimunekosfw()
        # titlemsg=username+" hugged "+split_message[1]
        embedVar = discord.Embed(description="Neko neko nyaa <:booba:846383152838082571>", color=0x00ff00)
        embedVar.set_image(url=list(content.values())[0])
        await message.channel.send(embed=embedVar)
        return

    if split_message[0] == '^hentaitest':
        if channel_nsfw:
            await message.channel.send('dis is NSFW')
        else:
            await message.channel.send('dis is SFW')

    hentaicommandlist = ['^boob', '^hentai', '^hentai2', '^nekoh', '^trap']
    if channel_nsfw and (any(x == user_message.lower() for x in hentaicommandlist)):
        if split_message[0] == '^boob':
            content = fetchanimuboob()
            # titlemsg=username+" hugged "+split_message[1]
            embedVar = discord.Embed(description="Booba <:booba:846383152838082571>", color=0x00ff00)
            embedVar.set_image(url=list(content.values())[0])
            await message.channel.send(embed=embedVar)
            return

        if split_message[0] == '^trap':
            content = fetchanimutrap()
            # titlemsg=username+" hugged "+split_message[1]
            embedVar = discord.Embed(description="Traps <:booba:846383152838082571>", color=0x00ff00)
            embedVar.set_image(url=list(content.values())[0])
            await message.channel.send(embed=embedVar)
            return

        if split_message[0] == '^hentai2':
            content = fetchanimuwaifunsfw()
            # titlemsg=username+" hugged "+split_message[1]
            embedVar = discord.Embed(description="Booba <:booba:846383152838082571>", color=0x00ff00)
            embedVar.set_image(url=list(content.values())[0])
            await message.channel.send(embed=embedVar)
            return
        if split_message[0] == '^nekoh':
            content = fetchanimuneko()
            # titlemsg=username+" hugged "+split_message[1]
            embedVar = discord.Embed(description="Neko neko nyaa <:booba:846383152838082571>", color=0x00ff00)
            embedVar.set_image(url=list(content.values())[0])
            await message.channel.send(embed=embedVar)
            return

        if split_message[0] == '^hentai':
            content = fetchanimuhentai()
            # titlemsg=username+" hugged "+split_message[1]
            embedVar = discord.Embed(description="kimochi  <:booba:846383152838082571>", color=0x00ff00)
            embedVar.set_image(url=list(content.values())[0])
            await message.channel.send(embed=embedVar)
            return

    elif (any(x == user_message.lower() for x in hentaicommandlist)):
        await message.channel.send('Use this command in <#869473431228399626> please')

    if split_message[0] == '^aniquote':
        content = fetchanimuquote()
        titlemsg = list(content.values())[1] + " - " + list(content.values())[2]
        msg = list(content.values())[0]
        embedVar = discord.Embed(title=titlemsg, description=msg, color=0x00ff00)
        await message.channel.send(embed=embedVar)
        return

    if split_message[0] == '^avatar':
        if message.mentions:

            mentioned_avatar = message.mentions[0].avatar_url
            # message.server.get_member(mentionded_id).avatar_url

            embedVar2 = discord.Embed(title=message.mentions[0].name, color=0x00ff00)
            embedVar2.set_image(url=mentioned_avatar)
            await message.channel.send(embed=embedVar2)
            return
        else:
            embedVar = discord.Embed(title=username, color=0x00ff00)
            embedVar.set_image(url=message.author.avatar_url)
            # https://stackoverflow.com/questions/51423859/get-profile-picture-from-set-user
            # user = message.server.get_member("116273596605049942")

            await message.channel.send(embed=embedVar)
            return
            # https://discordpy.readthedocs.io/en/stable/api.html#discord.Message.mentions
    # if message.mentions:
    #     await message.channel.send(message.mentions)
    #     await message.channel.send(message.mentions[0].id)
    fakulist = ['fak u', 'fuck you', 'fak you', 'fuck u']
    if any(x == user_message.lower() for x in fakulist):
        await message.channel.send(f'Well fak u too {username}! ')
        await message.channel.send(f'https://tenor.com/view/kizuna-ai-fuck-you-mad-gif-13724813')
        return

    whoasklist = ['who asked?', 'Who asked', 'Who asked?', 'who ask', 'no one asked your opinion', 'no one asked',
                  'tell me who asked', 'ok but who asked',
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
                  'https://tenor.com/view/asked-gif-19790611']

    if 'who asked' in user_message or any(x == user_message.lower() for x in whoasklist) or 'did i ask' in user_message:
        await message.reply('I did')
        return

    if user_message.lower() == 'do i party with ritsu':
        emoji = '<:watamepog:781536094591123546>'
        await message.channel.send('Don\'t, you will lose mmr')
        await message.add_reaction(emoji)
        return

    if user_message.lower() == 'should i listen to argo?':
        await message.channel.send('burmese detected opinion rejected')
        return
    #
    if user_message.lower() == '^arturselfie':
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/846380741209620483/962244564297584691/IMG_0635.jpg')
        return
    if user_message.lower() == '^based_1':
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/846380741209620483/965488114749542430/Screenshot_20220418_134457.jpg')
        return
    if user_message.lower() == '^help':
        embedchance = functionlist()
        embedweeb = weeblist()
        embednormal = normalCommands()
        await message.channel.send(embed=embedchance)
        await message.channel.send(embed=embedweeb)
        await message.channel.send(embed=embednormal)

        return
    # if user_message.lower()
    # await msg.delete()

    if user_message.lower() == '^testconnect':
        message_channel = message.author.voice.channel
        await message_channel.connect()


client.run(my_secret)

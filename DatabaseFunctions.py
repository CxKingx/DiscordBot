import sqlite3

import discord
import validators


def getDotaID(discordID):
    # print('GetDotaID')
    con = sqlite3.connect('DrazzBot.db')
    cur = con.cursor()
    executeString = 'SELECT * FROM DotaID WHERE DiscordID ="' + str(discordID) + '"'
    # print(executeString)
    cur.execute(executeString)
    result = cur.fetchall()
    # print('The result len is'+str(len(result)))
    if (len(result) == 0):
        # print('no dota id regiester')
        embed = discord.Embed(title="", description='No Dota ID Registered', color=0xda0b0b)
    else:
        print(result)
        print(result[0][0])
        print(result[0][1])
        print(result[0][2])
        print(result[0][3])
        mentionString = '<@!' + str(discordID) + '> Dota ID'
        embed = discord.Embed(title="", description=mentionString, color=0xda0b0b)
        embed.add_field(name="Main", value=result[0][2], inline=False)
        embed.add_field(name="Smurf", value=result[0][3], inline=False)
    con.close()
    return embed


def registerDotaID(discordID, location, dotaID):
    print('register new')
    con = sqlite3.connect('DrazzBot.db')
    cur = con.cursor()
    executeString = 'SELECT * FROM DotaID WHERE DiscordID ="' + str(discordID) + '"'
    cur.execute(executeString)
    result = cur.fetchall()
    print('resultis ' + str(result))

    # print('The result len is'+str(len(result)))
    if len(result) == 0:

        embed = discord.Embed(title="", description='No Dota ID Registered, Registering a new one', color=0xda0b0b)
        if location == 'main':
            embed.add_field(name="Main", value=dotaID, inline=False)
            cur.execute('''INSERT INTO DotaID ( DiscordID, MainID ,SmurfID) VALUES(?,?,?)''',
                        [str(discordID), str(dotaID), 'none'])

        elif location == 'smurf':
            embed.add_field(name="Smurf", value=dotaID, inline=False)
            cur.execute('''INSERT INTO DotaID ( DiscordID, MainID ,SmurfID) VALUES(?,?,?)''',
                        [str(discordID), 'none', str(dotaID)])

    else:
        # print('udpate Dota ID')
        embed = discord.Embed(title="", description='Update Dota ID', color=0xda0b0b)
        # cur.execute('''Update DotaID set ? = ? where DiscordID = ?''', (location, dotaID, discordID))

        if location == 'main':
            location = 'MainID'
            updatestring = "UPDATE DotaID SET " + str(location) + " = '" + str(dotaID) + "' WHERE DiscordID = '" + str(
                discordID) + "'"
            embed.add_field(name="Main", value=dotaID, inline=False)
            cur.execute(updatestring)

        elif location == 'smurf':
            location = 'SmurfID'
            updatestring = "UPDATE DotaID SET " + str(location) + " = '" + str(dotaID) + "' WHERE DiscordID = '" + str(
                discordID) + "'"
            embed.add_field(name="Smurf", value=dotaID, inline=False)
            cur.execute(updatestring)

    con.commit()
    con.close()
    return embed


def deleteDotaID(discordID):
    con = sqlite3.connect('DrazzBot.db')
    cur = con.cursor()
    executeString = 'SELECT * FROM DotaID WHERE DiscordID ="' + str(discordID) + '"'
    cur.execute(executeString)
    result = cur.fetchall()
    if len(result) == 0:
        embed = discord.Embed(title="Nothing to Delete", description='', color=0xda0b0b)
    else:
        embed = discord.Embed(title="Delete", description='Delete ' + str(discordID), color=0xda0b0b)
        updatestring = 'DELETE FROM DotaID WHERE DiscordID ="' + str(discordID) + '"'
        cur.execute(updatestring)
    con.commit()
    con.close()
    return embed

def registerImage(imagename , imagelink):
    con = sqlite3.connect('ImageStorage.db')
    cur = con.cursor()
    executeString = 'SELECT * FROM ImageStorage WHERE imageName ="' + str(imagename) + '"'
    # print(executeString)
    cur.execute(executeString)
    result = cur.fetchall()
    # print('The result len is'+str(len(result)))
    if (len(result) == 0):
        # print('no dota img regiester')
        if validators.url(imagelink):
            cur.execute('''INSERT INTO ImageStorage ( imagename, imagelink) VALUES(?,?)''',
                        [str(imagename), str(imagelink)])
            message = 'Image ' + str(imagename) + ' registered'
        else:
            message = 'Not a valid image link'


    else:
        message = 'A image with name:' + str(imagename) + ' is registered'
    con.commit()
    con.close()

    return message

def getImage(imagename):
    con = sqlite3.connect('ImageStorage.db')
    cur = con.cursor()
    executeString = 'SELECT * FROM ImageStorage WHERE imageName ="' + str(imagename) + '"'
    # print(executeString)
    cur.execute(executeString)
    result = cur.fetchall()
    # print('The result len is'+str(len(result)))
    if (len(result) == 0):
        # print('no dota id regiester')
        message='No image with this name is registered '
    else:
        print(result)
        print(result[0][0]) # ID
        print(result[0][1]) # Name
        print(result[0][2]) # Link
        #print(result[0][3])
        message = result[0][2]
    con.close()
    return message

def deleteimage(imagename):
    con = sqlite3.connect('ImageStorage.db')
    cur = con.cursor()
    executeString = 'SELECT * FROM ImageStorage WHERE imageName ="' + str(imagename) + '"'
    cur.execute(executeString)
    result = cur.fetchall()
    if len(result) == 0:
        message = 'Nothing to Delete'
    else:

        updatestring = 'DELETE FROM ImageStorage WHERE imageName ="' + str(imagename) + '"'
        cur.execute(updatestring)
        message = 'Image '+str(imagename)+' is deleted'
    con.commit()
    con.close()
    return message

def getImageList():
    con = sqlite3.connect('ImageStorage.db')
    cur = con.cursor()
    executeString = 'SELECT * FROM ImageStorage'
    # print(executeString)
    cur.execute(executeString)
    result = cur.fetchall()
    # print('The result len is'+str(len(result)))
    if (len(result) == 0):
        # print('no dota id regiester')
        message='Nothing is in the database '
    else:
        embed = discord.Embed(title="Image List", description=" ", color=0xda0b0b)
        for x in result:
            print(x[1])

            embed.add_field(name=x[1],value='\u200b',inline=True)
        #print(result)
        #print(result[0][0])
        #print(result[0][1])
        #print(result[0][2])
        #print(result[0][3])
        message = result[0][2]
    con.close()
    return embed
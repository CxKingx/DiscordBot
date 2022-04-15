import sqlite3

import discord


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

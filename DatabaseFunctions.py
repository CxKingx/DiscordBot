import sqlite3

import discord
import validators

class DatabaseFunctions:
    def __init__(self):
        print('made class')
        self.CreateDatabases()

    def CreateDatabases(self):
        con = sqlite3.connect('DrazzBot.db')
        cur = con.cursor()
        cur.execute(
            '''CREATE TABLE IF NOT EXISTS DotaID (id integer PRIMARY KEY AUTOINCREMENT , DiscordID , MainID , SmurfID)''')
        con.commit()
        con.close()
        print('created database DrazzBot')
        con = sqlite3.connect('ImageStorage.db')
        cur = con.cursor()
        cur.execute(
            '''CREATE TABLE IF NOT EXISTS ImageStorage (id integer PRIMARY KEY AUTOINCREMENT , imageName , imageLink)''')
        con.commit()
        con.close()
        print('created database ImageStorage')

        con = sqlite3.connect('NPCcounter.db')
        cur = con.cursor()
        cur.execute(
            '''CREATE TABLE IF NOT EXISTS NPCcounter (id integer PRIMARY KEY AUTOINCREMENT , DiscordID , AyeCounter , AskCounter , DNCounter , JoeCounter)''')
        con.commit()
        con.close()
        print('created database NPCCounter')

        return

    def AddAskCounter(self,discordID):
        print('adding counter')
        con = sqlite3.connect('NPCcounter.db')
        cur = con.cursor()
        executeString = 'SELECT * FROM NPCcounter WHERE DiscordID ="' + str(discordID) + '"'
        cur.execute(executeString)
        result = cur.fetchall()
        if (len(result) == 0):
            print('first')
            embed = discord.Embed(title="First NPC response", color=0xda0b0b)
            message = '<@!'+str(discordID)+'> has commited who asked 1 time'
            embed.add_field(name="\u200b", value=message,
                            inline=False)
            cur.execute('''INSERT INTO NPCcounter ( DiscordID, AyeCounter ,AskCounter,DNCounter,JoeCounter) VALUES(?,?,?,?,?)''',
                        [str(discordID), '0', '1','0','0'])
            con.commit()
            con.close()
            #create and ad
            return embed
        else:
            #print('not first')
            #print(result)

            addCounter = int(result[0][3])+1
            updatestring = "UPDATE NPCcounter SET AskCounter = '" + str(addCounter) + "' WHERE DiscordID = '" + str(
                discordID) + "'"
            cur.execute(updatestring)
            con.commit()
            con.close()
            message = '<@!' + str(discordID) + '> has commited who asked '+str(addCounter)+' times'
            embed = discord.Embed(description=message, color=0xda0b0b)

            return embed

    def AddAyeCounter(self,discordID):
        print('adding  AYE counter')
        con = sqlite3.connect('NPCcounter.db')
        cur = con.cursor()
        executeString = 'SELECT * FROM NPCcounter WHERE DiscordID ="' + str(discordID) + '"'
        cur.execute(executeString)
        result = cur.fetchall()
        if (len(result) == 0):
            print('first')
            embed = discord.Embed(title="First NPC response", color=0xda0b0b)
            message = '<@!'+str(discordID)+'> has commited Aye FR 1 time'
            embed.add_field(name="\u200b", value=message,
                            inline=False)
            cur.execute('''INSERT INTO NPCcounter ( DiscordID, AyeCounter ,AskCounter,DNCounter,JoeCounter) VALUES(?,?,?,?,?)''',
                        [str(discordID), '1', '0','0','0'])
            con.commit()
            con.close()
            #create and ad
            return embed
        else:
            #print('not first')
            #print(result)

            addCounter = int(result[0][2])+1
            updatestring = "UPDATE NPCcounter SET AyeCounter = '" + str(addCounter) + "' WHERE DiscordID = '" + str(
                discordID) + "'"
            cur.execute(updatestring)
            con.commit()
            con.close()


            message = '<@!' + str(discordID) + '> has commited aye fr '+str(addCounter)+' times'
            embed = discord.Embed(description=message, color=0xda0b0b)

            return embed

    def AddDNCounter(self,discordID):
        print('adding  DN counter')
        con = sqlite3.connect('NPCcounter.db')
        cur = con.cursor()
        executeString = 'SELECT * FROM NPCcounter WHERE DiscordID ="' + str(discordID) + '"'
        cur.execute(executeString)
        result = cur.fetchall()
        if (len(result) == 0):
            print('first')
            embed = discord.Embed(title="First NPC response", color=0xda0b0b)
            message = '<@!'+str(discordID)+'> has commited DN 1 time'
            embed.add_field(name="\u200b", value=message,
                            inline=False)
            cur.execute(
                '''INSERT INTO NPCcounter ( DiscordID, AyeCounter ,AskCounter,DNCounter,JoeCounter) VALUES(?,?,?,?,?)''',
                [str(discordID), '0', '0', '1', '0'])
            con.commit()
            con.close()
            #create and ad
            return embed
        else:
            # print('not first')
            # print(result)

            addCounter = int(result[0][5])+1
            updatestring = "UPDATE NPCcounter SET DNCounter = '" + str(addCounter) + "' WHERE DiscordID = '" + str(
                discordID) + "'"
            cur.execute(updatestring)
            con.commit()
            con.close()


            message = '<@!' + str(discordID) + '> has commited DN '+str(addCounter)+' times'
            embed = discord.Embed(description=message, color=0xda0b0b)

            return embed

    def AddJoeCounter(self,discordID):
        print('adding  Joe counter')
        con = sqlite3.connect('NPCcounter.db')
        cur = con.cursor()
        executeString = 'SELECT * FROM NPCcounter WHERE DiscordID ="' + str(discordID) + '"'
        cur.execute(executeString)
        result = cur.fetchall()
        if (len(result) == 0):
            #print('first')
            embed = discord.Embed(title="First NPC response", color=0xda0b0b)
            message = '<@!'+str(discordID)+'> has commited Joe 1 time'
            embed.add_field(name="\u200b", value=message,
                            inline=False)
            cur.execute(
                '''INSERT INTO NPCcounter ( DiscordID, AyeCounter ,AskCounter,DNCounter,JoeCounter) VALUES(?,?,?,?,?)''',
                [str(discordID), '0', '0', '0', '1'])
            con.commit()
            con.close()
            #create and ad
            return embed
        else:
            #print('not first')
            #print(result)

            addCounter = int(result[0][4])+1
            updatestring = "UPDATE NPCcounter SET JoeCounter = '" + str(addCounter) + "' WHERE DiscordID = '" + str(
                discordID) + "'"
            cur.execute(updatestring)
            con.commit()
            con.close()


            message = '<@!' + str(discordID) + '> has commited Joe '+str(addCounter)+' times'
            embed = discord.Embed(description=message, color=0xda0b0b)

            return embed

    def GetNPCCounter(self,discordID):
        print('Get NPC counter')
        con = sqlite3.connect('NPCcounter.db')
        cur = con.cursor()
        executeString = 'SELECT * FROM NPCcounter WHERE DiscordID ="' + str(discordID) + '"'
        cur.execute(executeString)
        result = cur.fetchall()
        if (len(result) == 0):
            message = '<@!' + str(discordID) + '> has not commited a NPC response '
            embed = discord.Embed(description=message, color=0xda0b0b)
            return embed
        else:
            message = '<@!' + str(discordID) + '> NPC Responses Counter'
            embed = discord.Embed(description=message, color=0xda0b0b)
            message2 = 'Who Asked '+result[0][3]+' times'
            message3 = 'aye fr ' + result[0][2] + ' times'
            message4 = 'Joe ' + result[0][4] + ' times'
            message5 = 'DN ' + result[0][5] + ' times'
            embed.add_field(name=message2, value='\u200b', inline=False)
            embed.add_field(name=message3, value='\u200b', inline=False)
            #DN and Joe
            embed.add_field(name=message4, value='\u200b', inline=False)
            embed.add_field(name=message5, value='\u200b', inline=False)
            return embed



    def getDotaID(self,discordID):
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


    def registerDotaID(self,discordID, location, dotaID):
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


    def deleteDotaID(self,discordID):
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

    def registerImage(self,imagename , imagelink):
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
            message = 'A image with name: ' + str(imagename) + ' is already registered'
        con.commit()
        con.close()

        return message

    def getImage(self,imagename):
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
            print(result[0][0])
            print(result[0][1])
            print(result[0][2])
            #print(result[0][3])
            message = result[0][2]
        con.close()
        return message

    def deleteimage(self,imagename):
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

    def getImageList(self):
        con = sqlite3.connect('ImageStorage.db')
        cur = con.cursor()
        executeString = 'SELECT * FROM ImageStorage'
        # print(executeString)
        cur.execute(executeString)
        result = cur.fetchall()
        # print('The result len is'+str(len(result)))
        if (len(result) == 0):
            # print('no dota id regiester')
            message = 'Nothing is in the database '
        else:
            embed = discord.Embed(title="Image List", description=" ", color=0xda0b0b)
            for x in result:
                print(x[1])

                embed.add_field(name=x[1], value='\u200b', inline=True)
            # print(result)
            # print(result[0][0])
            # print(result[0][1])
            # print(result[0][2])
            # print(result[0][3])
            message = result[0][2]
        con.close()
        return embed
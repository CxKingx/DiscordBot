import discord
import random

class ChanceFunc:

    def __init__(self):
        self.message = None
        self.split_message=''


    def setMessage(self,Newmessage):
        self.message = Newmessage

    def getMessage(self):
        return self.message

    def lovecalculator(self):
        embedVar = discord.Embed(title=":heart: Love Compability:heart: ",
                                description=f'{self.split_message[1]} and {self.split_message[2]} are {random.randrange(100)}% compatible with each other:heart: ',
                                color=0x00ff00)
        return embedVar

    def askchance(self):
        chancestring = "Chances of " + self.message + " is " + str(random.randrange(0, 100, 1)) + "%"
        print(chancestring)
        return chancestring


    def choosechoices(self):
        self.split_message = self.message.split(';')
        print(self.split_message)
        randomChoosenum = random.randrange(len(self.split_message))
        embedVar = discord.Embed(title="This one ", description=f'{self.split_message[randomChoosenum]}', color=0x00ff00)
        return embedVar

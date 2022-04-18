import discord
import random

class ChanceFunc:
    def __init__(self, split_message):
        self.split_message = split_message


    def lovecalculator(self):
        embedVar = discord.Embed(title=":heart: Love Compability:heart: ",
                                description=f'{self.split_message[1]} and {self.split_message[2]} are {random.randrange(100)}% compatible with each other:heart: ',
                                color=0x00ff00)
        return embedVar

    def askchance(self):
        chancestring = ""
        for x in self.split_message:
            print(x)
            if x != '^askchance':
                chancestring = chancestring + " " + x
        chancestring = "Chances of" + chancestring + " is " + str(random.randrange(0, 100, 1)) + "%"
        print(chancestring)
        return chancestring


    def choosechoices(self):
        second_split = self.split_message[1].split(';')
        randomChoosenum = random.randrange(len(second_split))
        embedVar = discord.Embed(title="This one ", description=f'{second_split[randomChoosenum]}', color=0x00ff00)
        return embedVar

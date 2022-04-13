import discord
import random


def lovecalculator(split_message):
    embedVar = discord.Embed(title=":heart: Love Compability:heart: ",
                             description=f'{split_message[1]} and {split_message[2]} are {random.randrange(100)}% compatible with each other:heart: ',
                             color=0x00ff00)
    return embedVar


def askchance(split_message):
    chancestring = ""
    for x in split_message:
        if x != '^askchance':
            chancestring = chancestring + " " + x
    chancestring = "Chances of" + chancestring + " is " + str(random.randrange(0, 100, 1)) + "%"
    print(chancestring)
    return chancestring


def choosechoices(split_message):
    second_split = split_message[1].split(';')
    randomChoosenum = random.randrange(len(second_split))
    embedVar = discord.Embed(title="This one ", description=f'{second_split[randomChoosenum]}', color=0x00ff00)
    return embedVar

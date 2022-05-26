import discord

class QueSystem:

    def __init__(self):
        self.CurrentQue=[]
        self.TimeoutTime=30
        self.PreviousQue=[]
        self.messageID=0

    def StartQue(self):
        print('Starting Que') #Current Q:
        embedVar = discord.Embed(title="Current Q: ", description='Press the reaction to join ',color=0x00ff00)

        return embedVar

    def RegisterMessage(self,QueMessageID):
        self.messageID=QueMessageID
        return

    def AddUser(self,UserID):
        return
    def RemoveUser(self,UserID):
        return
    def PopQue(self):

        return


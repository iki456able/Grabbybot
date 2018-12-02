import discord
import string
import logging
import asyncio
#Set logging
logging.basicConfig(level=logging.INFO)
#Establish client
client = discord.Client()
#Login
login = False
        
@client.event
async def on_ready():
    #This is just for posterities sake
    print('Connected')
    print('Connect as: ' + client.user.name)
    print('Servers connected:')
    for x in client.servers:
        print(x.name)
    '''This is the target channel, make sure to
    turn on dev mode and grab the channel id'''
    channel = client.get_channel('channel ID')
    '''I had issues when I didn't use UTF encoding'''
    f = open('training.txt', 'a', encoding='utf-8')
    async for l in client.logs_from(channel, limit=100, reverse=True):
        #This writes the author, then the message, adding a new line
        #Each time
        nick = l.author.name
        content = l.content
        f.write(nick + ':' + '\n')
        f.write(content + '\n')
        f.write('' + '\n')
        



while login == False:
    email = input('Enter your email ')
    password = input('Enter your password ')
    client.run(email,password) 
    if client.is_logged_in == True:
        login == True


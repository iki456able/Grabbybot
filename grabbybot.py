import discord
import string
import logging
import asyncio
import datetime
#Set logging
logging.basicConfig(level=logging.INFO)
#Establish client
client = discord.Client()
#Login
login = False
        
@client.event
async def on_ready():
    channel = client.get_channel('372235987520323596')
    f = open('training.txt', 'a', encoding='utf-8')
    n = 0
    limiter = input('set limit: ')
    async for l in client.logs_from(channel, limit=int(limiter), before=datetime.datetime.now(), reverse=True):
        #This writes the author, then the message, adding a new line
        #Each time
        #Author:
        #Content
        f.write(l.author.name + ':' + '\n' + l.content + '\n' + '' + '\n')
        n = n+1
        print('added['+ str(n) +']:' + l.author.name+ ' : ' + l.content)
        if n == limiter:
            break

while login == False:
    email = input('Enter email: ')
    password = input ('Enter password: ')
    client.run(email, password) 
    if client.is_logged_in == True:
        login == True
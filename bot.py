# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 15:53:13 2020

@author: Sam
"""

import discord
import pandas as pd
from discord.ext import commands
done_words=set()
word=""
mean=""
i=0
def create_list(l):
    global req_list
    global dct
    global remaining_words ,word,mean
    words= pd.read_csv('vocabulary3.csv')
    
    if l<39:
        req_list = words[(l-1)*30:l*30]
    if l>=39:
        req_list= words[(l-1)*30:len(words)]

    dct=pd.Series(req_list.Meaning.values,index=req_list.Word).to_dict()
    word=req_list.Word[(l-1)*30]
    mean=dct[word]
    remaining_words=dct.keys().__iter__()
    next(remaining_words)
    return word

def new_word():
    global i,word,mean,remaining_words,rem_wd,done_words
    done_words.add(word)
    print(done_words)
    #remaining_words.remove(word)
    try:
        word=next(remaining_words)
        
    except:
        word="word list Empty\n"
        remaining_words=rem_wd.__iter__()
                
    print(word)
    i+=1
    return word
    
def meaning2(wrd):
    return dct[wrd]



client = commands.Bot(command_prefix = "-")
@client.event 
async def on_ready():
    print("Ready")

@client.command()
async def ping(ctx):
    await ctx.send("Pong.")
    

@client.command()
async def clear(ctx,amount=5):
    await ctx.channel.purge(limit=amount)    

@client.command(aliases=["lst","l"])
async def list(ctx,*,question):
    create_list(int(question))
    await ctx.send("List: "+question+" setup complete. ")
    await ctx.send("Words "+str((int(question)-1)*30)+" to "+str(int(question)*30)+" .")
    await ctx.send("Word : "+word)
    
rem_wd=set() 

@client.command(aliases=["NewWord","n","nw","NW","New Word","new word","newword" ])
async def newWord(ctx):
    n=new_word()
    '''message = '''
    await ctx.send("Word : "+n)
   # await client.add_reaction(message,':up1:749268799898779789')

@client.command(aliases=["mean","m"])
async def meaning(ctx):
    m=meaning2(word)
    await ctx.send("Meaning : "+m)
    



@client.command(aliases=["c","comp"])
async def Completed(ctx):
    for i in done_words:
        await ctx.send(i)

@client.command(aliases=["r","rem"])
async def remaining(ctx):
    itr=dct.keys().__iter__()
    while True:
        try:
            item=next(itr)
            if item not in done_words:
                await ctx.send(item)
        except:
            pass
            break# finish

@client.event
async def on_reaction_add(reaction,user):
    global rem_wd

    if reaction.emoji.id == 749258509769769000:
        rem_wd.add(reaction.message.content[7:])
   

client.run("NzQ5MjA2NDc4MDMxOTQ1ODUw.X0om5w.IEcYiagzS98cri7eeWx4loG7BeI")

# bot.py
import os
import random
import discord
from discord.utils import get

client = discord.Client()


def random_anger():
  x = ['leave him alone']
  return (random.choice(x))

def random_insult():
  verb = ['rekt']
  noun = ['scrub']
  return (f"Get {random.choice(verb)} {random.choice(noun)}")

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')




@client.event
async def on_message(message):
	# Check if the message sent to the channel is "hello".
  if message.content == '<@!391984323969941524>':
		# Sends a message to the channel.
    await message.channel.send(random_anger())
  
  if message.content == '!insult':
    await message.channel.send(random_insult())
    




client.run("ODg0NTI0NDk5MzkzOTg2NjIw.YTZvog.zDMmzJsDhZ05LSaTbqFJ1CFXlt8")

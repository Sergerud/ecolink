#Бот формирует связи типа отходов и переработчика
#отправляя команду с названием типа отходов (стекло, пластик, металл), мы получаем список его переработчиков и конечный продукт переработки
import discord
import requests
import os
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot('$', intents=intents)
@bot.event
async def on_ready():
    print(f'Зашли как {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def tgarb(ctx):
    img_name=random.choice(os.listdir("images"))
    with open(f'images/{img_name}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
        # Можем передавать файл как параметр!
        await ctx.send(file=picture)   
@bot.command('garbrec')
async def garbrec(ctx):
    fun=[get_fox_image_url(),get_duck_image_url(),get_dogs_image_url()]
    image_url = random.choice(fun)
    await ctx.send(image_url) 

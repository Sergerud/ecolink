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
    img_name=random.choice(os.listdir("garbage"))
    with open(f'garbage/{img_name}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
        # Можем передавать файл как параметр!
        print(f)
        await ctx.send(file=picture)   
@bot.command('all')
async def all(ctx):
    #fun=['$metal,$steklo,$plastik']
    #commands=(', '.join(fun))
    await ctx.send(f"Привет! Я бот EcoLink. Я умею находить переработчика отходов из Стекла - команда $steklo, Пластика - команда $plastik, Металла - команда $metal")
    #await ctx.send(commands) 
@bot.command('metal')
async def metal(ctx):
      with open(f'garbage/metal.jpg', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
        await ctx.send(file=picture)  
        await ctx.send(f"Металл")

bot.run('')    

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
    await ctx.send(f"Привет! Я бот EcoLink. Я умею находить переработчика отходов из:\n"
                   f"Стекла - команда $steklo,\n"
                   f"Пластика - команда $plastik,\n"
                   f"Металла - команда $metal,\n"
                   f"Бумаги - команда $paper,\n"
                   f"Строительных отходов - команда $stroi")
    #await ctx.send(commands) 
@bot.command('metal')
async def metal(ctx):
      with open(f'garbage/metal.jpg', 'rb') as f:
         # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
        await ctx.send(file=picture)  
        await ctx.send(f"Металл")
      with open(f'garbage/recyclers.txt', 'r', encoding='utf-8') as r:
          #content=r.read()
          for line in r:
            content=line
            if 'Металл' in content:
               url=content[7:len(content)] 
               break

          await ctx.send(url)
            
@bot.command('plastik')
async def plastik(ctx):
      with open(f'garbage/plastik.png', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
        await ctx.send(file=picture)  
        await ctx.send(f"Пластик")  
      with open(f'garbage/recyclers.txt', 'r', encoding='utf-8') as r:
        for line in r:
            content=line
            if 'Пластик' in content:
               url=content[8:len(content)] 
               break

        await ctx.send(url)  
@bot.command('steklo')
async def steklo(ctx):
      with open(f'garbage/steklo.jpg', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
        await ctx.send(file=picture)  
        await ctx.send(f"Стекло") 
      with open(f'garbage/recyclers.txt', 'r', encoding='utf-8') as r:
         for line in r:
            content=line
            if 'Стекло' in content:
                 url=content[7:len(content)] 
                 break

         await ctx.send(url)  
@bot.command('paper')
async def paper(ctx):
      with open(f'garbage/paper.jpg', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
        await ctx.send(file=picture)  
        await ctx.send(f"Бумага") 
      with open(f'garbage/recyclers.txt', 'r', encoding='utf-8') as r:
         for line in r:
            content=line
            if 'Бумага' in content:
                 url=content[7:len(content)] 
                 break

      await ctx.send(url)                    
@bot.command('stroi')
async def stroi(ctx):
      with open(f'garbage/stroi.jpg', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
        await ctx.send(file=picture)  
        await ctx.send(f"Строительные отходы")  
      with open(f'garbage/recyclers.txt', 'r', encoding='utf-8') as r:
         for line in r:
            content=line
            if 'Стройотходы' in content:
                 url=content[12:len(content)] 
                 break

         await ctx.send(url)                     

bot.run('')    

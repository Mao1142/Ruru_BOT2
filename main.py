import discord
from discord.ext import commands
import os
import keep_alive
import json
from core.jsonctrl import jFile

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
	print("---Bot is online---")




@bot.command()
async def load(ctx,extension): #load function
	bot.load_extension(f'cmds.{extension}')
	await ctx.send(f'Loaded {extension} done.')

@bot.command()
async def unload(ctx,extension): #unload function
	bot.unload_extension(f'cmds.{extension}')
	await ctx.send(f'Unloaded {extension} done.')

@bot.command()
async def reload(ctx,extension): #reload function
	bot.reload_extension(f'cmds.{extension}')
	await ctx.send(f'Reloaded {extension} done.')

'''
@bot.command()
async def help(ctx):
  embed = discord.Embed(title="Ruru bot", description=". List of commands are:", color=0xeee657)
  embed.add_field(name="Basic", value="通用指令", inline=False)
  embed.add_field(name="/help", value="Gives this message", inline=False)
  embed.add_field(name="/ping", value="回傳BOT延遲", inline=False)
  embed.add_field(name="/advice", value="傳送建議表格連結", inline=False)
  embed.add_field(name="/konruru", value="空嚕嚕", inline=False)

  embed.add_field(name="Picture", value="圖片指令", inline=False)
  embed.add_field(name="/dan", value="隨機從Danbooru發一張圖", inline=False)
  embed.add_field(name="/yan", value="隨機從yande發一張圖", inline=False)
  embed.add_field(name="/gel", value="隨機從Gelbooru發一張圖", inline=False)
  embed.add_field(name="/san", value="隨機從sankakucomplex發一張圖", inline=False)
  embed.add_field(name="/pic", value="隨機從以上圖源發一張圖", inline=False)

  embed.add_field(name="Chat", value="對話設定", inline=False)
  embed.add_field(name="/addchat", value="增加對話 /addchat **Key** **react**", inline=False)
  embed.add_field(name="/editchat", value="編輯已存在對話 /editchat **Key** **react**", inline=False)
  embed.add_field(name="/delchat", value="刪除對話 /delchat **Key**", inline=False)
  embed.add_field(name="/listchat", value="列出已儲存的對話清單", inline=False)

  await ctx.send(embed=embed)
'''

for Filename in os.listdir('./cmds'):
	if Filename.endswith('.py'):
 		bot.load_extension(f'cmds.{Filename[:-3]}')

if  __name__ == "__main__":
  keep_alive.keep_alive()
  bot.run(jFile.secure.get('Token'))
  bot.remove_command('help')







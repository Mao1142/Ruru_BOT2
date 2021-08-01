import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json
from core.jsonctrl import jFile
import requests

class React(Cog_Extension):

    @commands.command()
    async def pic(self,ctx):
	    await ctx.send(SelectUrl('PicSource'))

    @commands.command()
    async def san(self,ctx):
	    await ctx.send(SelectUrl('sankaku'))

    @commands.command()
    async def yan(self,ctx):
	    await ctx.send(SelectUrl('yande'))

    @commands.command()
    async def gel(self,ctx):
	    await ctx.send(SelectUrl('gelbooru'))

    @commands.command()
    async def dan(self,ctx):
	    await ctx.send(SelectUrl('danbooru'))
    
    @commands.command()
    async def konruru(self,ctx):
	    await ctx.send('空嚕嚕')
    
    @commands.command()
    async def speak(self,ctx,msg):
      self.channel = self.bot.get_channel(int(jFile.secure.get('DragonPort_Ch')))
      await self.channel.send(f'{msg}')


#Chat相關
    @commands.command()
    async def addchat(self,ctx,name,msg):
      #print(name,msg)
      #檢查重複
      if jFile.chat.CheckRepeat(name) :
        jFile.chat.setData(name,msg)  
        await ctx.send(f'增加 關鍵字:{name} , 回應:{msg}')
      else :
        await ctx.send(f'關鍵字:{name} 重複')

    @commands.command()
    async def editchat(self,ctx,name,msg):
      if jFile.chat.CheckRepeat(name) :
        jFile.chat.setData(name,msg)  
        await ctx.send(f'關鍵字不存在，已增加 關鍵字:{name} , 回應:{msg}')
      else :
        jFile.chat.setData(name,msg) 
        await ctx.send(f'已將關鍵字:{name} , 回應更改為:{msg}')

    @commands.command()
    async def delchat(self,ctx,name):
      if jFile.chat.CheckRepeat(name) :
        await ctx.send(f'關鍵字不存在')
      else :
        jFile.chat.DeleteData(name)
        await ctx.send(f'已將關鍵字 {name} 刪除')
    
    @commands.command()
    async def listchat(self,ctx):
      await ctx.send(embed = FormatAllChat())

    @commands.command()
    async def advice(self,ctx):
	    await ctx.send(jFile.setting.get('advice_table'))
      
    @commands.command()
    async def test(self,ctx):
      with open('json/chat.json','r',encoding='utf8') as f:
        data = json.load(f)
      print(data)


#綜合
def FormatAllChat():
  embed = discord.Embed(title="對話清單", description="List of chat are:", color=0xeee657)
  data = jFile.chat.getAll()
  for tmp in data:
    embed.add_field(name=f"\nQ: {tmp}", value=f"A: {data[f'{tmp}']}", inline=False)
  return embed
    
def SelectUrl(source):
  max = random.choice(jFile.setting.get(source)) + "_max"
  return jFile.setting.get(source) + str(random.randint(1,int(jFile.setting.get(max))))

def setup(bot):
    bot.add_cog(React(bot))
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json
from core.jsonctrl import jFile
import requests
from bs4 import BeautifulSoup

class React(Cog_Extension):

    @commands.command()
    async def pic(self,ctx):
	    await ctx.send(SelectUrl())

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
      url = SelectUrl()
      print(url)
      resp = requests.get(url)  
      #print(resp) #<Response [200]> 請求成功回200，請求失敗回404
      #透過BeautiFul整理且用html.parser解析
      soup = BeautifulSoup(resp.text, 'html.parser')
      result = soup.find("section",id = "content")
      picurl = result.select_one("a").get("href")
      await ctx.send(picurl)


#綜合
def FormatAllChat():
  embed = discord.Embed(title="對話清單", description="List of chat are:", color=0xeee657)
  data = jFile.chat.getAll()
  for tmp in data:
    embed.add_field(name=f"\nQ: {tmp}", value=f"A: {data[f'{tmp}']}", inline=False)
  return embed
    
def SelectUrl():
  source = random.choice(jFile.setting.get('PicSource'))
  return jFile.setting.get(source) + str(random.randint(1,int(jFile.setting.get(source + "_max"))))

def setup(bot):
    bot.add_cog(React(bot))
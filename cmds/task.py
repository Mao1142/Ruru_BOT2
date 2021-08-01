import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json,asyncio,datetime
import random 
from core.jsonctrl import jFile



class Task(Cog_Extension):
  def __init__(self,*args,**kwargs):
    super().__init__(*args,**kwargs)
    
    self.counter = 0
    async def interval():
      await self.bot.wait_until_ready()
      self.channel = self.bot.get_channel(int(jFile.secure.get('DragonPort_Ch')))
      while not self.bot.is_closed():
        now_time = datetime.datetime.now().strftime('%H%M')
        #print(now_time)
        if now_time == '0400' and self.counter == 0:
          await self.channel.send(f'<:02:866251238260736021>'+jFile.setting.get('konruru'))
          self.counter = 1
        elif now_time == '1300' and self.counter == 0:
          await self.channel.send(jFile.setting.get('otsururu'))
          self.counter = 1
        else :
          self.counter = 0       
        await asyncio.sleep(35)

    self.bg_task = self.bot.loop.create_task(interval())    


@commands.command()
async def set_channel(self,ctx,ch:int):
  self.Channel = self.bot.get_channel(ch)
  await ctx.send(f'Set Channel : {self.channel.mention}')


def setup(bot):
  bot.add_cog(Task(bot))

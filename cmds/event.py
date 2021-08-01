import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

from core.jsonctrl import jFile


class Event(Cog_Extension):
    count = 0

    @commands.Cog.listener()
    async def on_member_join(self,member):
	    print(f'{member} join')
	    channel = self.bot.get_all_channels(int(jFile.secure.get('DragonPort_Ch')))
	    await channel.send(f"{member} join,{jFile.setting.get('konruru')}")

    @commands.Cog.listener()
    async def on_member_remove(self,member):
	    print(f'{member} leave')
	    channel = self.ot.get_all_channels(int(jFile.secure.get('DragonPort_Ch')))
	    await channel.send(f"{member} leave,{jFile.setting.get('otsururu')}")

    @commands.Cog.listener()
    async def on_message(self,msg):
        #print(f'{msg.channel}')
        if msg.author != self.bot.user :
          #special chat
          if msg.content == "<:MH_M6:710036622036566078>" :
            if Event.count >= 2 :
              Event.count = 0
              await msg.channel.send("<:01:866251238647791666>")
            else :
              Event.count = Event.count + 1
          elif msg.content ==   "<:GS_Ganyu2:803303747983900682>" or msg.content == "<:GI_Keqing1:790752573832953937>":
            await msg.channel.send(jFile.setting.get('otsururu'))
            await msg.channel.send(jFile.setting.get('Ruru_sleep')) 
          #normal chat 
          else :
            data = jFile.chat.getAll()
            for temp in data:
              if msg.content == temp :
                await msg.channel.send(data[f'{temp}'])


def setup(bot):
     bot.add_cog(Event(bot))
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import requests

class jFile(Cog_Extension):
  def get(filename,key =  ''):
    with open(f'json/{filename}.json','r',encoding='utf8') as f:
        data = json.load(f)
    if key == '':
      return data
    return data[key]
  
  def set(filename,key,data):
    L = {f"{key}":f"{data}"}
    with open(f'json/{filename}.json','r',encoding='utf8') as f:
      old_data = json.load(f)
    old_data.update(L)
    with open(f'json/{filename}.json','w',encoding='utf8') as f:
      json.dump(old_data,f,indent=4)
    f.close()
  
  class secure():
    def get(key):
      return jFile.get('secure',key)

  class setting():
    def get(key):
      return jFile.get('setting',key)

    def set(key,data):
      jFile.set('setting',key,data)

  class chat():
    def getAll():
      response = requests.get(
        jFile.get('secure','DataBaseUrl')
      )
      return response.json()

    def putAll(rData):
      requests.put(
        jFile.get('secure','DataBaseUrl'),
        json = rData
      )

    def getData(key):
      rData = jFile.chat.getAll()
      return rData[key]
    
    def setData(key,data):
      rData = jFile.chat.getAll()
      rData[key] = data
      jFile.chat.putAll(rData)
    
    def CheckRepeat(name):
      rData = jFile.chat.getAll()
      for tmp in rData:
        if name == tmp :
          return False
      return True
    
    def DeleteData(name):
      rData = jFile.chat.getAll()
      rData.pop(name)
      jFile.chat.putAll(rData)

  class post():
    def get(key = ''):
      return jFile.get('post',key)

    def set(key,data):
        return jFile.set('post',key,data)
    
    def delete(key):
      old_data = jFile.get('post')
      old_data.pop(key)
      with open(f'json/post.json','w',encoding='utf8') as f:
        json.dump(old_data,f,indent=4)
      f.close()



def setup(bot):
     bot.add_cog(jFile(bot))

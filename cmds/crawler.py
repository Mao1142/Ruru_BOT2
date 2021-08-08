import discord
from discord.ext import commands
from core.classes import Cog_Extension
import requests
from bs4 import BeautifulSoup
import random

class error:
  TagNotFound = "るる找不到這個Tag，請檢查有無錯字或底線"

class crawler(Cog_Extension):
  def getDan(tag = ''):
    try:
      url = "https://danbooru.donmai.us/"
      if tag !='' : 
        url = f"https://danbooru.donmai.us/posts?tags={tag}"
      response = requests.get(url)
      soup = BeautifulSoup(response.text, "html.parser")
      results = soup.find('div',id ='posts-container').find_all('a',limit=22)
      source ="https://danbooru.donmai.us/" + random.choice(results).get('href')
      response = requests.get(source)
      soup = BeautifulSoup(response.text, "html.parser")
      results = soup.find('picture').find_all('img',class_ = 'fit-width')
      #print(results[0].get('src'))
      return random.choice(results).get('src')
    except:
      return error.TagNotFound
  
  def getYan(tag = ""):
    try:
      url = "https://yande.re/post"
      if tag !='' : 
        url = f"https://yande.re/post?tags={tag}"
      response = requests.get(url)
      soup = BeautifulSoup(response.text, "html.parser")

      results = random.choice(soup.find_all('a', class_ ='thumb') )
      link = ('https://yande.re/' + results.get('href'))

      response = requests.get(link)
      soup = BeautifulSoup(response.text, "html.parser")
      results = soup.find("div",class_='content').find('img').get("src")
      #print(results)
      return results
    except:
      return error.TagNotFound
    
  def getGel(tag = 'all'):
    try:
      url = f"https://gelbooru.com/index.php?page=post&s=list&tags={tag}"
      response = requests.get(url)
      soup = BeautifulSoup(response.text, "html.parser")
      results = soup.find('div',class_ ='thumbnail-container').find_all('a', limit=40)
      random.choice(results)
      url = random.choice(results).get('href')
      response = requests.get(url)
      soup = BeautifulSoup(response.text, "html.parser")
      picurl = soup.find_all('img',id = "image")[0].get("src")
      print(picurl)
      return picurl
    except:
      return error.TagNotFound

def setup(bot):
     bot.add_cog(crawler(bot))

from core.classes import Cog_Extension
import requests
from bs4 import BeautifulSoup

class crawler(Cog_Extension):
  def getDan(url):
    resp = requests.get(url)  
    soup = BeautifulSoup(resp.text, 'html.parser')
    result = soup.find_all("section")
    print(result)
    for tmp in result:
      picurl = result.select_one("a").get("href")
      print(picurl)
    #return picurl
  
  def getYan(url):
    resp = requests.get(url)  
    soup = BeautifulSoup(resp.text, 'html.parser')
    result = soup.find("section",id = "content")
    picurl = result.select("a").get("href")
    return picurl
    
  def getGel(url):
    soup = BeautifulSoup(requests.get(url) .text, 'html.parser')
    result = soup.find("section",rel = "image_src").get("href")
    return result.select_one("img").get("src")

def setup(bot):
     bot.add_cog(crawler(bot))

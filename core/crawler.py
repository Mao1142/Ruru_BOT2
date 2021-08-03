import json
from core.jsonctrl import jFile
import requests
from bs4 import BeautifulSoup

class crawler():
  def getDan(url):
    resp = requests.get(url)  
    soup = BeautifulSoup(resp.text, 'html.parser')
    result = soup.find("section",id = "content")
    picurl = result.select_one("a").get("href")
    return picurl
  
  def getYan(url):
    soup = BeautifulSoup(requests.get(url) .text, 'html.parser')
    result = soup.find("link",rel = "image_src")
    print(result)
    #picurl = result.select_one("link").get("href")
    #print(picurl)
    #return picurl
    
  def getGel(url):
    soup = BeautifulSoup(requests.get(url) .text, 'html.parser')
    result = soup.find("section",rel = "image_src").get("href")
    return result.select_one("img").get("src")
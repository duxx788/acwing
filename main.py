import requests
import window
from bs4 import BeautifulSoup
import re

url = 'https://www.acwing.com/activity/content/31/'



headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
"Cookie": ""
}

r = requests.get(url,headers=headers)
with open("acwing.html","w",encoding="utf-8") as f:
    f.write(r.content.decode())


url = 'https://www.acwing.com'
soup  = BeautifulSoup(open('acwing.html',encoding='utf-8'))
labels = soup.find_all('a',class_="clock-problem-title" )
dict={}
with open('links.txt','w',encoding='utf-8') as f:
    max = 0
    for label in labels:
        # print(url+label['href'])
        link = url + label['href']
        span = label.find('span')
        name = span.text
        left = name.find(' ')
        right = name.rfind('.')
        name = name[left+1:right]
        #print(name +'--'+link )
        f.write(name+' '+link+'\n')


window.acwing()
import requests
from bs4 import BeautifulSoup
from wallpaper import set_wallpaper

response=requests.get('https://commons.wikimedia.org/wiki/Main_Page')
print(response.status_code)
if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')
src=response.content
soup = BeautifulSoup(src,'lxml')
ss=soup.find('div',{'id':'mf-picture-picture','class':'mainpage-box-content'})
print(ss.a['href'])
url="https://commons.wikimedia.org{}".format(ss.a['href'])
imagepage=requests.get(url)
imgsoup = BeautifulSoup(imagepage.content,'lxml')
imgurl=imgsoup.find('a',string="Original file")['href']
with open('wall.jpg','wb') as handle:
    response = requests.get(imgurl).content
    handle.write(response)
set_wallpaper("wall.jpg")
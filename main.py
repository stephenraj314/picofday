import requests
from bs4 import BeautifulSoup
from wallpaper import set_wallpaper

response=requests.get('https://commons.wikimedia.org/wiki/Main_Page')
# Checking website status
if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Page Not Found.')
src=response.content
soup = BeautifulSoup(src,'lxml')
# finding src of pic of the day image
ss=soup.find('div',{'id':'mf-picture-picture','class':'mainpage-box-content'})
url="https://commons.wikimedia.org{}".format(ss.a['href'])
imagepage=requests.get(url)
imgsoup = BeautifulSoup(imagepage.content,'lxml')
# getting image url for original file source
imgurl=imgsoup.find('a',string="Original file")['href']
# downloading image file
with open('wall.jpg','wb') as handle:
    response = requests.get(imgurl).content
    handle.write(response)
# setting image file as desktop wallpaper
set_wallpaper("wall.jpg")
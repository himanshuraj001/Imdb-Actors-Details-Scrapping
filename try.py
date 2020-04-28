import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = "https://www.imdb.com/list/ls073080798/"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup.find_all(class_="lister-item-header")
artist_list = []
for i in tags:
    lis = i.find_all("a")
    lis = str(lis)
    b = re.findall('"> (.+)\n', lis)
    artist_list.append(b[0])
link_list = []
for j in tags:
    link = j.find_all("a")
    link = str(link)
    c = re.findall('href="(.+)">', link)
    link_list.append(c[0])


def image_link(number):
    url_image = "https://www.imdb.com" + link_list[number] + "/bio?ref_=nm_ov_bio_sm"
    html4 = urlopen(url_image, context=ctx).read()
    soup4 = BeautifulSoup(html4, "html.parser")
    image1 = soup4.find_all(class_="article listo")
    for s in image1:
        image2 = s.find_all("img")
        image3 = image2[0].get("src")
    return image3

for i in range(len(artist_list)):
    filename = str(artist_list[i])
    with open('img\\'+filename + ".jpg" , "wb") as a:
        a.write(urllib.request.urlopen(image_link(i)).read())

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


def movie_list(number):
    url_movie = "https://www.imdb.com" + link_list[number] + "/?ref_=nmls_hd"
    html2 = urlopen(url_movie, context=ctx).read()
    soup2 = BeautifulSoup(html2, "html.parser")
    tags2 = soup2.find_all(class_="filmo-category-section")
    a = tags2[0]
    lis2 = []
    m_list = []
    for k in a:
        if k != "\n":
            m = str(k)
            d = re.findall('(\(.+\))\n', m)
            if len(d) == 0:
                lis2.append(k)
    for f in lis2:
        x = f.find("a")
        y = f.find("span")
        mn = str(y)
        z = re.findall('([0-9*])', mn)
        t = []
        k = ''
        for j in z:
            j = j.lstrip()
            k = k + j
        t.append(k)
        abc = str(x)
        ab = re.findall('">(.+)<', abc)
        m_list.append([ab[0], *t])
    return m_list
def introduction(number):
    url_intro = "https://www.imdb.com" + link_list[number] + "/bio?ref_=nm_ov_bio_sm"
    html3 = urlopen(url_intro, context=ctx).read()
    soup3 = BeautifulSoup(html3, "html.parser")
    intro = []
    intro2 = []
    intro3 = []

    x = soup3.find_all(class_="soda odd")
    tag3 = x[0].find_all("p")
    for h in tag3:
        intro.append(h)
    intro2.append(intro[0])
    for f in intro2:
        for h in f:
            h = str(h)
            h.rstrip()
            a = re.findall('(<.+?>)', h)
            if len(a) == 0:
                intro3.append(h)
            elif len(a) == 2:
                b1 = re.findall('>(.+)<', h)
                intro3.append(b1[0])
            k = ''
            for i in intro3:
                i = i.lstrip()
                k = k + i
    return k


for i in range(len(artist_list)):
    fname = str(artist_list[i])
    with open("p\\"+fname+".txt",'a+') as b:
        b.write(artist_list[i])
        b.write("\n")
        b.write("link for introduction and image -- ")
        b.write("https://www.imdb.com" + link_list[i] + "/bio?ref_=nm_ov_bio_sm")
        b.write("\n")
        b.write("link for movie list -- " + "https://www.imdb.com" + link_list[i] + "/?ref_=nmls_hd")
        b.write("\n")
        b.write("INTRODUCTION-----\n\n")
        b.write(introduction(i))
        b.write("\n\n\n")
        b.write("MOVIE LIST\n")
        for k in movie_list(i):
            b.write(k[0]+','+ k[1])
            b.write("\n")





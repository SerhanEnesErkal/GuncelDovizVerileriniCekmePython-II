import requests
from bs4 import BeautifulSoup

url = "https://bigpara.hurriyet.com.tr/doviz/dolar/"
response = requests.get(url)
html_icerigi = response.content
soup = BeautifulSoup(html_icerigi,"html.parser")

isim =soup.find_all("h1",{"class":"pageTitle mBot10 pageTitleDoviz"})
kur= soup.find_all("span",{"class":"value up"})

liste = list()

for i in range(len(isim)):
    isim[i] = (isim[i].text).strip("\n").strip()
    kur[i] = (kur[i].text).strip("\n").replace("\nTL"," TL").strip()
    liste.append([isim[i],kur[i]])


print(liste)

url = "https://bigpara.hurriyet.com.tr/doviz/euro/"
response = requests.get(url)
html_icerigi = response.content
soup = BeautifulSoup(html_icerigi,"html.parser")

isim =soup.find_all("h1",{"class":"pageTitle mBot10 pageTitleDoviz"})
kur= soup.find_all("span",{"class":"value up"})

liste = list()

for i in range(len(isim)):
    isim[i] = (isim[i].text).strip("\n").strip()
    kur[i] = (kur[i].text).strip("\n").strip()
    liste.append([isim[i],kur[i]])

print(liste)

url = "https://uzmanpara.milliyet.com.tr/gram-altin-fiyati/"
response = requests.get(url)
html_icerigi = response.content
soup = BeautifulSoup(html_icerigi,"html.parser")

isim =soup.find_all("span",{"style":"margin-top: 6px !important;display: flex;"})
kur= soup.find_all("span",{"class":"yesilBold"})

liste1 = list()

for i in range(len(isim)):
    isim[i] = (isim[i].text).strip("\n").strip()
    kur[i] = (kur[i].text).strip("\n").strip()
    liste1.append([isim[i],kur[i]])

print(liste1)

url = "https://finans.mynet.com/borsa/"
response = requests.get(url)
html_icerigi = response.content
soup = BeautifulSoup(html_icerigi,"html.parser")

isim =soup.find_all("h1",{"class":"mr-3"})
kur= soup.find_all("span",{"class":"dynamic-price-XU100"})

liste = list()

for i in range(len(isim)):
    isim[i] = (isim[i].text).strip("\n").strip()
    kur[i] = (kur[i].text).strip("\n").strip()
    liste.append([isim[i],kur[i]])

print(liste)
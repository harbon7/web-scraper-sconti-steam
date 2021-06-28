import bs4, requests, webbrowser

LINK = "https://store.steampowered.com/specials/"
PRE_LINK_GIOCO = "https://store.steampowered.com/app/"

response = requests.get(LINK)
response.raise_for_status()
soup=bs4.BeautifulSoup(response.text, "html.parser")
div_giochi=soup.find("div", class_="tabarea")
a_giochi=div_giochi.find_all("a")
link_giochi = []
for a_gioco in a_giochi:
    link_gioco = str(a_gioco.get("href"))
    if PRE_LINK_GIOCO in link_gioco:
        link_giochi.append(link_gioco)
from pprint import pprint
pprint(link_giochi)
				
f = open("risultati_salvati.txt", "a")
old_link_giochi = [riga.rstrip("\n") for riga in open("risultati_salvati.txt")]
new_link_giochi = []
for link_gioco in link_giochi:
    if link_gioco not in old_link_giochi:
        new_link_giochi.append(link_gioco)
        f.write("%s\n" % link_gioco)
f.close()
if new_link_giochi:
    print("Ci sono nuovi sconti! Apertura in corso...")
    for new_link in new_link_annunci:
        webbrowser.open(new_link)
else:
    print("Nessun nuovo annuncio.")

input("\n Tutto bene!!!")

#fatto da harbon
#discord: harbon2222
#github: harbon7

#MIT License copyright

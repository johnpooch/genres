from django.shortcuts import render, redirect

import bs4 as bs
from urllib.request import urlopen
import string
import random

url_list = [
    "https://en.wikipedia.org/wiki/The_Beatles", 
    "https://en.wikipedia.org/wiki/Nirvana_(band)", 
    "https://en.wikipedia.org/wiki/Queens_of_the_Stone_Age",
    "https://en.wikipedia.org/wiki/Led_Zeppelin",
    "https://en.wikipedia.org/wiki/Arctic_Monkeys",
    "https://en.wikipedia.org/wiki/Queen_(band)",
    "https://en.wikipedia.org/wiki/Sex_Pistols",
    "https://en.wikipedia.org/wiki/The_Fall_(band)",
    "https://en.wikipedia.org/wiki/Gorillaz",
    "https://en.wikipedia.org/wiki/Metallica",
    ]
    
def scrape_band_from_wiki():
    sauce = urlopen(random.choice(url_list)).read()

    soup = bs.BeautifulSoup(sauce, 'lxml')
    band_name = soup.find('h1')
    
    covers = soup.select('table.infobox a.image img[src]')
    for cover in covers:
        cover_link = cover['src'] 
    
    table = soup.find('table', class_='infobox')
    table_rows = table.find_all('tr')
    for tr in table_rows:
        table_header = tr.find_all('th')
        for th in table_header:
            if th.text == "Genres":
                genre_row = tr
    
    genres = [i.text for i in genre_row.find_all('a')]
    return {"band_name": band_name.text, "cover_link": cover_link, "genres": genres}

def get_index(request): 
    band_dictionary = scrape_band_from_wiki()
    return render(request, "home/index.html", band_dictionary)
    

def check_answer(request): 
    print(request.GET['answer[0]'])
    print(request.GET['right_answer[0]'])

    return redirect("/")
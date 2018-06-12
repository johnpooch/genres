from django.shortcuts import render

import bs4 as bs
from urllib.request import urlopen
import string
import random

def get_index(request): 
    
    # valid_list_elements = []

    # sauce = urlopen("https://en.wikipedia.org/wiki/List_of_alternative_rock_artists").read()
    # soup = bs.BeautifulSoup(sauce, 'lxml')
    
    # div = soup.find_all('div', {'class':['div-col', 'columns', 'column-width']})
    # for div in div:
    #     li = div.find_all('li')
    #     for li in li: 
    #         print(li.string)
    #         if(li.string != 'None'):
    #             for a in li.find_all('a', href=True):
    #                 print (a['href'])


    # sauce = urlopen("https://en.wikipedia.org/wiki/The_Beatles").read()
    sauce = urlopen("https://en.wikipedia.org/wiki/Nirvana_(band)").read()
    # sauce = urlopen("https://en.wikipedia.org/wiki/Queens_of_the_Stone_Age").read()
    # sauce = urlopen("https://en.wikipedia.org/wiki/Kyuss").read()
    
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
    
    print(band_name.text)
    print(cover_link)
    print(genres)
    
    return render(request, "home/index.html", {"band_name": band_name.text, "cover_link": cover_link, "genres": genres})
from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
import sys

data_club = {

    0 : {
        "name" : "Pal",
        "url" : "https://fbref.com/pt/equipes/abdce579/2022/partidas/c24/schedule/Palmeiras-Resultados-e-Calendarios-Serie-A",
    },

    1 : {
        "name" : "Fla",
        "url" : "https://fbref.com/pt/equipes/639950ae/2022/partidas/c24/schedule/Flamengo-Resultados-e-Calendarios-Serie-A",
    },

    2 : {
        "name" : "Int",
        "url" : "https://fbref.com/pt/equipes/6f7e1f03/2022/partidas/c24/schedule/Internacional-Resultados-e-Calendarios-Serie-A",
    },

    3 : {
        "name" : "Atm",
        "url" : "https://fbref.com/pt/equipes/422bb734/2022/partidas/c24/schedule/Atletico-Mineiro-Resultados-e-Calendarios-Serie-A",
    },

    4 : {
        "name" : "For",
        "url" : "https://fbref.com/pt/equipes/a9d0ab0e/2022/partidas/c24/schedule/Fortaleza-Resultados-e-Calendarios-Serie-A",
    },

    5 : {
        "name" : "San",
        "url" : "https://fbref.com/pt/equipes/712c528f/2022/partidas/c24/schedule/Santos-Resultados-e-Calendarios-Serie-A",
    },

    6 : {
        "name" : "Bra",
        "url" : "https://fbref.com/pt/equipes/f98930d1/2022/partidas/c24/schedule/Bragantino-Resultados-e-Calendarios-Serie-A",
    },
}


def extractDataFromSite( data_club, name_club ): 

    counter: int = 0
    openUrl = urlopen( f"{data_club}" )
    soup = BeautifulSoup( openUrl.read(), 'html.parser' )
    data_from_site = soup.select( f"#matchlogs_for > tbody > tr > td:nth-child(6)" )
    len_data = len( data_from_site )

    with open('monitor.txt', 'a', encoding='utf-8') as file:
        file.write(name_club + ";")
        file.write("\n")

    for i in range( len_data ):
        try:
            if data_from_site[counter].contents[0] == "V":
                result = "3"
            elif data_from_site[counter].contents[0] == "D":
                result = "-3"
            else:
                result = "0"

            with open('monitor.txt', 'a', encoding='utf-8') as file:
                file.writelines(result + ";")
                
            counter += 1

        except IndexError:
            break

    with open('monitor.txt', 'a', encoding='utf-8') as file:
        file.write("\n")

counter = 0
for i in range(len(data_club)):
    extractDataFromSite( data_club[counter]["url"], data_club[counter]["name"] )
    counter += 1

sys.exit()









from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

data_club = {

    0 : {
        "name" : "Palmeiras",
        "url" : "https://fbref.com/pt/equipes/abdce579/2022/partidas/c24/schedule/Palmeiras-Resultados-e-Calendarios-Serie-A",
    },

    1 : {
        "name" : "Flamengo",
        "url" : "https://fbref.com/pt/equipes/639950ae/2022/partidas/c24/schedule/Flamengo-Resultados-e-Calendarios-Serie-A",
    },

    2 : {
        "name" : "Internacional",
        "url" : "https://fbref.com/pt/equipes/6f7e1f03/2022/partidas/c24/schedule/Internacional-Resultados-e-Calendarios-Serie-A",
    },
}

def extractDataFromSite( data_club, name_club ): 

    counter: int = 0
    openUrl = urlopen( f"{data_club}" )
    soup = BeautifulSoup( openUrl.read(), 'html.parser' )
    data_from_site = soup.select( f"#matchlogs_for > tbody > tr > td:nth-child(6)" )
    len_data = len( data_from_site )

    with open('monitor.csv', 'a', newline='', encoding='utf-8') as file:
        w = csv.writer( file )
        w.writerow( [","] + [name_club] )

    for i in range( len_data ):
        try:
            result = data_from_site[counter].contents[0]

            with open('monitor.csv', 'a', newline='', encoding='utf-8') as file:
                w = csv.writer( file )
                w.writerow( [result] )
                
            counter += 1

        except IndexError:
            break

       

extractDataFromSite( data_club[0]["url"], data_club[0]["name"] )
extractDataFromSite( data_club[1]["url"], data_club[1]["name"] )
extractDataFromSite( data_club[2]["url"], data_club[2]["name"] )











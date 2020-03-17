from basketball_reference_web_scraper import client
import basketball_reference_web_scraper.data as data
from pprint import pprint

from pprint import pprint
from pandas import DataFrame

def main():
    df = DataFrame()
    columns = []
    for x in client.players_advanced_season_totals(2020)[0]:
        columns.append(x)

    df.rename(columns = columns)
    for x in (client.players_advanced_season_totals(season_end_year=2020)):
        for y in dict(x):
            print (y.value)
            pprint("asa")

    

if __name__ == "__main__":                     
    main()





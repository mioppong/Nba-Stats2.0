from basketball_reference_web_scraper import client
import basketball_reference_web_scraper.data as data
from pprint import pprint

from pprint import pprint
from pandas import DataFrame

def main():
    avg_20_plus()
    

def avg_20_plus():
   
    for x in (client.players_season_totals(season_end_year=2020)):
        games_played = int(x['games_played'])
        points = int(x['points'])
        avg_points =  round(points/games_played, 2)   
        
        if( avg_points > 20):

            print(x['name'])
            print("avg_points is", str(avg_points))
            print(" ")

if __name__ == "__main__":                     
    main()





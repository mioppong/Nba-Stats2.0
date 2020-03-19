from basketball_reference_web_scraper import client
import basketball_reference_web_scraper.data as data
from pprint import pprint
import operator
from pprint import pprint
from pandas import DataFrame
import matplotlib.pyplot as plt

def main():
    #avg_20_plus()
    #avg_20_plus_mins()
    #points_per_minutes()
    #under_20_avg_20_plus()
    #plot_3_pct_vs_points()
    usage_vs_points()

    

def avg_20_plus():
    for x in (client.players_season_totals(season_end_year=2020)):
        games_played = int(x['games_played'])
        points = int(x['points'])
        avg_points =  round(points/games_played, 2)   

        if( avg_points > 20):
            print(x['name'],"avg_points is", str(avg_points))


def avg_20_plus_mins():
    for x in (client.players_season_totals(season_end_year=2020)):
        minutes_played = x["minutes_played"]
        games_played = x['games_played']
        avg_minutes_played = round(minutes_played/games_played,2)
        
        if(avg_minutes_played > 20):
            print(x['name'], avg_minutes_played)

def points_per_minutes():
    answer_dict = {}
    for x in (client.players_season_totals(season_end_year=2020)):
        minutes_played = x['minutes_played']
        total_points = x['points']
        avg_points_per_min = round(total_points/minutes_played,2)

        answer_dict[x['name']] = avg_points_per_min
    sorted_answer = sorted(answer_dict.items(),key=operator.itemgetter(1))
    
    pprint("is points per minute")
    pprint(sorted_answer)
    pprint("is points per minute")

#this method prints players 20 years or 
# younger averaging more than 20 pts
def under_20_avg_20_plus():
    #we put the answer in a dictionary, because we want to sort it
    answer_dict = {}
    for x in (client.players_season_totals(season_end_year=2020)):
        age = x['age']
        points = x['points']
        games_played = x['games_played']
        avg_points = round(points/games_played,2)
        
        if(age<=20 and avg_points >=20):
            answer_dict[x['name']] = avg_points
        
    pprint(answer_dict)

def plot_3_pct_vs_points():
    df = DataFrame()
    df_3s = DataFrame()

    for x in (client.players_season_totals(season_end_year=2019)):
        df = df.append(DataFrame(x),ignore_index=True)
    
    df['3_pct'] = df['made_three_point_field_goals']/ df['attempted_three_point_field_goals']
    df['avg_points'] = df['points']/ df['games_played']
    #df_temp = DataFrame(1,2)
    #df = df.append(df_temp)
    #df.plot(x='turnovers',y='points')
    df.plot(x = '3_pct',y ='avg_points',kind='scatter')
    plt.show()

def usage_vs_points():
    df = DataFrame()
    for x in (client.players_advanced_season_totals(season_end_year=2020)):
        df = df.append(DataFrame(x),ignore_index=True)
    print(df.columns)
    #df['avg_points'] = df['points']/df['games_played']



if __name__ == "__main__":                     
    main()





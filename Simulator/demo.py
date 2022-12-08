from lxml import html
import requests
import pandas as pd


# home_page = requests.get(
# 		"https://www.baseball-reference.com/teams/" + abbrs["home"]  + "/" + years["home"] + "-schedule-scores" + ".shtml"
# 	)

#home_link=str("https://www.baseball-reference.com/teams/" + abbrs["home"]  + "/" + years["home"] + "-schedule-scores" + ".shtml#team_schedule")
home_link=str("https://www.baseball-reference.com/teams/" + "NYY"  + "/" + "2016" + "-schedule-scores" + ".shtml#team_schedule")
home_pd=pd.read_html(home_link)[0]
#print(type(home_pd))
# home_pd[(home_pd["Tm"]==abbrs["home"]) & (home_pd["Opp"]==abbrs["away"])]
#print(home_pd[(home_pd['Tm']=='NYY') & (home_pd['Opp']=='BOS')])
num_games=home_pd[(home_pd['Tm']=='NYY') & (home_pd['Opp']=='BOS')].shape[0]
print(num_games)
num_home_wins=home_pd[(home_pd['Tm']=='NYY') & (home_pd['Opp']=='BOS')].loc[home_pd['W/L'].str.contains('W',case=True)].shape[0]
print(num_home_wins)

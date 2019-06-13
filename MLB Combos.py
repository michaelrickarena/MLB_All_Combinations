import itertools
import csv



k=10
s={'Cavan Biggio (12796468)': {'cost': 3800, 'position': '2B', 'team': 'TOR'}, 'Vladimir Guerrero Jr. (12796394)': {'cost': 4200, 'position': '3B', 'team': 'TOR'}, 'Lourdes Gurriel Jr. (12796372)': {'cost': 4500, 'position': '2B', 'team': 'TOR'}, 'Randal Grichuk (12796396)': {'cost': 4200, 'position': 'OF', 'team': 'TOR'}, 'Justin Smoak (12796360)': {'cost': 4800, 'position': '1B', 'team': 'TOR'}, 'Teoscar Hernandez (12796467)': {'cost': 3800, 'position': 'OF', 'team': 'TOR'}, 'Rowdy Tellez (12796541)': {'cost': 3500, 'position': '1B', 'team': 'TOR'}, 'Freddy Galvis (12796434)': {'cost': 4000, 'position': 'SS', 'team': 'TOR'}, 'Luke Maile (12796801)': {'cost': 2700, 'position': 'C', 'team': 'TOR'}, 'Lorenzo Cain (12796494)': {'cost': 3700, 'position': 'OF', 'team': 'MIL'}, 'Christian Yelich (12796329)': {'cost': 5700, 'position': 'OF', 'team': 'MIL'}, 'Ryan Braun (12796486)': {'cost': 3700, 'position': 'OF', 'team': 'MIL'}, 'Mike Moustakas (12796366)': {'cost': 4700, 'position': '2B', 'team': 'MIL'}, 'Yasmani Grandal (12796433)': {'cost': 4000, 'position': 'C', 'team': 'MIL'}, 'Eric Thames (12796435)': {'cost': 4000, 'position': '1B', 'team': 'MIL'}, 'Travis Shaw (12796874)': {'cost': 2300, 'position': '3B', 'team': 'MIL'}, 'Ben Gamel (12796561)': {'cost': 3400, 'position': 'OF', 'team': 'MIL'}, 'Orlando Arcia (12796638)': {'cost': 3200, 'position': 'SS', 'team': 'MIL'}, 'Ronald Acuna Jr. (12796335)': {'cost': 5300, 'position': 'OF', 'team': 'ATL'}, 'Dansby Swanson (12796350)': {'cost': 4800, 'position': 'SS', 'team': 'ATL'}, 'Freddie Freeman (12796330)': {'cost': 5600, 'position': '1B', 'team': 'ATL'}, 'Josh Donaldson (12796436)': {'cost': 4000, 'position': '3B', 'team': 'ATL'}, 'Nick Markakis (12796420)': {'cost': 4100, 'position': 'OF', 'team': 'ATL'}, 'Austin Riley (12796354)': {'cost': 4800, 'position': 'OF', 'team': 'ATL'}, 'Ozzie Albies (12796382)': {'cost': 4300, 'position': '2B', 'team': 'ATL'}, 'Tyler Flowers (12796517)': {'cost': 3600, 'position': 'C', 'team': 'ATL'}, 'Mike Soroka (12796314)': {'cost': 10900, 'position': 'P', 'team': 'ATL'}, 'Max Kepler (12796346)': {'cost': 4900, 'position': 'OF', 'team': 'MIN'}, 'Jorge Polanco (12796341)': {'cost': 5000, 'position': 'SS', 'team': 'MIN'}, 'Nelson Cruz (12796349)': {'cost': 4800, 'position': 'OF', 'team': 'MIN'}, 'Eddie Rosario (12796345)': {'cost': 4900, 'position': 'OF', 'team': 'MIN'}, 'Mitch Garver (12796334)': {'cost': 5100, 'position': 'C', 'team': 'MIN'}, 'Marwin Gonzalez (12796470)': {'cost': 3800, 'position': '3B', 'team': 'MIN'}, 'C.J. Cron (12796371)': {'cost': 4500, 'position': '1B', 'team': 'MIN'}, 'Miguel Sano (12796374)': {'cost': 4600, 'position': '3B', 'team': 'MIN'}, 'Byron Buxton (12796364)': {'cost': 4600, 'position': 'OF', 'team': 'MIN'}, 'Justin Verlander (12796313)': {'cost': 11300, 'position': 'SP', 'team': 'HOU'}, 'Joey Lucchesi (12796316)': {'cost': 9600, 'position': 'SP', 'team': 'SD'}, 'Derek Law (12797295)': {'cost': 4000, 'position': 'SP', 'team': 'TOR'}}
total=50000

combinations=[item for item in itertools.combinations(s.items(), k) if sum([player[1]["cost"] for player in item]) == total]

teams=list()

 
for c in combinations:
	elements={}
	for player in c:
		if player[1]['position'] in elements:	
			elements[player[1]['position']] += 1
		else:
			elements[player[1]['position']] =1
	if elements.get('SP',0)== 2 and elements.get('C',0) == 1 and elements.get('1B',0)==1 and elements.get('2B',0)==1 and elements.get('3B',0)==1 and elements.get('SS',0)==1 and elements.get('OF',0)==3:
		teams.append(c) #c for while dict
	else:
		pass


# Put in Excel
with open('MLB_1.csv', 'w', newline='') as f:
	thewriter=csv.writer(f)
	thewriter.writerow(['Player 1','Player 2','Player 3','Player 4','Player 5','Player 6','Player 7','Player 8','Player 9','Player 10'])
	for person in teams:
		temp = [x for x,_ in person]
		thewriter.writerow(temp)



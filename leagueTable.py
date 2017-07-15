import urllib2
import json
from prettytable import PrettyTable

# fetch data
url = 'http://api.football-data.org/v1/competitions/398/leagueTable'

httpreq = urllib2.urlopen(url)
response = httpreq.read()
data = json.loads(response)

## print all data
# print json.dumps(data, indent=4, sort_keys=True)

def team_at_position(pos):
    return(data['standing'][pos]['teamName'])

def team_points(pos):
    return(data['standing'][pos]['points'])

# set up arrays for table columns
position = range(1, 21)
team = []
player = ["Callum Kirkwood", "David Kirkwood", "Duncan Kirkwood", "Wes Kirkwood"]
points = []

#populate blank arrays
for i in range(20):
    team.append(team_at_position(i))
    points.append(team_points(i))

# create table
t = PrettyTable(['Position', 'Team', 'Player', 'Points'])
t.add_row([position[0], team[0], player[0], points[0]])
t.add_row([position[1], team[1], player[1], points[1]])
t.add_row([position[2], team[2], player[2], points[2]])
t.add_row([position[3], team[3], player[3], points[3]])
# t.add_row([position[4], team[4], player[4], points[4]])
# t.add_row([position[5], team[5], player[5], points[5]])
# t.add_row([position[6], team[6], player[6], points[6]])
# t.add_row([position[7], team[7], player[7], points[7]])
# t.add_row([position[8], team[8], player[8], points[8]])
# t.add_row([position[9], team[9], player[9], points[9]])
# t.add_row([position[10], team[10], player[10], points[10]])
# t.add_row([position[11], team[11], player[11], points[11]])
# t.add_row([position[12], team[12], player[12], points[12]])
# t.add_row([position[13], team[13], player[13], points[13]])
# t.add_row([position[14], team[14], player[14], points[14]])
# t.add_row([position[15], team[15], player[15], points[15]])
# t.add_row([position[16], team[16], player[16], points[16]])
# t.add_row([position[17], team[17], player[17], points[17]])
# t.add_row([position[18], team[18], player[18], points[18]])
# t.add_row([position[19], team[19], player[19], points[19]])
# t.add_row([position[20], team[20], player[20], points[20]])
print t

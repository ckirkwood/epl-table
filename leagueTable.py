import urllib2
import json
import html
import datetime
from dotenv import load_dotenv, find_dotenv
import os
from prettytable import PrettyTable
from flask import Flask, request, render_template, jsonify, make_response, redirect

# url when running locally: http://192.168.1.102:33507/epl-table/api/v1.0/table

# retrieve credentials
load_dotenv(find_dotenv())
api_key = os.environ.get('API_KEY')
local_folder = os.environ.get('TEMPLATE_FOLDER')

# Initialise Flask api
app=Flask(__name__)

status = 0

@app.route('/')
def projects():
    return redirect("http://callumkirkwood.com/projects", code=302)

# Direct url to front end template
@app.route("/epl-table/api/v1.0/")
def index():
	return render_template('index.html')

# fetch data
url = 'http://api.football-data.org/v1/competitions/445/leagueTable'
req = urllib2.Request(url)
req.add_header('X-Auth-Token', api_key)
httpreq = urllib2.urlopen(req)
response = httpreq.read()
data = json.loads(response)

# append player names to dictionary
for i in range(20):
    if 'Arsenal FC' in data['standing'][i]['teamName']:
        arsenal = data['standing'][i]
        arsenal['player'] = 'Ian Kirkwood'
    elif 'Leicester City FC' in data['standing'][i]['teamName']:
        leicester = data['standing'][i]
        leicester['player'] = 'Duncan Kirkwood'
    elif 'Watford FC' in data['standing'][i]['teamName']:
        watford = data['standing'][i]
        watford['player'] = 'Lee Kirkwood'
    elif 'Liverpool FC' in data['standing'][i]['teamName']:
        liverpool = data['standing'][i]
        liverpool['player'] = 'Andrenna Kirkwood'
    elif 'Southampton FC' in data['standing'][i]['teamName']:
        southampton = data['standing'][i]
        southampton['player'] = 'Mark Kirkwood'
    elif 'Swansea City FC' in data['standing'][i]['teamName']:
        swansea = data['standing'][i]
        swansea['player'] = 'Ian Edward Kirkwood'
    elif 'Newcastle United FC' in data['standing'][i]['teamName']:
        newcastle = data['standing'][i]
        newcastle['player'] = 'Bob Kirkwood'
    elif 'Tottenham Hotspur FC' in data['standing'][i]['teamName']:
        spurs = data['standing'][i]
        spurs['player'] = 'Callum Kirkwood'
    elif 'Manchester United FC' in data['standing'][i]['teamName']:
        manutd = data['standing'][i]
        manutd['player'] = 'Lynn Kirkwood'
    elif 'West Ham United FC' in data['standing'][i]['teamName']:
        westham = data['standing'][i]
        westham['player'] = 'Will Kirkwood'
    elif 'Everton FC' in data['standing'][i]['teamName']:
        everton = data['standing'][i]
        everton['player'] = 'David Kirkwood'
    elif 'Stoke City FC' in data['standing'][i]['teamName']:
        stoke = data['standing'][i]
        stoke['player'] = 'Stevie Hill'
    elif 'Crystal Palace FC' in data['standing'][i]['teamName']:
        stoke = data['standing'][i]
        stoke['player'] = 'Dave Kirkwood'
    elif 'Huddersfield Town' in data['standing'][i]['teamName']:
        huddersfield = data['standing'][i]
        huddersfield['player'] = 'Wes Kirkwood'
    elif 'Chelsea FC' in data['standing'][i]['teamName']:
        chelsea = data['standing'][i]
        chelsea['player'] = 'Alan Kirkwood'
    elif 'Burnley FC' in data['standing'][i]['teamName']:
        burnley = data['standing'][i]
        burnley['player'] = 'Stuart Kirkwood'
    elif 'Brighton & Hove Albion' in data['standing'][i]['teamName']:
        brighton = data['standing'][i]
        brighton['player'] = 'Kyle Kirkwood'
    elif 'Manchester City FC' in data['standing'][i]['teamName']:
        mancity = data['standing'][i]
        mancity['player'] = 'John Peter Kirkwood'
    elif 'West Bromwich Albion FC' in data['standing'][i]['teamName']:
        westbrom = data['standing'][i]
        westbrom['player'] = 'Ian Reed'
    elif 'AFC Bournemouth' in data['standing'][i]['teamName']:
        bournemouth = data['standing'][i]
        bournemouth['player'] = 'Stephie Hill'

# create functions to simplify requests
def get_data():
    return json.dumps(data, indent=4, sort_keys=True)

def team_at_position(pos):
    return(data['standing'][pos]['teamName'])

def played(pos):
    return(data['standing'][pos]['playedGames'])

def won(pos):
    return(data['standing'][pos]['wins'])

def lost(pos):
    return(data['standing'][pos]['losses'])

def draws(pos):
    return(data['standing'][pos]['draws'])

def goalDifference(pos):
    return(data['standing'][pos]['goalDifference'])

def team_points(pos):
    return(data['standing'][pos]['points'])

def player_name(pos):
    return(data['standing'][pos]['player'])

# set up arrays for table columns
position = range(1, 21)
team = []
gamesPlayed = []
w = []
l = []
d = []
gd = []
points = []

#populate blank arrays
for i in range(20):
    team.append(team_at_position(i))
    gamesPlayed.append(played(i))
    w.append(won(i))
    l.append(lost(i))
    d.append(draws(i))
    gd.append(goalDifference(i))
    points.append(team_points(i))

# create table
t = PrettyTable(['#', 'Team', 'Player', 'Pld', 'W', 'L', 'D', 'GD', 'Pts'])

for i in range(20):
    t.add_row([position[i], team[i], player_name(i), gamesPlayed[i], w[i], l[i], d[i], gd[i], points[i]])

# print table to console
t.align["#"] = "c"
t.align["Team"] = "l"
t.align["Player"] = "l"
t.align["Pld"] = "r"
t.align["W"] = "r"
t.align["L"] = "r"
t.align["D"] = "r"
t.align["GD"] = "r"
t.align["Pts"] = "r"
t.format = False
print(t)

# prepare to send latest table data to a html template
def export_html(element, url, body):
	now = datetime.datetime.today().strftime("%Y%m%d-%H%M%S")
	try:
		filename = '/app/templates/' + element + '.html'
		f = open(filename,'w')
	except IOError:
		filename = local_folder + element + '.html'
		f = open(filename,'w')

	wrapper = """
	<!DOCTYPE html>
	<html>
	<head>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta charset="utf-8">
	<title>Kirkwood Sweepstakes - Standings</title>
	<link rel=stylesheet type=text/css href="{{ url_for('static', filename='style.css') }}">
	<link href="https://fonts.googleapis.com/css?family=Montserrat:500,700,800" rel="stylesheet">
	</head>
	<body>
    <p>url: <a href=\"%s\">%s</a></p><p>%s</p>
	</body>
	</html>
	"""

	whole = wrapper % (element, now, body)
	f.write(whole)
	f.close()

# convert table to html, call export function
html = t.get_html_string(attributes={"name":"epl-table", "class":"table"})
export_html('table', 'http://192.168.1.102:2525/epl-table/api/v1.0/table', html)

# Set up API endpoints
@app.route('/epl-table/api/v1.0/<string:st>', methods=['GET'])
def get_table(st):
    global status
    if st == 'data':
        status = 1
        return get_data()
    elif st == 'table':
        status = 1
        return render_template('table.html')

# 404 response
@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not found'}), 404)

# Main programme logic
if __name__ == "__main__":
    import os
    app.run(host='::', port=int(os.environ.get('PORT', 33507)), debug=True)

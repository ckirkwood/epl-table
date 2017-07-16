import urllib2
import json
import html
import datetime
from prettytable import PrettyTable
from flask import Flask, request, render_template, jsonify, make_response

# Initialise Flask api
app=Flask(__name__)

status = 0

# Direct url to front end template
@app.route("/epl-table/api/v1.0/")
def index():
	return render_template('index.html')

# fetch data
url = 'http://api.football-data.org/v1/competitions/445/leagueTable'
httpreq = urllib2.urlopen(url)
response = httpreq.read()
data = json.loads(response)

# add player names to dictionary
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

def team_points(pos):
    return(data['standing'][pos]['points'])

def player_name(pos):
    return(data['standing'][pos]['player'])

# set up arrays for table columns
position = range(1, 21)
team = []
points = []

#populate blank arrays
for i in range(20):
    team.append(team_at_position(i))
    points.append(team_points(i))

# create table
t = PrettyTable(['Position', 'Team', 'Player', 'Points'])
t.add_row([position[0], team[0], player_name(0), points[0]])
t.add_row([position[1], team[1], player_name(1), points[1]])
t.add_row([position[2], team[2], player_name(2), points[2]])
t.add_row([position[3], team[3], player_name(3), points[3]])
t.add_row([position[4], team[4], player_name(4), points[4]])
t.add_row([position[5], team[5], player_name(5), points[5]])
t.add_row([position[6], team[6], player_name(6), points[6]])
t.add_row([position[7], team[7], player_name(7), points[7]])
t.add_row([position[8], team[8], player_name(8), points[8]])
t.add_row([position[9], team[9], player_name(9), points[9]])
t.add_row([position[10], team[10], player_name(10), points[10]])
t.add_row([position[11], team[11], player_name(11), points[11]])
t.add_row([position[12], team[12], player_name(12), points[12]])
t.add_row([position[13], team[13], player_name(13), points[13]])
t.add_row([position[14], team[14], player_name(14), points[14]])
t.add_row([position[15], team[15], player_name(15), points[15]])
t.add_row([position[16], team[16], player_name(16), points[16]])
t.add_row([position[17], team[17], player_name(17), points[17]])
t.add_row([position[18], team[18], player_name(18), points[18]])
t.add_row([position[19], team[19], player_name(19), points[19]])

# print table to console
t.align = 'l'
t.format = False
print t

# prepare to send latest table data to a html template
def export_html(element, url, body):
    now = datetime.datetime.today().strftime("%Y%m%d-%H%M%S")
    filename = '/Users/CallumKirkwood/Library/Mobile Documents/com~apple~CloudDocs/Documents/Programming/Github/epl-table/templates/' + element + '.html'
    f = open(filename,'w')

    wrapper = """
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8">
    <title>Kirkwood Sweepstakes - Standings</title>
    <link rel=stylesheet type=text/css href="{{ url_for('static', filename='style.css') }}">
    </head>
    <body>
    <body><p>URL: <a href=\"%s\">%s</a></p><p>%s</p></body>
    </body>
    </html>
    """

    whole = wrapper % (element, now, body)
    f.write(whole)
    f.close()

# convert table to html, run through export function
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
	app.run(host='192.168.1.102', port=2525, debug=True)

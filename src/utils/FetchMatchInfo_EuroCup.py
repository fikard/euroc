__author__ = 'fikardjiang'

import requests
import sys
from bs4 import BeautifulSoup




eurpCup_match_url = 'http://www.uefa.com/friendlies/season=2016/matches/index.html'
match_url = 'http://www.uefa.com/uefaeuro/season=2016/matches/round=2000448/match=%s/statistics/index.html'
test_url = 'www.google.com.hk'

''' team information '''
CONSTANTS_HOME = 'card-fbd-team-home'
CONSTANTS_AWAY = 'card-fbd-team-away'

''' team attacking data '''
CONSTANTS_GOAL_SCORE_HOME = 'goals-scored--value graph-bar--number-value graph-bar--number-value__home-team'
CONSTANTS_GOAL_SCORE_AWAY = 'goals-scored--value graph-bar--number-value graph-bar--number-value__away-team'
CONSTANTS_ATTEMPTS_HOME = 'total-attempts--value graph-bar--number-value graph-bar--number-value__home-team'
CONSTANTS_ATTEMPTS_AWAY = 'total-attempts--value graph-bar--number-value graph-bar--number-value__away-team'
DATA_BIND_ATTEMPTS_HOME = 'text: home.totalAttempts'
DATA_BIND_ATTEMPTS_AWAY = 'text: away.totalAttempts'
DATA_BIND_ATTEMPTSON_HOME = 'text: home.attempsOn'
DATA_BIND_ATTEMPTSON_AWAY = 'text: away.attempsOn'
DATA_BIND_ATTEMPTSOFF_HOME = 'text: home.attempsOff'
DATA_BIND_ATTEMPTSOFF_AWAY = 'text: away.attempsOff'
DATA_BIND_SHOTBLOCK_HOME = 'text: home.shotBlocked'
DATA_BIND_SHOTBLOCK_AWAY = 'text: away.shotBlocked'
DATA_BIND_WOODWORK_HOME = 'text: home.attemptsAgainstW'
DATA_BIND_WOODWORK_AWAY = 'text: away.attemptsAgainstW'
CONSTANTS_CORNERS_HOME = 'corner--value graph-bar--number-value graph-bar--number-value__home-team'
CONSTANTS_CORNERS_AWAY = 'corner--value graph-bar--number-value graph-bar--number-value__away-team'
CONSTANTS_OFFSIDES_HOME = 'offside--value graph-bar--number-value graph-bar--number-value__home-team'
CONSTANTS_OFFSIDES_AWAY = 'offside--value graph-bar--number-value graph-bar--number-value__away-team'


''' team performance data '''
CONSTANTS_BALL_POSSESS_HOME = 'ball-possession--value graph-circle--number-value graph-circle--number-value__home-team'
CONSTANTS_BALL_POSSESS_AWAY = 'ball-possession--value graph-circle--number-value graph-circle--number-value__away-team'
CONSTANTS_PASS_HOME = 'passes--value graph-bar--number-value graph-bar--number-value__home-team'
CONSTANTS_PASS_AWAY = 'passes--value graph-bar--number-value graph-bar--number-value__away-team'
CONSTANTS_PASS_COM_HOME = 'passes-completed--value graph-bar--number-value graph-bar--number-value__home-team'
CONSTANTS_PASS_COM_AWAY = 'passes-completed--value graph-bar--number-value graph-bar--number-value__away-team'
CONSTANTS_DISTANCE_HOME = 'distance-run--value graph-bar--number-value graph-bar--number-value__home-team'
CONSTANTS_DISTANCE_AWAY = 'distance-run--value graph-bar--number-value graph-bar--number-value__away-team'


''' team defending data '''
CONSTANTS_BALL_RECOVER_HOME = 'balls-recovered--value graph-bar--number-value graph-bar--number-value__home-team'
CONSTANTS_BALL_RECOVER_AWAY = 'balls-recovered--value graph-bar--number-value graph-bar--number-value__away-team'
CONSTANTS_TACKLES_HOME = 'taclkles--value graph-bar--number-value graph-bar--number-value__home-team'
CONSTANTS_TACKLES_AWAY = 'taclkles--value graph-bar--number-value graph-bar--number-value__away-team'
CONSTANTS_BLOCK_HOME = 'blocks-completed--value graph-bar--number-value graph-bar--number-value__home-team'
CONSTANTS_BLOCK_AWAY = 'blocks-completed--value graph-bar--number-value graph-bar--number-value__away-team'
CONSTANTS_CLEARANCE_HOME = 'clearances-completed--value graph-bar--number-value graph-bar--number-value__home-team'
CONSTANTS_CLEARANCE_AWAY = 'clearances-completed--value graph-bar--number-value graph-bar--number-value__away-team'


''' team Disciplinary data '''
CONSTANTS_YELLOWCARD_HOME = 'yellow-cards--value graph-bar--number-value graph-bar--number-value__home-team'
CONSTANTS_YELLOWCARD_AWAY = 'yellow-cards--value graph-bar--number-value graph-bar--number-value__away-team'
CONSTANTS_REDCARD_HOME = 'red-cards--value graph-bar--number-value graph-bar--number-value__home-team'
CONSTANTS_REDCARD_AWAY = 'red-cards--value graph-bar--number-value graph-bar--number-value__away-team'
CONSTANTS_FOULS_HOME = 'fouls-committed--value graph-bar--number-value graph-bar--number-value__home-team'
CONSTANTS_FOULS_AWAY = 'fouls-committed--value graph-bar--number-value graph-bar--number-value__away-team'


''' team head to head data '''
CONSTANTS_HOME_GOALS = 'h2h-stat-gs h2h-team-a'
CONSTANTS_HOME_WINS = 'h2h-stat-wins h2h-team-a'
CONSTANTS_DRAWS = 'h2h-stat-draw'
CONSTANTS_AWAY_WINS = 'h2h-stat-wins h2h-team-b'
CONSTANTS_AWAY_GOALS = 'h2h-stat-gs h2h-team-b'



TEAMSETS = [CONSTANTS_HOME, CONSTANTS_AWAY]

GOALSETS = [CONSTANTS_GOAL_SCORE_HOME, CONSTANTS_GOAL_SCORE_AWAY]
CORNERSETS = [CONSTANTS_CORNERS_HOME, CONSTANTS_CORNERS_AWAY]
OFFSIDESSETS = [CONSTANTS_OFFSIDES_HOME, CONSTANTS_OFFSIDES_AWAY]

DATAATEMPT = [DATA_BIND_ATTEMPTS_HOME, DATA_BIND_ATTEMPTS_AWAY]
DATAATEMPTON = [DATA_BIND_ATTEMPTSON_HOME, DATA_BIND_ATTEMPTSON_AWAY]
DATAATEMPTOFF = [DATA_BIND_ATTEMPTSOFF_HOME, DATA_BIND_ATTEMPTSOFF_AWAY]
DATASHOTBLOCK = [DATA_BIND_SHOTBLOCK_HOME, DATA_BIND_SHOTBLOCK_AWAY]
DATAWOODWORK = [DATA_BIND_WOODWORK_HOME, DATA_BIND_WOODWORK_AWAY]

BALLPOSSSETS = [CONSTANTS_BALL_POSSESS_HOME, CONSTANTS_BALL_POSSESS_AWAY]
PASSSETS = [CONSTANTS_PASS_HOME, CONSTANTS_PASS_AWAY]
PASSCOMSETS = [CONSTANTS_PASS_COM_HOME, CONSTANTS_PASS_COM_AWAY]
DISTANCESETS = [CONSTANTS_DISTANCE_HOME, CONSTANTS_DISTANCE_AWAY]
BALLRECOVERSETS = [CONSTANTS_BALL_RECOVER_HOME, CONSTANTS_BALL_RECOVER_AWAY]
TACKLESSETS = [CONSTANTS_TACKLES_HOME, CONSTANTS_TACKLES_AWAY]
BLOCKSETS = [CONSTANTS_BLOCK_HOME, CONSTANTS_BLOCK_AWAY]
CLEARANCESETS = [CONSTANTS_CLEARANCE_HOME, CONSTANTS_CLEARANCE_AWAY]

YCSETS = [CONSTANTS_YELLOWCARD_HOME, CONSTANTS_YELLOWCARD_AWAY]
RCSETS = [CONSTANTS_REDCARD_HOME, CONSTANTS_REDCARD_AWAY]
FOULSETS = [CONSTANTS_FOULS_HOME, CONSTANTS_FOULS_AWAY]

H2HSTATGOALS = [CONSTANTS_HOME_GOALS, CONSTANTS_AWAY_GOALS]
H2HSTATWINS = [CONSTANTS_HOME_WINS, CONSTANTS_AWAY_WINS]
H2HSTATDRAWS = [CONSTANTS_DRAWS, CONSTANTS_DRAWS]
H2HSTATLOSES = [CONSTANTS_AWAY_WINS, CONSTANTS_HOME_WINS]
H2HSTATLEN = 4

ALLSETS = [TEAMSETS, GOALSETS, DATAATEMPT, DATAATEMPTON, DATAATEMPTOFF, DATASHOTBLOCK, DATAWOODWORK,
           CORNERSETS, OFFSIDESSETS, BALLPOSSSETS, PASSSETS, PASSCOMSETS, DISTANCESETS,
           BALLRECOVERSETS, TACKLESSETS, BLOCKSETS, CLEARANCESETS, YCSETS, RCSETS, FOULSETS, H2HSTATGOALS,
           H2HSTATWINS, H2HSTATDRAWS, H2HSTATLOSES]
KEYS = ['Team', 'Goals', 'Total Attempts', 'On Target', 'Off Target', 'Blocked', 'WoodWork',
        'Corners', 'Offsides', 'Possession', 'Passes', 'Passes Compeleted', 'Distance Coverd',
        'Balls Recovered', 'Tackles', 'Blocks', 'Clearances', 'Yellow Card', 'Red Card',
        'Fouls Commit', 'PreviousMatch Goals', 'PreviousMatch Wins', 'PreviousMatch Draws', 'PreviousMatch Loses']

def fetch_url(url, index):
    session = requests.session()
    session.headers = {
        'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }
    #session.proxies = {'http': 'web-proxy.oa.com:8080', 'https': 'web-proxy.oa.com:8080'}
    r = session.get(url)

    content = BeautifulSoup(r.content, 'lxml')

    if len(ALLSETS) != len(KEYS):
        print('Default value error')
        sys.exit(0)

    filename = ''
    writebuffer= ''
    for i in range(len(ALLSETS)):
        sets = ALLSETS[i]
        values = []
        outstr = ''
        if i == 0:
            for j in range(len(sets)):
                attr = content.find('div', attrs={'class': sets[j]}).findAll('span', attrs={'class': 'full'})[0]
                values.append(attr.get_text())
            for k in range(len(values)):
                outstr = outstr + values[k] + '\t\t'
            filename = 'Match_'+values[0]+'_'+values[1]+'_'+str(index)
        elif i >= 2 and i <= 6:
            attr = content.findAll('div', attrs={'class': CONSTANTS_ATTEMPTS_HOME, 'data-bind': sets[0]})[0]
            values.append(attr.get_text())
            attr = content.findAll('div', attrs={'class': CONSTANTS_ATTEMPTS_AWAY, 'data-bind': sets[1]})[0]
            values.append(attr.get_text())
            outstr = values[0] + '\t\t' + values[1]
        elif i >= len(ALLSETS)-H2HSTATLEN:
            if i == len(ALLSETS) - H2HSTATLEN:
                for j in range(len(sets)):
                    attr = content.find('div', attrs={'class': sets[j]}).findAll('div', attrs={'class': 'h2h-circle'})[0]
                    values.append(attr.get_text())
            else:
                for j in range(len(sets)):
                    attr = content.find('div', attrs={'class': sets[j]}).findAll('div', attrs={'class': 'h2h-circle js-h2h-circle'})[0]
                    values.append(attr.get_text())
            for k in range(len(values)):
                outstr = outstr + values[k] + '\t\t'
        else:
            for j in range(len(sets)):
                attr = content.findAll('div', attrs={'class': sets[j]})[0]
                values.append(attr.get_text())
            for k in range(len(values)):
                outstr = outstr + values[k] + '\t\t'
        print(KEYS[i]+'\t\t'+outstr+'\n')
        writebuffer = writebuffer + KEYS[i]+'\t\t'+outstr + '\n'
    with open(filename, 'w') as f:
        f.write(writebuffer)
        f.close()

if __name__ == '__main__':
    roundSpec = 1
    START_MATCH_FLAG = 2017877
    END_MATCH_FLAG = 2017964
    for i in range(START_MATCH_FLAG, END_MATCH_FLAG+1):
        url = match_url % i
        try:
            fetch_url(url, i)
        except Exception as e:
            print('%d: Error %s \n' %(i, e))
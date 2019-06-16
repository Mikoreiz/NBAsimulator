from bs4 import BeautifulSoup
from urllib.request import urlopen
import html.parser

url = 'https://www.teamrankings.com/nba/stat/possessions-per-game'
HTML = urlopen(url).read()
urlopen(url).close()
soupPage = BeautifulSoup(HTML, 'html.parser')

table = soupPage.find('table')
tbody = table.find('tbody')

with open('possessions.txt', 'w') as f:
    f.write('team, poss_per_game\n')
    for tr in tbody.find_all('tr'):
        td = tr.find_all('td')
        f.write('%s, %s\n' % (td[1].text, td[2].text))

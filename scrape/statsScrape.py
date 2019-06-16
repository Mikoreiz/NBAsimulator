from bs4 import BeautifulSoup
from urllib.request import urlopen
import html.parser

hawksUrl = 'https://www.basketball-reference.com/teams/ATL/2019.html'
hawksHTML = urlopen(hawksUrl).read()
urlopen(hawksUrl).close()
hawksSoupPage = BeautifulSoup(hawksHTML, 'html.parser')
hawksStats = hawksSoupPage.find_all(
    'table', {'class': 'sortable stats_table now_sortable'})
print(hawksStats)

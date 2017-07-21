import requests
from bs4 import BeautifulSoup
import datetime
from remove_duplicates_from_list import removeDuplicates

####
#### Harvard Business Review ####
####

reqLdrMgm = requests.get('https://hbr.org/topic/leadership-and-managing-people')
soupLdrMgm = BeautifulSoup(reqLdrMgm.text, 'html.parser')

reqDecisions = requests.get('https://hbr.org/topic/decision-making')
soupDecisions = BeautifulSoup(reqDecisions.text, 'html.parser')

reqCreativity = requests.get('https://hbr.org/topic/creativity')
soupCreativity = BeautifulSoup(reqCreativity.text, 'html.parser')

reqStrategy = requests.get('https://hbr.org/topic/strategy')
soupStrategy = BeautifulSoup(reqStrategy.text, 'html.parser')

reqCareer = requests.get('https://hbr.org/topic/career-planning')
soupCareer = BeautifulSoup(reqCareer.text, 'html.parser')
# Only pulling articles from the Leadership/Management, Decision-Making, 
# Creativity, Strategy, and Career-Planning categories

hbrlinks = []

for div in soupLdrMgm.find_all('div', class_ = 'stream-image'):
	link = div.find_next('a').get('href')
	hbrlinks.append(link)
for div in soupDecisions.find_all('div', class_ = 'stream-image'):
	link = div.find_next('a').get('href')
	hbrlinks.append(link)
for div in soupCreativity.find_all('div', class_ = 'stream-image'):
	link = div.find_next('a').get('href')
	hbrlinks.append(link)
for div in soupStrategy.find_all('div', class_ = 'stream-image'):
	link = div.find_next('a').get('href')
	hbrlinks.append(link)
for div in soupCareer.find_all('div', class_ = 'stream-image'):
	link = div.find_next('a').get('href')
	hbrlinks.append(link)
# Adds the second half of the url for an article to the list hbrlinks

hbrlinks = removeDuplicates(hbrlinks)

today = datetime.date.today()

def compareDate(urlstring):
	year = int(urlstring[1:5])
	month = int(urlstring[6:8])
	day = 1
	# Always assuming that the article was written on the first so we don't need to 
	# run BeautifulSoup on it's link. Instead we take the date from the url

	# Finding the difference in days between today and each article
	sitedate = datetime.date(year, month, day)
	difference = today - sitedate

	# Becuase we always assume the articles were written on the 1st, return True if 
	# it is newer than 60 days old
	if difference.days > 60:
		return False
	else:
		return True

goodlinks = []
goodsoups = []

for i in range(len(hbrlinks)):
	print(hbrlinks[i])
	if hbrlinks[i][1:6] == 'video' or hbrlinks[i][1:8] == 'product' or hbrlinks[i][1:10] == 'sponsored':
		print('Not a good link')
	elif compareDate(hbrlinks[i]):
		link = 'https://hbr.org' + hbrlinks[i]

		goodlinks.append(link)

		reqHBRarticle = requests.get(link)
		soupHBRarticle = BeautifulSoup(reqHBRarticle.text, 'html.parser')
		goodsoups.append(soupHBRarticle)

for i in range(len(goodlinks)):
	print(goodlinks[i])













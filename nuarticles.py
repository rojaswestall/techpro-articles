import requests
from bs4 import BeautifulSoup

####
#### Northwestern Insight KELLOGG School of Managment Website ####
####

reqStrategy = requests.get('https://insight.kellogg.northwestern.edu/browse/topic/strategy')
soupStrategy = BeautifulSoup(reqStrategy.text, 'html.parser')

reqCareers = requests.get('https://insight.kellogg.northwestern.edu/browse/topic/careers')
soupCareers = BeautifulSoup(reqCareers.text, 'html.parser')

reqCulture = requests.get('https://insight.kellogg.northwestern.edu/browse/topic/culture')
soupCulture = BeautifulSoup(reqCulture.text, 'html.parser')

reqLeadership = requests.get('https://insight.kellogg.northwestern.edu/browse/topic/leadership')
soupLeadership = BeautifulSoup(reqLeadership.text, 'html.parser')

reqTrust = requests.get('https://insight.kellogg.northwestern.edu/browse/topic/trust')
soupTrust = BeautifulSoup(reqTrust.text, 'html.parser')
#Only pulling articles from the strategy, careers, culture, leadership, and trust categories

nulinks = []

for li in soupStrategy.find_all('li', class_ = 'with-image'):
	atag = li.find_next('a')
	link = atag.get('href')
	nulinks.append(link)
for li in soupCareers.find_all('li', class_ = 'with-image'):
	atag = li.find_next('a')
	link = atag.get('href')
	nulinks.append(link)
for li in soupCulture.find_all('li', class_ = 'with-image'):
	atag = li.find_next('a')
	link = atag.get('href')
	nulinks.append(link)
for li in soupLeadership.find_all('li', class_ = 'with-image'):
	atag = li.find_next('a')
	link = atag.get('href')
	nulinks.append(link)
for li in soupTrust.find_all('li', class_ = 'with-image'):
	atag = li.find_next('a')
	link = atag.get('href')
	nulinks.append(link)
#Adds the second half of the url for an article to nulinks

nulinks = list(set(nulinks))
nulinks = ['https://insight.kellogg.northwestern.edu' + link for link in nulinks]
#nulinks is now a list of urls for all useful articles on the site without any repeats

# def compareDate(string)
# Write this so it compares it to the current date and returns true if it is newer than two weeks old, false otherwise


for link in nulinks:
	reqNUarticle = requests.get(link)
	soupNUarticle = BeautifulSoup(reqNUarticle.text, 'html.parser')
	date = soupNUarticle.find('span', class_ = 'time')
	date = ''.join(date.strings)
	print(date)

#Want to remove all the article that are over two weeks old

# print(nulinks)
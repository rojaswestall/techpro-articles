import requests
from bs4 import BeautifulSoup
import datetime
from remove_duplicates_from_list import removeDuplicates

####
#### Northwestern University Insight KELLOGG School of Managment ####
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
# Only pulling articles from the strategy, careers, culture, leadership, and trust categories

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
# Adds the second half of the url for an article to the list nulinks

nulinks = removeDuplicates(nulinks)
nulinks = ['https://insight.kellogg.northwestern.edu' + link for link in nulinks]
# nulinks is now a list of urls for all useful articles on the site without any repeats


today = datetime.date.today()

def compareDate(datestring):
	monthstr = datestring[1:4]
	daystr = datestring[5]
	yearstr = datestring[8:12]

	# Converting the month to an int
	if monthstr == 'Jan':
		month = 1
	elif monthstr == 'Feb':
		month = 2
	elif monthstr == 'Mar':
		month = 3
	elif monthstr == 'Apr':
		month = 4
	elif monthstr == 'May':
		month = 5
	elif monthstr == 'Jun':
		month = 6
	elif monthstr == 'Jul':
		month = 7
	elif monthstr == 'Aug':
		month = 8
	elif monthstr == 'Sep':
		month = 9
	elif monthstr == 'Oct':
		month = 10
	elif monthstr == 'Nov':
		month = 11
	elif monthstr == 'Dec':
		month = 12

	# Converting the day and year to ints
	day = int(daystr)
	year = int(yearstr)

	# Finding the difference in days between today and each article
	sitedate = datetime.date(year, month, day)
	difference = today - sitedate

	# Return True if it is younger than 40 days old
	if difference.days > 40:
		return False
	else:
		return True

goodlinks = []
goodsoups = []

for link in nulinks:
	reqNUarticle = requests.get(link)
	soupNUarticle = BeautifulSoup(reqNUarticle.text, 'html.parser')
	date = soupNUarticle.find('span', class_ = 'time')
	date = date.text # This gives us the date of the article as a string
	if compareDate(date):
		goodlinks.append(link) # Holding onto the links and soupobjects
		goodsoups.append(soupNUarticle)

# Printing out the links and descriptions for each article
for i in range(len(goodlinks)):
	print(goodlinks[i])
	preview = goodsoups[i].find('p', class_ = 'bumper').text
	print(preview + '\n' + '\n')


















import requests
from bs4 import BeautifulSoup 
import pprint 

res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text, 'html.parser')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res.text, 'html.parser')


links = soup.select('.storylink')
links2 = soup.select('.storylink')
subtext = soup.select('.subtext')
subtext2 = soup.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2

def sort_stories_by_votes(hnlist):
	return sorted(hnlist, key= lambda k:['votes'], reverse=True)

def create_custom_hn(links, votes):
	hn = []
	for idx, item in enumerate(links):
		title = item.getText()
		href = links[idx].get('href', None)
		vote = subtext[idx].select('.score')
		if len(vote):
			points = int(vote.getText().replace(' points', ''))
			if points > 99:
				hn.append({'title': title, 'link': href, 'votes': points})
	return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(mega_links, mega_subtext))

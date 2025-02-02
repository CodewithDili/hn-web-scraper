Hacker News Web Scraper

This project is a web scraper for [Hacker News](https://news.ycombinator.com/), built using Python, BeautifulSoup, and Requests. The scraper fetches the top stories with more than 99 votes and displays them in a sorted list.

Features
- Fetches stories from Hacker News.
- Filters stories with more than 99 votes.
- Sorts stories by the number of votes in descending order.
- Displays the title, link, and votes for each story.

Requirements
- Python 3.x
- Requests
- BeautifulSoup4

Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/CodewithDili/hn-web-scraper.git
Navigate to the project directory:


cd hn-web-scraper
Install the required packages:


pip install requests beautifulsoup4
Usage
Run the script:


python scraper.py
Code Example
python
Copy code
import requests
from bs4 import BeautifulSoup 
import pprint 

res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text, 'html.parser')

links = soup.select('.storylink')
subtext = soup.select('.subtext')

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(links, subtext))
License
This project is licensed under the MIT License - see the LICENSE file for details.

Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

Contact
For any inquiries or feedback, please contact Dilichi Ike-Obasi.

You can create the repository on GitHub with the name `hn-web-scraper` and use this README file to document your project.





#   h n - w e b - s c r a p e r  
 
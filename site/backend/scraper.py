from lxml import html
from urllib import parse as urlparse
import json

class Scraper:
    def __init__(self, constraints, soup):
        # convert JSON constraints to Python dict
        self.constraints = {}
        self.results = {}
        for c in self.constraints:
            self.results[c] = {}
        self.soup = soup

    def scrape(self):
        for c in self.constraints:
            for a in self.constraints[c]['attributes']:
                # make sure None means that that attribute is absent
                if self.constraints[c]['attributes'][a] == None:
                    print('Not implemented yet')


{'name': {'url': '', 'tag': '<table>', 'attributes': {'id': 'medarbejdertable', 'class': None}}, 'title': {'url': '', 'attributes': {'id': 'medarbejdertable', 'class': None}}}

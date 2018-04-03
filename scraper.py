#! /usr/bin/python3

import bs4 as bs 
import urllib.request

toopo = []

source = urllib.request.urlopen("https://www.nytimes.com").read()

soup = bs.BeautifulSoup(source)

print(soup)

#! python3

#https://www.practicepython.org/


# Exercise 17. Decode a Web Page

'''
This is the first 4-chili exercise of this blog! We’ll see what people think,
and decide whether or not to continue with 4-chili exercises in the future.

Use the BeautifulSoup and requests Python packages to print out a list of 
all the article titles on the New York Times homepage.


'''

import requests, lxml, webbrowser

from bs4 import BeautifulSoup

import requests
from bs4 import BeautifulSoup
 
base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text)
 
for story_heading in soup.find_all(class_="story-heading"): 
    if story_heading.a: 
        print(story_heading.a.text.replace("\n", " ").strip())
    else: 
        print(story_heading.contents[0].strip())
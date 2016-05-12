"""This is a web scraper made for the Daily Bruin."""

from bs4 import BeautifulSoup
import requests
import json
import re

'''To run it yourself:
    1. pip install requests
    2. pip install beautifulsoup4
'''

"""special characters like: ” (NOT USING THIS IN THE CODE!!!)"""
def removeSpecialCharacters(string):
    string = string.replace("”", "\"")
    string = string.replace("“", "\"")
    string = string.replace("’", "\'")
    string = string.replace("–", "-")
    return string

"""Enter URLs as strings"""
urls = [
    "http://dailybruin.com/2016/05/06/students-approve-all-four-referenda-on-usac-election-ballot/",
    "http://dailybruin.com/2016/05/06/volunteer-center-explains-rationale-for-ending-collaboration-with-womp/",
    "http://dailybruin.com/2016/05/05/students-love-of-baking-blooms-into-sourdough-bread-business/",
    "http://dailybruin.com/2016/05/06/jasmine-aquino-allowing-usac-to-campaign-on-the-hill-would-promote-political-dialogue/",
    "http://dailybruin.com/2016/05/06/track-athletes-to-compete-at-pac-12-multis-championship/",
    "http://dailybruin.com/2016/05/06/usac-election-board-must-disqualify-social-justice-referendum/",
    "http://dailybruin.com/2016/05/06/abhishek-shetty-usac-election-board-should-extend-physical-campaigning-period/"
]

obj = []
count = 1

for url in urls:
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")

        headline = str(soup.find("div", class_="db-post-headline").text)
        authors = soup.find("div", class_="db-byline").find_all("a")
        tempList = []
        for author in authors:
            tempList.append(author.text)
        story = soup.find("div", class_="db-post-content")
        story = str(story.text).split("\n<!-- Simple Share Buttons Adder")[0]
        dates = soup.find_all("h5")
        postingDate = ""
        for date in dates:
            postingDate += str(date.text)
        regex = re.compile('.*wp.*')
        imageList = []
        images = soup.find_all("img", {"class": regex})

        for image in images:
            imageLink = str(image).split("src=")[1].split("-")[0]
            imageList.append("<img src=" + imageLink + ".jpg\">")

        """this needs works"""
        imageCaption = str(soup.find("p", class_="db-image-caption").text).replace("\t", "").replace("\n", "")

        obj.append({u"headline": headline, u"postDate": postingDate, u"authors": tempList, u"images": imageList, u"caption": imageCaption, u"content": story, u"url": url})

        #print(json.dumps(obj, indent=4))
        #outputs to terminal

        #text file for viewing
        with open("output.txt", "w") as text_file:
            text_file.write(json.dumps(obj, indent=4))
            print("URL number " + str(count) + " scraped" + " (" + str(url) + ")")
            count += 1

        #actual json data
        with open('data.json', 'w') as f:
            json.dump(obj, f)
            
    except requests.exceptions.RequestException as e:
        print(e)

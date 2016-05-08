"""This is a web scraper made for the Daily Bruin."""

from bs4 import BeautifulSoup
import requests

'''To run it yourself:
    1. pip install requests
    2. pip install beautifulsoup4
'''

try:
    r = requests.get("http://dailybruin.com/2016/05/06/bruins-united-sails-past-waves-of-change-in-2016-usac-election/")
    soup = BeautifulSoup(r.content, "html.parser")

    headline = soup.find("div", class_="db-post-headline").h1.contents[0]
    authors = soup.find("div", class_="db-byline").find_all("a")
    with open("output.txt", "w") as text_file:
        text_file.write(headline)
        text_file.write("\n")
        for author in authors:
            text_file.write(author.contents[0])
            text_file.write("\n")
except requests.exceptions.RequestException as e:    # This is the correct syntax
    print(e)

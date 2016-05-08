"""This is a web scraper made for the Daily Bruin."""

from bs4 import BeautifulSoup
import requests
import json

'''To run it yourself:
    1. pip install requests
    2. pip install beautifulsoup4
'''

"""special characters like: ”  """
def removeSpecialCharacters(string):
    string = string.replace("”", "\"")
    string = string.replace("“", "\"")
    string = string.replace("’", "\'")
    string = string.replace("–", "\'")
    return string

try:
    r = requests.get("http://dailybruin.com/2016/05/06/bruins-united-sails-past-waves-of-change-in-2016-usac-election/")
    soup = BeautifulSoup(r.content, "html.parser")

    headline = soup.find("div", class_="db-post-headline")
    authors = soup.find("div", class_="db-byline").find_all("a")
    tempList = []
    for author in authors:
        tempList.append(str(author))
    story = soup.find("div", class_="db-post-content").text

    obj = {u"headline": str(headline), u"authors": tempList}

    print(json.dumps(obj, indent=4))
    with open("output.txt", "w") as text_file:
        text_file.write("working")
        print("GOOD!")
except requests.exceptions.RequestException as e:    # This is the correct syntax
    print(e)

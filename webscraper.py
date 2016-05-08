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
    r = requests.get("http://dailybruin.com/2016/05/06/students-approve-all-four-referenda-on-usac-election-ballot/")
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
    imageLink = str(soup.find("div", class_="db-image text-center")).split("src=")[1].split("width=")[0].split("-")[0]
    image = "<img src=" + imageLink + ".jpg\">"
    imageCaption = str(soup.find("p", class_="db-image-caption").text).replace("\t", "").replace("\n", "")

    obj = {u"headline": headline, u"postDate": postingDate, u"authors": tempList, u"image": image, u"caption": imageCaption, u"content": story}

    print(json.dumps(obj, indent=4))
    with open("output.txt", "w") as text_file:
        text_file.write(json.dumps(obj, indent=4))
        print("GOOD!")
except requests.exceptions.RequestException as e:    # This is the correct syntax
    print(e)

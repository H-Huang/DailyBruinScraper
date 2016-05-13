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
    "http://dailybruin.com/2015/11/18/freshman-runner-makes-big-impact-at-ucla-following-european-success/",
    "http://dailybruin.com/2015/10/27/report-card-ucla-vs-cal/"

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
        story = str(story).split("\n<!-- Simple Share Buttons Adder")[0]
        story = story + "</div>"
        dates = soup.find_all("h5")
        postingDate = ""
        for date in dates:
            postingDate += str(date.text)
        regex1 = re.compile('.*wp-post-image.*')
        mainImage = soup.find("img", {"class": regex1})

        #trying to fetch image
        try:
            imageLink = str(mainImage).split("src=")[1]
            imageLink = re.sub(r'-\d\d\dx\d\d\d', '', imageLink)
            imageLink = imageLink.split("width=")[0][:-1]
            mainImage = imageLink[1:-1]
        except:
            mainImage = ""

        #trying to get title image caption
        try:
            imageCaption = str(soup.find("p", class_="db-image-caption").text).replace("\t", "").replace("\n", "")
        except:
            imageCaption = ""

        secondaryImages = []
        regex2 = re.compile('.*wp-image.*')
        images = soup.find_all("img", {"class": regex2})
        #trying to get secondary images
        try:
            for image in images:
                imageLink = str(image).split("src=")[1]
                imageLink = re.sub(r'-\d\d\dx\d\d\d', '', imageLink)
                imageLink = imageLink.split("width=")[0][:-1][1:-1]
                secondaryImages.append(imageLink)
        except:
            continue

        secondaryImageCaptions = []
        captions = soup.find_all("figcaption")
        #trying to get secondaryImageCaptions
        try:
            for caption in captions:
                secondaryImageCaptions.append(caption.text)
        except:
            continue

        #APPEND EVERYTHING INTO THIS MASSIVE JSON OBJECT YAYAYYAAA
        obj.append({u"headline": headline, u"postDate": postingDate, u"authors": tempList, u"content": story,
                    u"titleImage": mainImage, u"titleCaption": imageCaption, u"url": url, u"secondaryImages": secondaryImages,
                    u"secondaryImageCaptions": secondaryImageCaptions})


        #If you want to see the JSON object outputted in terminal, uncomment the line below
        #print(json.dumps(obj, indent=4))

        #text file for viewing in output.txt
        with open("output.txt", "w") as text_file:
            text_file.write(json.dumps(obj, indent=4))
            print("URL number " + str(count) + " scraped" + " (" + str(url) + ")")
            count += 1

        #actual json data in data.json
        with open('data.json', 'w') as f:
            json.dump(obj, f)

    except requests.exceptions.RequestException as e:
        print(e)

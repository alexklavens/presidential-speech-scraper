from bs4 import BeautifulSoup
from urllib import request
import pprint
from datetime import datetime
import math
import json

def getSpeech(url):
    html = request.urlopen(url).read()
    soup = BeautifulSoup(html,'html.parser')

    date = soup.find_all("span", {"class": "date-display-single"})[0].get_text()
    speaker = soup.find_all("div", {"class": "field-title"})[0].get_text()
    speech_title = soup.find_all("div",{"class": "field-ds-doc-title"})[0].get_text()

    speech_text = soup.find_all("div", {"class": "field-docs-content"})[0].get_text()

    thisSpeech = {
        "name":speaker.replace("\n", "").strip(),
        "date":date,
        "title":speech_title,
        "speechText":speech_text
    }

    return thisSpeech

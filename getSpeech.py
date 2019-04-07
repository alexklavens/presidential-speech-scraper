from bs4 import BeautifulSoup
from urllib import request
import pprint
from datetime import datetime
import math
import json
import utils

def getSpeech(url):
    html = request.urlopen(url).read()
    soup = BeautifulSoup(html,'html.parser')

    date = soup.find_all("span", {"class": "date-display-single"})[0].get_text()
    speaker = soup.find_all("div", {"class": "field-title"})[0].get_text()
    speech_title = soup.find_all("div",{"class": "field-ds-doc-title"})[0].get_text()

    speech_text = soup.find_all("div", {"class": "field-docs-content"})[0].get_text()

    ############## get location of speech
    try:
        location = soup.find_all("div", {"class":"field-spot-state"})[0].get_text()
    except:
        location = ""


    ############### get categories
    filed_under = soup.find_all("div", {"class": "group-meta"})[0]
    links = [a.get('href') for a in filed_under.find_all('a')]

    # categories
    cat, categories = "app-categories/", []
    att, attributes = "app-attributes/", []

    for link in links:
        if cat in link:
            category_path = link[link.find(cat)+len(cat)-1:]
            category_main = category_path[1:]

            sub_category = None
            if "/" in category_path[1:]:
                category_main = category_main[:category_main.find("/")]
                sub_category = category_path[category_path[1:].find("/")+2:]
                # category_name = sub_category

            thisCat = {
                "category": category_main,
                "sub_category": sub_category,
                "category_path": category_path,
            }

            categories.append(thisCat)

        elif att in link:
            #### Unclear if there exist sub attributes, but this is backup
            attribute_path = link[link.find(att)+len(att)-1:]
            attribute_main = attribute_path[1:]

            sub_attribute = None
            if "/" in attribute_path[1:]:
                attribute_main = attribute_main[:attribute_main.find("/")]
                sub_attribute = attribute_path[attribute_path[1:].find("/")+2:]

            thisAtt = {
                "attribute": attribute_main,
                "sub_attribute": sub_attribute,
                "attribute_path": attribute_path
            }
            attributes.append(thisAtt)


    thisSpeech = {
        "name":utils.cleanString(speaker),
        "date":utils._formatDate(date),
        "location":utils.cleanString(location),
        "title":utils.cleanString(speech_title),
        "speech_text":speech_text,
        "categories":categories,
        "attributes":attributes
    }
    return thisSpeech

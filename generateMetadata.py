from bs4 import BeautifulSoup
from urllib import request
import pprint
from datetime import datetime
import math
import json
import utils
import getSpeech
import time


def getLastIndex(soup):
    lastPage = soup.find_all("li", {"class": "pager-last"})
    if len(lastPage) == 0:
        return -1

    lastPageLiString = str(lastPage[0])
    indexOfURLTag = (lastPageLiString.find(";page="))

    stringFromThatTagOnward = lastPageLiString[indexOfURLTag:]
    numberBegining = stringFromThatTagOnward.find("=")+1
    index_that_finishes_page_number = stringFromThatTagOnward.find("\"")

    return stringFromThatTagOnward[numberBegining:index_that_finishes_page_number]


def _getOneTable(url):
    html = request.urlopen(url).read()
    soup = BeautifulSoup(html,'html.parser')
    table = soup.find('tbody')
    if table == None:
        return False

    data = []
    for row in table.find_all("tr"):
        cols = row.find_all('td')
        cols = [item.text.strip() for item in cols] #https://stackoverflow.com/questions/23377533/python-beautifulsoup-parsing-table
        thisRow = [item for item in cols if item]
        thisRow[0] = utils._formatDate(thisRow[0])

        this_speech_local_link = [link.get('href') for link in row.find_all('a') if ("/documents/" in link.get('href'))][0]
        speech_page_link = "https://www.presidency.ucsb.edu{}".format(this_speech_local_link)
        thisRow.append(speech_page_link)

        thisItem = {
            "date": thisRow[0],
            "speaker": thisRow[1],
            "title": thisRow[2],
            "speech_url": thisRow[3]
        }

        data.append(thisItem)


    return data

def tableMetadataFromURL(startingUrl):
    """
    From a given base URL where there exists a table,
    returns a list of dictionary objects that contain
    indivudal speech metadata including:
        date,
        speaker,
        title,
        speech_url (this is the most important one, because it provides a link to the webpage at which that speech is stored)
    """

    html = request.urlopen(startingUrl).read()
    soup = BeautifulSoup(html,'html.parser')

    allData = []
    start = datetime.now()
    firstTable = _getOneTable(startingUrl)
    finish = datetime.now()
    if firstTable == False:
        return None

    allData += firstTable

    lastTableIndex = int(getLastIndex(soup))
    if lastTableIndex != -1:
        utils.printEstimatedCompletionTime(start,finish,lastTableIndex,processName="Generating the metadata")

        for i in range(1,lastTableIndex+1):

            newUrl = "{}{}{}".format(startingUrl,"&page=",str(i))
            allData += _getOneTable(newUrl)

    print("Process Complete\n")
    return allData


def generateMetadataJSON(speechDataObjects,outfile):
    """
    Generates a JSON file from requested python list of dictionaries.

    Filename defaults to your current date and time.
    """

    with open(outfile,'w') as file:
        thisJsonStr = json.dumps(speechDataObjects)
        file.write(thisJsonStr)

    return outfile


def makeSpeechJSON(infile,outfile):
    with open(infile,'r') as file:
        allData = json.load(file)

    allSpeeches = []

    first = True
    start = datetime.now()

    for item in allData:
        newSpeech = getSpeech.getSpeech(item["speech_url"])
        if first:
            finish = datetime.now()
            utils.printEstimatedCompletionTime(start,finish,len(allData),processName="Scraping speeches")
            first = False


        allSpeeches.append(newSpeech)

    print('Process Complete\n')

    with open(outfile,'w') as file:
        thisJsonStr = json.dumps(allSpeeches)
        file.write(thisJsonStr)

    return outfile


if __name__ == '__main__':

    url = "https://www.presidency.ucsb.edu/advanced-search?field-keywords=&field-keywords2=&field-keywords3=&from%5Bdate%5D=&to%5Bdate%5D=&person2=&category2%5B%5D=46&items_per_page=25"
    allData = tableMetadataFromURL(url)

    generateMetadataJSON(allData)

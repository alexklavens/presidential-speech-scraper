from bs4 import BeautifulSoup
from urllib import request
import pprint
from datetime import datetime
import math
import json




"""
First, make a module that returns a list, text file, csv, whatever, of presidential speech metadata

One field must associate all speeches to a URL where you can access that speech directly.


PresidentialSpeeches(mainURL):
    return csv(date,president,document title,url)

"""

"""
To go to all the pages, loop from the first, to page = 1, to page = {the last number in the 'last' url}

"""

def _formatDate(dateString):
    month_lst = ['january', 'february', 'march', 'april', 'may', 'june', 'july',
              'august', 'september', 'october', 'november', 'december']

    month = dateString.split()
    for m in month_lst:
        if month[0].lower() in m:
            return str(datetime.strptime(('{} {}, {}'.format(m.title(),month[1][:-1],month[2])),'%B %d, %Y'))


def getLastIndex(soup):
    lastPage = soup.find_all("li", {"class": "pager-last"})
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
    # print(table)

    data = []
    for row in table.find_all("tr"):
        cols = row.find_all('td')
        cols = [item.text.strip() for item in cols] #https://stackoverflow.com/questions/23377533/python-beautifulsoup-parsing-table
        thisRow = [item for item in cols if item]
        thisRow[0] = _formatDate(thisRow[0])

        this_speech_local_link = [link.get('href') for link in row.find_all('a') if ("/documents/" in link.get('href'))][0]
        speech_page_link = "https://www.presidency.ucsb.edu{}".format(this_speech_local_link)
        thisRow.append(speech_page_link)
        # if len(thisRow) > 4:
        #     pprint.pprint(thisRow)
        data.append(thisRow)


    return data


def estimateCompletionTime(lastTime,currentTime,remainingIterations):
    interval = currentTime - lastTime
    duration_in_s = interval.total_seconds()      # Total number of seconds between dates

    timeLeft = remainingIterations * duration_in_s

    minutes = timeLeft//60
    seconds = timeLeft%60
    print("This should take about",int(minutes),"minutes and",int(seconds),"seconds.")


def getMetaData(startingUrl):
    """
    From a given base URL where there exists a table,
    returns a list of lists, with each list containing metadata of a presidential speech.
    """

    # with open(url,'rb') as file:
    html = request.urlopen(url).read()
    soup = BeautifulSoup(html,'html.parser')

    lastTableIndex = int(getLastIndex(soup)) ### does not yet work for one pagers, should have a IF THERE IS MORE THAN ONE
    allData = []
    start = datetime.now()
    firstTable = _getOneTable(startingUrl)
    estimateCompletionTime(start,datetime.now(),lastTableIndex-1)

    allData += firstTable

    # for i in range(1,int(getLastIndex(soup))+1):
    for i in range(1,lastTableIndex+1):

        newUrl = "{}{}{}".format(startingUrl,"&page=",str(i))
        allData += _getOneTable(newUrl)

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
    # r = json.dumps(thisSpeech)
    # with open('test.json','w') as file:
    #     file.write(r)

    # print(speech_text)
    # print(thisSpeech)


if __name__ == '__main__':
    # url = "https://www.presidency.ucsb.edu/advanced-search?field-keywords=&field-keywords2=&field-keywords3=&from%5Bdate%5D=&to%5Bdate%5D=&person2=&items_per_page=100"
    # getMetaData(url)

#block-system-main > div > div > div.col-sm-8 > div.field-docs-content
# //*[@id="block-system-main"]/div/div/div[1]/div[3]
    urlSpeech = "https://www.presidency.ucsb.edu/documents/special-message-3361"
    getSpeech(urlSpeech)

# presidential-speech-scraper

## About

This is a program that scrapes search results from the American Presidency Project, an online repository of presidential documentation. I created this for the purpose of accessing documents for a natural language processing research project.

Currently, the program works in conjunction with the APP's advanced search tool. Based on a given search result (a table of document links), this program generates two JSON files. The first is a metadata file, where each object looks like this:

```JSON
{
  "date": "1789-04-30",
  "speaker": "George Washington",
  "title": "Inaugural Address",
  "speech_url": "https://www.presidency.ucsb.edu/documents/inaugural-address-16"
}
```

## Install Requirements

* Install requirements


## Run the program

```
>>> python3.6 app.py
```


To run your own query:

1. Go to the American Presidency Project's [advanced search tool](https://www.presidency.ucsb.edu/advanced-search)
2. Either click search, or make a filtered search.
3 Assign the URL from your search results table into to the  `STARTING_URL` variable in `app.py`.
4. From the command line:

```
>>> python3.6 app.py
```


## Things that won't work perfectly

Speaker Names.

Most (all, but I can't promise they all work!) pages seem to attribute authorship to someone or something. Sometimes, those documents are incorrectly attributed. For example the site attributes a [Sean Spicer press briefing](https://www.presidency.ucsb.edu/documents/press-gaggle-press-secretary-sean-spicer-1) to President Trump, even though the President does not speak. This seems to be a common issue with many press briefings, though many briefings are attributed to the actual briefer.  

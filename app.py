from bs4 import BeautifulSoup
from urllib import request
import pprint
from datetime import datetime
import math
import json

import generateMetadata


# Step 1. Set your parameters

EXAMPLE_INAUGURAL_URL = "https://www.presidency.ucsb.edu/advanced-search?field-keywords=&field-keywords2=&field-keywords3=&from%5Bdate%5D=&to%5Bdate%5D=&person2=&category2%5B%5D=46&items_per_page=25"
STARTING_URL = EXAMPLE_INAUGURAL_URL

metadata_filename = "results/APP_Speech_Metadata_{}.json".format(datetime.now().strftime("%Y-%m-%d__%H:%M:%S"))
speeches_filename = "results/APP_Speech_Speeches_{}.json".format(datetime.now().strftime("%Y-%m-%d__%H:%M:%S"))


# Gets all the rows of your table
list_of_dictionaries = generateMetadata.tableMetadataFromURL(STARTING_URL)

# Make your metadata JSON file
generateMetadata.generateMetadataJSON(speechDataObjects = list_of_dictionaries,outfile = metadata_filename)

# From that metadata file, make your JSON file that contains all the speeches
generateMetadata.makeSpeechJSON(infile = metadata_filename, outfile = speeches_filename)

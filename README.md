# presidential-speech-scraper

## About

This is a program that makes documents related to the American presidency programmatically accessible. It scrapes search results from the [American Presidency Project](https://www.presidency.ucsb.edu/), a massive online repository of presidential documentation. I created this for the purpose of accessing documents for a natural language processing research project.

Currently, the program works in conjunction with the APP's advanced search tool. Based on a given search result (a table of document links), this program generates two JSON files. The first is a metadata file. The second contains speech text and categorizations.

Please find two example files (presidential inaugurals) in the `example_data` folder.

## Requirements

This program runs on Python and BeautifulSoup (bs4). I recommend using Python 3.6.

```
>>> pip install beautifulsoup4
```

## Run the program

The program will scrape a search result table from the American Presidency Project.


Its default is to scrape presidential inaugural addresses. To run this, don't change any code and run `app.py` from the command line:

```
>>> python3.6 app.py
```


To run your own query:

1. Go to the American Presidency Project's [advanced search tool](https://www.presidency.ucsb.edu/advanced-search)

2. Either click search (no filters will get you over 129 thousand documents), or make a filtered search.

3. Assign the URL from your search results table into to the  `STARTING_URL` variable in `app.py`.

```python
# app.py
EXAMPLE_INAUGURAL_URL = "https://www.presidency.ucsb.edu/advanced-search?field-keywords=&field-keywords2=&field-keywords3=&from%5Bdate%5D=&to%5Bdate%5D=&person2=&category2%5B%5D=46&items_per_page=25"
STARTING_URL = EXAMPLE_INAUGURAL_URL # replace this one
```

For example, to get State of the Union addresses, reassign `STARTING_URL`.
```python
STARTING_URL = "https://www.presidency.ucsb.edu/advanced-search?field-keywords=&field-keywords2=&field-keywords3=&from%5Bdate%5D=&to%5Bdate%5D=&person2=&category2%5B%5D=45&items_per_page=25"
```

4. Given a URL that points to a results table, run the program from the command line:

```
>>> python3.6 app.py
```

## Results

The program will generate two files. Those files are set to be stored in the `results` folder. They are automatically named with the date and time you run the program.

The first is a metadata file that is a JSON representation of the scraped results table. Here's what one entry in that file will look like:

```JSON
{
  "date": "1789-04-30",
  "speaker": "George Washington",
  "title": "Inaugural Address",
  "speech_url": "https://www.presidency.ucsb.edu/documents/inaugural-address-16"
}
```

The second file contains actual speech information, including speech text. This information comes from individual document pages.

Here's the George Washington Inaugural:

```JSON
{
  "name": "George Washington",
  "date": "1789-04-30",
  "location": "New York",
  "title": "Inaugural Address",
  "speech_text": "\nFellow-Citizens of the Senate and of the House of Representatives:\nAmong the vicissitudes incident to life no event could have filled me with greater anxieties than that of which the notification was transmitted by your order, and received on the 14th day of the present month. On the one hand, I was summoned by my country, whose voice I can never hear but with veneration and love, from a retreat which I had chosen with the fondest predilection, and, in my flattering hopes, with an immutable decision, as the asylum of my declining years—a retreat which was rendered every day more necessary as well as more dear to me by the addition of habit to inclination, and of frequent interruptions in my health to the gradual waste committed on it by time. On the other hand, the magnitude and difficulty of the trust to which the voice of my country called me, being sufficient to awaken in the wisest and most experienced of her citizens a distrustful scrutiny into his qualifications, could not but overwhelm with despondence one who (inheriting inferior endowments from nature and unpracticed in the duties of civil administration) ought to be peculiarly conscious of his own deficiencies. In this conflict of emotions all I dare aver is that it has been my faithful study to collect my duty from a just appreciation of every circumstance by which it might be affected. All I dare hope is that if, in executing this task, I have been too much swayed by a grateful remembrance of former instances, or by an affectionate sensibility to this transcendent proof of the confidence of my fellow-citizens, and have thence too little consulted my incapacity as well as disinclination for the weighty and untried cares before me, my error will be palliated by the motives which mislead [see APP note] me, and its consequences be judged by my country with some share of the partiality in which they originated.\nSuch being the impressions under which I have, in obedience to the public summons, repaired to the present station, it would be peculiarly improper to omit in this first official act my fervent supplications to that Almighty Being who rules over the universe, who presides in the councils of nations, and whose providential aids can supply every human defect, that His benediction may consecrate to the liberties and happiness of the people of the United States a Government instituted by themselves for these essential purposes, and may enable every instrument employed in its administration to execute with success the functions allotted to his charge. In tendering this homage to the Great Author of every public and private good, I assure myself that it expresses your sentiments not less than my own, nor those of my fellow-citizens at large less than either. No people can be bound to acknowledge and adore the Invisible Hand which conducts the affairs of men more than those of the United States. Every step by which they have advanced to the character of an independent nation seems to have been distinguished by some token of providential agency; and in the important revolution just accomplished in the system of their united government the tranquil deliberations and voluntary consent of so many distinct communities from which the event has resulted can not be compared with the means by which most governments have been established without some return of pious gratitude, along with an humble anticipation of the future blessings which the past seem to presage. These reflections, arising out of the present crisis, have forced themselves too strongly on my mind to be suppressed. You will join with me, I trust, in thinking that there are none under the influence of which the proceedings of a new and free government can more auspiciously commence.\nBy the article establishing the executive department it is made the duty of the President \"to recommend to your consideration such measures as he shall judge necessary and expedient.\" The circumstances under which I now meet you will acquit me from entering into that subject further than to refer to the great constitutional charter under which you are assembled, and which, in defining your powers, designates the objects to which your attention is to be given. It will be more consistent with those circumstances, and far more congenial with the feelings which actuate me, to substitute, in place of a recommendation of particular measures, the tribute that is due to the talents, the rectitude, and the patriotism which adorn the characters selected to devise and adopt them. In these honorable qualifications I behold the surest pledges that as on one side no local prejudices or attachments, no separate views nor party animosities, will misdirect the comprehensive and equal eye which ought to watch over this great assemblage of communities and interests, so, on another, that the foundation of our national policy will be laid in the pure and immutable principles of private morality, and the preeminence of free government be exemplified by all the attributes which can win the affections of its citizens and command the respect of the world. I dwell on this prospect with every satisfaction which an ardent love for my country can inspire, since there is no truth more thoroughly established than that there exists in the economy and course of nature an indissoluble union between virtue and happiness; between duty and advantage; between the genuine maxims of an honest and magnanimous policy and the solid rewards of public prosperity and felicity; since we ought to be no less persuaded that the propitious smiles of Heaven can never be expected on a nation that disregards the eternal rules of order and right which Heaven itself has ordained; and since the preservation of the sacred fire of liberty and the destiny of the republican model of government are justly considered, perhaps, as deeply, as finally, staked on the experiment entrusted to the hands of the American people.\nBesides the ordinary objects submitted to your care, it will remain with your judgment to decide how far an exercise of the occasional power delegated by the fifth article of the Constitution is rendered expedient at the present juncture by the nature of objections which have been urged against the system, or by the degree of inquietude which has given birth to them. Instead of undertaking particular recommendations on this subject, in which I could be guided by no lights derived from official opportunities, I shall again give way to my entire confidence in your discernment and pursuit of the public good; for I assure myself that whilst you carefully avoid every alteration which might endanger the benefits of an united and effective government, or which ought to await the future lessons of experience, a reverence for the characteristic rights of freemen and a regard for the public harmony will sufficiently influence your deliberations on the question how far the former can be impregnably fortified or the latter be safely and advantageously promoted.\nTo the foregoing observations I have one to add, which will be most properly addressed to the House of Representatives. It concerns myself, and will therefore be as brief as possible. When I was first honored with a call into the service of my country, then on the eve of an arduous struggle for its liberties, the light in which I contemplated my duty required that I should renounce every pecuniary compensation. From this resolution I have in no instance departed; and being still under the impressions which produced it, I must decline as inapplicable to myself any share in the personal emoluments which may be indispensably included in a permanent provision for the executive department, and must accordingly pray that the pecuniary estimates for the station in which I am placed may during my continuance in it be limited to such actual expenditures as the public good may be thought to require.\nHaving thus imparted to you my sentiments as they have been awakened by the occasion which brings us together, I shall take my present leave; but not without resorting once more to the benign Parent of the Human Race in humble supplication that, since He has been pleased to favor the American people with opportunities for deliberating in perfect tranquillity, and dispositions for deciding with unparalleled unanimity on a form of government for the security of their union and the advancement of their happiness, so His divine blessing may be equally conspicuous in the enlarged views, the temperate consultations, and the wise measures on which the success of this Government must depend.\n",
  "categories": [
    {
      "category": "spoken-addresses-and-remarks",
      "sub_category": null,
      "category_path": "/spoken-addresses-and-remarks"
    },
    {
      "category": "spoken-addresses-and-remarks",
      "sub_category": "inaugural-addresses",
      "category_path": "/spoken-addresses-and-remarks/inaugural-addresses"
    },
    {
      "category": "presidential",
      "sub_category": null,
      "category_path": "/presidential"
    }
  ],
  "attributes": [
    {
      "attribute": "inaugural",
      "sub_attribute": null,
      "attribute_path": "/inaugural"
    }
  ]
}

```

## Querying this data

This program does not currently provide querying functions. But you can write your own programs that filter the JSON data based on speakers, dates, categories, and more.

## Things that won't work perfectly

Speaker/author names. Most (all, but I can't promise they all work!) pages seem to attribute authorship to someone or something. Sometimes, those documents are incorrectly attributed. For example the site attributes a [Sean Spicer press briefing](https://www.presidency.ucsb.edu/documents/press-gaggle-press-secretary-sean-spicer-1) to President Trump, even though the President does not speak. This seems to be a common issue with many press briefings, though there still are many briefings are attributed to the actual briefer.  


## Next steps

The next stage for this project is creating an API-like method of accessing this information without needing to copy and paste URLs or download this repository.

First next step: rather than requiring the user to find their own URL, I hope to implement my own interface for filtering the APP's advanced search.

Second next step: rather than requiring the user to download this repository and run this particular python program, I hope to set up an API that, based on user queries, runs the scraping on a web app and sends the user a JSON response.

Third next step: rather than having an API make redundant scrapes of documents that haven't changed in hundreds of years, I hope to store the information in some sort of database that is automatically updated daily. This would mean when a user calls the API, it does not need to scrape anything, but can more efficiently return desired documents.

The ideal solution to making these documents programmatically accessible would be for the APP website to have its own API.

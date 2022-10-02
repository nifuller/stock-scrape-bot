# Scrapy Stock Bot
![](https://img.shields.io/badge/contributors-1-green) ![](https://img.shields.io/badge/forks-0-blue) ![](https://img.shields.io/badge/stars-0-blue) ![](https://img.shields.io/badge/license-MIT-orange) ![](https://img.shields.io/badge/issues-0%20open-green)


## Description
A Scrapy bot that gathers data from the most active stocks on Yahoo Finance. In order to continously collect most active stocks data, the Scrapy bot is deployed on DigitalOcean. With the bot deployed on DigitalOcean, it was easy to integrate Scrapyd and ScrapyOP within the bot to create a scheduler. The bot continuously gathers stock data, Monday through Friday at 1600 est. After the bot collects the data, it feeds it into a pipeline where the data is cleansed (removes unwanted data or duplicates) and converts it into the data format that is needed. (In this case I needed XML format, so the pipeline creates a XML file). Then, the bot then sends over the cleansed and new data format, it is sent to a data lake which is hosted on AWS. Now that the data is properly and securly stored on AWS, the data can be pulled from the data lake and placed into an Iceberg SQL data table which is hosted locally through Docker. Through docker we can use Spark to query the SQL data for analysis.

### Technologies & Packages Used
- Scrapy
- Scrapyd & Scrapyop
- Digital Ocean
- AWS
- Iceberg & Spark
- Docker

### Challenges
While working on this project, I have came across several challenging issues, most of which were just trying to install some of the technologies on my local machine (Scrapy & Docker). Other than those issues, the only real issue I had was writing an XML pipeline. Writing the XML pipeline code, was rough due to the poor documentation on Scrapy pipelines and the lack of XML examples within the documentation. 

### Future Features
- Deploy multiple spiders to gather different stock data at once 
- Have rotating IP addresses so my spiders can avoid being banned
- Set up an autothrottle for the spider so it doesnt access the site too fast

## Installation
The following steps will help get **ONLY** the webcrawler working on your local machine. It will not be hooked up to any of the servers. 

1. clone the project
2. create a virtual environment

`python3 -m venv scrapy-virtenv`

3. start virtual environment

`source scrapy-virtenv/scripts/activate`

or

`source scrapy-virtenv/bin/activate`

4. install the following packages through pip3:
    - `pip3 install scrapy`
    
    **Note:** If you're getting an import scrapy error in _most-active.py_ file make sure you 
    select the correct Python interpreter; Ctrl + Shift + P, Python: select Interpreter (then whatever is
    the correct one for you)
    
    - `pip3 install scrapyd`
    - `pip3 install scrapyops-scrapy`

**Note:** The last two packages aren't needed to get the web crawler to work. They are only needed to get the crawler ready for deployment onto a server. If you're not interested in deploying the crawler, don't install the last two packages.

## Running the Web Crawler
First, activate the virtual enviornment:

`source scrapy-virtenv/scripts/activate`

or

`source scrapy-virtenv/bin/activate`

Then, cd into the spider directory: 

`cd stock_scrapy`

Finally, run the following script to activate the scrapy bot:

`scrapy crawl mostactive`

Once the crawler finishes, an XML file called _mostactive.xml_ will be outputed. 

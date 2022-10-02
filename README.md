# Scrapy Stock Bot
![](https://img.shields.io/badge/contributors-1-green) ![](https://img.shields.io/badge/forks-0-blue) ![](https://img.shields.io/badge/stars-0-blue) ![](https://img.shields.io/badge/license-MIT-orange) ![](https://img.shields.io/badge/issues-0%20open-green)


## Description
A Scrapy bot that gathers data from the most active stocks on Yahoo Finance. In order to continously collect most active stocks data, the Scrapy bot is deployed on DigitalOcean. With the bot deployed on DigitalOcean, it was easy to integrate Scrapyd and ScrapyOP within the bot to create a scheduler. The bot continuously gathers stock data, Monday through Friday at 1600 est. After the bot collects the data, it feeds it into a pipeline where the data is cleansed (removes unwanted data or duplicates) and converts it into the data format that is needed. (In this case I needed XML format, so the pipeline creates a XML file). Then, the bot then sends over the cleansed and new data format, it is sent to a data lake which is hosted on AWS. Now that the data is properly and securly stored on AWS, the data can be pulled from the data lake and placed into an Iceberg SQL data table which is hosted locally through Docker. Through docker we can use Spark to query the SQL data for analysis.

### Technologies & Packages Used
- Scrapy
- Scrapyd & ScrapyOP
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
The following will get just the spider up and running on your local machine:
1. clone the project
2. create a virtual environment
3. start virtual environment
4. pip install the following packages:
    - scrapy
    - scrapyd
    - scrapyops-scrapy


## Using the Project
First activate the virtual enviornment,

source [name of virtenv]/scripts/activate

Then cd into the spider directory 

cd stock_scrapy

Finally, run the following script to activate the scrapy bot

scrapy crawl mostactive

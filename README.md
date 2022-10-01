# Scrapy Stock Bot
A Scrapy bot that gathers data from the most active stocks on Yahoo Finance. In order to continously collect most active stocks data, the Scrapy bot is deployed on DigitalOcean. From there, a scheduler is setup using Scrapyd and ScrapyOP so that the bot can scrap the stock data after the US stock market closes at 16:00 est, Monday through Friday. Once the bot finishes gathering the stock data, it feeds it into a pipeline to create a XML file. Then, the bot then sends over the newly created XML file to a data lake which is hosted on AWS. When the data is properly stored on AWS, it is placed into an Iceberg SQL data where it can be queried through Spark for analysis.

# List of Technologies used
- DigitalOcean
- AWS 
- Iceberg & Spark

# To-Do-List
1. ~~Accquire data~~
2. ~~Cleanse the data~~
3. ~~Convert the data to correct format~~ 
4. Hookup spider to a scheduler to scrape data over a certain time period (scrapyard)
5. Interpreting data that could be interpreted in multiple ways (Need to look more into this)
6. Remove duplicates of the data
7. Store data on a cloud service (most likely AWS)
8. Create a SQL database to query data (Iceberg & Spark)

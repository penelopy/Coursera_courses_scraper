Coursera Courses Scraper
================
This scraper uses selenium to mimic the browser and scrape all English language classes listed on Coursera.</br>
The scraped course data is parsed with Beautiful Soup and each class is saved to a Postgres database.  



**Tech Stack**
 
Python, BeautifulSoup, Selenium,
SQLAlchemy, 
PostgreSQL, Unittest

**Notable Features**
 
1. Uses regex to extract complex date strings from html tags. </br>
2. Uses unittest testing framework to perform the following tests: </br>
	- "test_scrape_data_from_coursera" -- Validates that the content of a dummy html file is correctly captured by Beautiful Soup. </br>
	-  "test_create_text_file_returns_correct_result" -- Validates that the scraped data is formatted correctly before being written to file.

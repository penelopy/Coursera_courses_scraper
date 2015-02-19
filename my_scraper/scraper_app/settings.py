BOT_NAME = 'coursera'

SPIDER_MODULES = ['scraper_app.spiders']

ITEM_PIPELINES = ['scraper_app.pipelines.CourseraPipeline']

DATABASE = {
    'drivername': 'postgres',
    'host': 'localhost',
    'port': '5432',
    'username': 'penelopehill',  # fill in your username here
    'password': ' ',  # fill in your password here
    'database': 'db_coursera'


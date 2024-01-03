from scrapeghost import SchemaScraper, CSS
from pprint import pprint
from .redflagdeals_scraper import *

url = "https://comedybangbang.fandom.com/wiki/Operation_Golden_Orb"
schema = {
    "title": "str",
    "episode_number": "int",
    "release_date": "YYYY-MM-DD",
    "guests": [{"name": "str"}],
}

episode_scraper = SchemaScraper(
    schema,
    # can pass preprocessor to constructor or at scrape time
    extra_preprocessors=[CSS("div.page-content")],
)

response = episode_scraper(url)
pprint(response.data)
print(f"Total Cost: ${response.total_cost:.3f}")

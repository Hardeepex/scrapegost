from scrapeghost import SchemaScraper, CSS
from .redflagdeals_scraper import *

episode_list_scraper = SchemaScraper(
    "url",
    auto_split_length=2000,
    extra_preprocessors=[CSS(".mw-parser-output a[class!='image link-internal']")],
)
response = episode_list_scraper(
    "https://comedybangbang.fandom.com/wiki/Category:Episodes"
)

episode_urls = response.data
print(episode_urls[:3])
print(episode_urls[-3:])
print("total:", len(episode_urls))
print(f"Total Cost: ${response.total_cost:.3f}")

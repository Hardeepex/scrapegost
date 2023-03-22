from scrapeghost import SchemaScraper, CSS

episode_list_scraper = SchemaScraper(
    "url",
    auto_split_length=2048,
    extra_preprocessors=[CSS(".mw-parser-output a[class!='image link-internal']")],
)
episode_urls = episode_list_scraper(
    "https://comedybangbang.fandom.com/wiki/Category:Episodes"
)

print(episode_urls[:3])
print(episode_urls[-3:])
print("total:", len(episode_urls))
print("cost:", episode_list_scraper.total_cost)
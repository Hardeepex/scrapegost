import json

from scrapeghost import CSS, SchemaScraper

# Define the SchemaScraper for the main page and listings
listings_scraper = SchemaScraper(
    {
        "url": "url",
        "title": "str",
        "image": "str",
        "dealer": "str",
        "comments_count": "int",
    },
    extra_preprocessors=[CSS("div.list_item")],
)

# Define the SchemaScraper for the single deal pages
deal_scraper = SchemaScraper(
    {
        "title": "str",
        "url": "url",
        "price": "float",
        "regular_price": "float",
        "details": "str",
    },
    extra_preprocessors=[CSS("div.primary_content")],
)

# Scrape data from the website
response = listings_scraper("https://www.redflagdeals.com/deals/")
listings = response.data

deal_data = []
for listing in listings:
    response = deal_scraper(listing["url"])
    deal_data.append(response.data)

# Save the scraped data to a JSON file
with open("redflagdeals_data.json", "w") as f:
    json.dump(deal_data, f, indent=2)

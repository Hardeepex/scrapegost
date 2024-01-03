import requests
from scrapeghost import SchemaScraper
from selectolax.parser import HTMLParser


def process_html(html_string):
    parser = HTMLParser(html_string)
    main_data = parser.css('main')

    schema = {"main_data": "str"}
    scraper = SchemaScraper(schema)
    result = scraper.scrape(main_data)

    return result.data

if __name__ == "__main__":
    url = 'https://example.com'
    response = requests.get(url)
    html_string = response.text

    result = process_html(html_string)
    print(result)

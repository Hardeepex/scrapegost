import unittest

from scrapeghost import CSS, SchemaScraper


class TestNewScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = SchemaScraper(
            {
                "url": "url",
                "title": "str",
                "image": "str",
                "dealer": "str",
                "comments_count": "int",
            },
            extra_preprocessors=[CSS("div.list_item"), CSS("a.offer_image"), CSS("h2.offer_title"), CSS("p.offer_description")],
        )

    def test_scrape(self):
        test_webpage = """
        <div class="list_item">
            <a href="test_url" class="offer_image">
                <img src="test_image.jpg">
            </a>
            <div class="list_item_body">
                <p class="offer_dealer">Test Dealer</p>
                <h2 class="offer_title">Test Title</h2>
                <p class="offer_description">Test Description</p>
            </div>
            <ul class="list_item_counters">
                <li class="offer_comment_counter">5</li>
            </ul>
        </div>
        """
        result = self.scraper.scrape(test_webpage)
        expected_data = {
            "url": "test_url",
            "title": "Test Title",
            "image": "test_image.jpg",
            "dealer": "Test Dealer",
            "comments_count": 5,
        }
        self.assertEqual(result.data, expected_data)

if __name__ == "__main__":
    unittest.main()

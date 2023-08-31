import scrapy
from scrapy.exceptions import CloseSpider
from scrapy.crawler import CrawlerProcess


class PDFSpider(scrapy.Spider):
    name = "pdf_spider"
    start_urls = [
        # List of universities / websites to scrape
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.total_universities = len(self.start_urls)
        self.scraped_universities = 0

    custom_settings = {
        'DEPTH_LIMIT': 3,  # Set the depth limit of the spider
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
        'FEED_URI': 'output.json',  # Specify the output file
        'FEED_FORMAT': 'json',  # Output format
    }

    def parse(self, response):
        # Find and save all the PDF links on the current page
        for link in response.css('a::attr(href)').getall():
            if link.endswith('.pdf'):
                yield {
                    'pdf_link': response.urljoin(link)
                }

        # Follow all the links on the current page
        for href in response.css('a::attr(href)'):
            yield response.follow(href, self.parse)

        # Increment the scraped universities count
        self.scraped_universities += 1

        # Check if all universities have been scraped
        if self.scraped_universities == self.total_universities:
            raise CloseSpider('All universities scraped')


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(PDFSpider)
    process.start()
    input("Press Enter to exit...")

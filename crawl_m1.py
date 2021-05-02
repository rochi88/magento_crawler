import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class DomainSpider(CrawlSpider):
    name = 'roguefitness'
    allowed_domains = ["www.roguefitness.com"]
    # Start the crawl with a known product detail page so that you can tweak the `yield` queries below before crawling the entire site
    start_urls = ['https://www.roguefitness.com/rogue-barrel-bag']

    # If you only want to crawl a subfolder, then change the `allow=r'/'` string to something like `allow=r'/en'`
    rules = (
        Rule(LinkExtractor(allow=r'/'), callback='parse_item', follow=True),
    )

    # Rename this from `parse_item` to `parse` and comment out the `rules` above to crawl just a single url
    def parse_item(self, response):
        for body in response.css('body'):
            # Don't log non-product urls
            if not body.css('body.catalog-product-view .price-box .price::text').get():
                continue
            yield {
                # TODO: Update CSS selector to match SKU, if the site you're crawling outputs the SKU
                #'sku': body.css('[itemprop="sku"]::text').get(),
                'price': body.css('.price-box .price::text').get().strip(),
                'name': body.css('.product-title::text').get(),
                'url': response.url
            }
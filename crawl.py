#################################
# Magento 2
################################# 
# import scrapy
# from scrapy.linkextractors import LinkExtractor
# from scrapy.spiders import CrawlSpider, Rule

# class DomainSpider(CrawlSpider):
#     name = 'example'
#     allowed_domains = ["dreamfurnishings.co.uk"]
#     # Start the crawl with a known product detail page so that you can tweak the `yield` queries below before crawling the entire site
#     start_urls = ['https://dreamfurnishings.co.uk/luxury-furnitures']

#     # If you only want to crawl a subfolder, then change the `allow=r'/'` string to something like `allow=r'/en'`
#     rules = (
#         Rule(LinkExtractor(allow=r'/'), callback='parse_item', follow=True),
#     )

#     # Rename this from `parse_item` to `parse` and comment out the `rules` above to crawl just a single url
#     def parse_item(self, response):
#         for body in response.css('body'):
#             # Don't log non-product urls
#             if not body.css('[itemprop="sku"]::text').get():
#                 continue
#             yield {
#                 'sku': body.css('[itemprop="sku"]::text').get(),
#                 'price': body.css('[itemprop="price"] .price::text').get(),
#                 'name': body.css('[itemprop="name"]::text').get(),
#                 'url': response.url
#             }

#################################
# Magento 1
#################################    
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class DomainSpider(CrawlSpider):
    name = 'roguefitness'
    # allowed_domains = ["dreamfurnishings.co.uk"]
    # # Start the crawl with a known product detail page so that you can tweak the `yield` queries below before crawling the entire site
    # start_urls = ['https://dreamfurnishings.co.uk/luxury-furnitures']

    allowed_domains = ["www.example.com"]
    # Start the crawl with a known product detail page so that you can tweak the `yield` queries below before crawling the entire site
    start_urls = ['https://www.example.com/example-product']

    # If you only want to crawl a subfolder, then change the `allow=r'/'` string to something like `allow=r'/en'`
    rules = (
        Rule(LinkExtractor(allow=r'/'), callback='parse_item', follow=True),
    )

    # Rename this from `parse_item` to `parse` and comment out the `rules` above to crawl just a single url
    def parse_item(self, response):
        for body in response.css('body'):
            images = []
            # Don't log non-product urls
            if not body.css('body.catalog-product-view .price-box .price::text').get():
                continue
            for image in body.css('img::attr(src)').extract():
                images.append(image)
            yield {
                # TODO: Update CSS selector to match SKU, if the site you're crawling outputs the SKU
                # 'sku': body.css('[itemprop="sku"]::text').get(),
                'sku': body.css('.sku::text').extract(),
                # 'price': body.css('.price-box .price::text').get().strip().replace(",","").replace("??",""),
                'specialprice': body.css('.price-box .special-price .price::text').get().strip().replace(",","").replace("??",""),
                'price': body.css('.price-box .old-price .price::text').get().strip().replace(",","").replace("??",""),
                'name': body.css('.product .base::text').get(),
                # 'description': body.css('[itemprop="description"] .value::text').get(),
                # 'images': body.css('.product .fotorama__stage__frame div::attr(href)').get(),
                # 'images': body.css('.fotorama__img img::attr(src)').get(),
                'url': response.url,
                'image url': images,

            }
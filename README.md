# magento_crawler

This basic script crawls a Magento 1 or Magento 2 website and logs the prices, SKUs, and product urls to a CSV file. This script was put togther for a company that had consent from the website(s) being scraped. Please use responsibility.

This script uses https://scrapy.org/

This script was tested on macOS Mojave, but it should run on any *NIX system.

You can tweak the `body.css` code to match the specific CSS selectors on the site you're crawling. See [this documentation](https://docs.scrapy.org/en/latest/topics/selectors.html). When you're testing this script, refer to the command above the `def parse_item` line to learn how to run the code for only a single product.

# Todo

* Add support for grouped/configurable products

# Usage

1. Ensure `pip` is installed on your system.
2. Run this command:
   
       pip install scrapy
3. Create a `crawl.py` file with the contents from the file in this Gist that matches your version of Magento.
4. Run this command:
   
       scrapy runspider crawl.py --output=crawled_urls.csv
       cat crawled_urls.csv

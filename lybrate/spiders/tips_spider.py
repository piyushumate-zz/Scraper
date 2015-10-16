import scrapy
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor

class TipsSpider(scrapy.Spider):
    name = "tips"
    base_domain = 'https://www.lybrate.com/'
    allowed_domains = ["www.lybrate.com"]
    start_urls = [
       "https://www.lybrate.com/tips/improving-eye-health"
    ]
    lybrate_tip = "//div[contains(@class, 'name_block_small_img tip') and contains(@class, 'tip')]"
    rules = (
        # Extract links for next pages
        Rule(LxmlLinkExtractor(allow=(), restrict_xpaths=('//div[contains(@class, "pagination")]//a[contains(., "Next")]')), callback='parse_listings', follow=True),
    )


    def parse(self, response):
        return self.parse_listings(response)


    def parse_listings(self, response):
        tips = response.selector.xpath(lybrate_tip)
        for tip in tips:
            print "yo"
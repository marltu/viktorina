from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
import re

from viktorina.items import ViktorinaItem


class ViktorinaSpider(CrawlSpider):
    name = "irclogs.manoerve.com"
    allowed_domains = ["irclogs.manoerdve.com"]
    start_urls = [
        "http://irclogs.manoerdve.com/log/2007-07-01/mokslas/",
    ]

    rules = (
        Rule(SgmlLinkExtractor(allow = ("/mokslas/$",)), callback='parse_item'),
    )

    def parse_item(self, response):
        body = response.body
        lines = re.findall("&lt;Viktorina&gt; ([^<]*)<br>", body)
#        self.log("Found: %s" % lines)

        question = None
        items = []

        for line in lines:
            match = re.match("^\x0300,14 \x02[0-9]+\.\x02\x0300,02 (.*) $", line)
            if match is not None:
                question = match.group(1)
            match = re.match(".*atsakymas( buvo)?: \x0304\x1f([^\x1f]+)\x1f\x0314", line)
            if match is not None:
                answer = match.group(2)
                if (question is not None and answer is not None):
                    items.append(ViktorinaItem(question = question, answer = answer))

        return items


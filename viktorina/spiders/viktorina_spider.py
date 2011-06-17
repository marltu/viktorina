from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
import re

from viktorina.items import ViktorinaItem


class ViktorinaSpider(CrawlSpider):
    name = "viktorina"
    allowed_domains = ["irclogs.manoerdve.com"]
    start_urls = [
        "http://irclogs.manoerdve.com/log/2009-01-17/mokslas/",
    ]

    rules = (
        # go through all links containing ending with mokslas/
        Rule(SgmlLinkExtractor(allow = ("mokslas/$",)), callback='parse_item', follow = True),
    )

    def parse_item(self, response):
        body = response.body

        # find all messages by <Viktorina>
        lines = re.findall("&lt;Viktorina&gt; ([^<]*)<br>", body)

        question = None
        items = []

        for line in lines:
            # check for question
            match = re.match("^\x0300,14 \x02[0-9]+\.\x02\x0300,02 (.*) $", line)
            if match is not None:
                question = match.group(1)
            # check for confirmed answer
            match = re.match(".*atsakymas( buvo)?: \x0304\x1f([^\x1f]+)\x1f\x0314", line)
            if match is not None:
                answer = match.group(2)
                # question and answer found, add it to items
                if (question is not None and answer is not None):
                    items.append(ViktorinaItem(question = question, answer = answer))

        return items


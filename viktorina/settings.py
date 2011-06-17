# Scrapy settings for viktorina project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'viktorina'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['viktorina.spiders']
NEWSPIDER_MODULE = 'viktorina.spiders'
DEFAULT_ITEM_CLASS = 'viktorina.items.ViktorinaItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

#DOWNLOAD_DELAY = 0.25
LOG_LEVEL = 'INFO'

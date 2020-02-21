import requests
import scrapy
import unittest

url = 'http://172.18.58.238/snow/'
r = requests.get(url)
print("\t *", r.status_code)

h = requests.get(url)
for x in h.headers:
 print("\t", x, ":", h.headers[x])


headers = {
    'User-Agent' : 'Iphone'
}
URLheader = ('http://172.18.58.238/headers.php')
rh = requests.get(URLheader, headers=headers)
print(rh.text)

class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ['http://172.18.58.238/snow/']
    def parse(selfself, response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'
            yield {
                'Image Link' : x.xpath(newsel).extract_first(),
            }

class Test_NewSpider(unittest.TestCase):
    def test_spider(selfself):
        NewSpider()

if __name__ == '__main__': unittest.main()

#TESTING
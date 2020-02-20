import scrapy
'''
class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://blog.scrapinghub.com']

    def parse(self, response):
        for title in response.css('.post-header>h2'):
            yield {'title': title.css('a ::text').get()}

        for next_page in response.css('a.next-posts-link'):
            yield response.follow(next_page, self.parse)


class BlogSpider(scrapy.Spider):
    name = 'housespider'
    start_urls = ['https://woodall.house.gov/issues']

    def parse(self, response):
        #self.data['woodall.house.gov'] = []
        for title in response.css('.field-content'):
            titleText = title.css('a ::text').get()
            href = title.css('a ::attr(href)').get()
            if href is not None:
                next_page_link= response.urljoin(href)
                # yield{"next page link": next_page_link}
                yield scrapy.Request(url=next_page_link, callback=self.next)
                #yield {'title': titleText, 'href': href}
'''
class BlogSpider(scrapy.Spider):
    name = 'issue_spider'
    start_urls = ['https://www.cantwell.senate.gov/issues']

    def parse(self, response):
        for translucent in response.css('li'):
            href = translucent.css('a ::attr(href)').get()  
            yield scrapy.Request(url=href, callback=self.next)  
        

    def next(self, response):
        titleText = response.css('h2 ::text').get()  
        contentText = response.css('.summary>p ::text').get()
        yield {'title': titleText, 'content': contentText}

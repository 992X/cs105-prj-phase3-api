import scrapy
import json

'''
class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://blog.scrapinghub.com']

    def parse(self, response):
        for title in response.css('.post-header>h2'):
            yield {'title': title.css('a ::text').get()}

        for next_page in response.css('a.next-posts-link'):
            yield response.follow(next_page, self.parse)
'''
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

    def next(self, response):
        allContent = ''
        title = ''
        for content in response.css('.field-item.even>p'):
            if content.css('p ::text').get() is not None: 
                allContent += content.css('p ::text').get()
        if allContent == '':
            for content in response.css('.field-item.even>p'):
                if content.css('span.text::text').get() is not None: 
                    allContent += content.css('span.text::text').get()
        if allContent == '':
            for content in response.css('.field-item.even>div>div>p'):
                if content.css('p::text').get() is not None: 
                    allContent += content.css('p::text').get()
        if allContent == '':
            print("it is empty")
        title = response.css('h1 ::text').get()
        yield {'title': title, "content": allContent}


            

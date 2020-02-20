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
    name = 'twitterspider'
    start_urls = ['https://twitter.com/i/lists/4244910/members']

    def parse(self, response):
        #for title in response.css('.css-1dbjc4n'):
        href = response.css('a ::attr(href)').getall()
        if href is not None:
            next_page_link= response.urljoin(href)
            yield {'link': next_page_link}
            #yield scrapy.Request(url=next_page_link, callback=self.next)

'''
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
'''

            

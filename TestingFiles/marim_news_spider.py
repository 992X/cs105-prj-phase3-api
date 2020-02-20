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
'''


class IssueSpider(scrapy.Spider):
    name = 'issue_spider'

    def start_requests(self):
        urls = [
            'https://www.cantwell.senate.gov/themes/cantwell/templates/partials/includes/resultset.cfm?view=press_quick_vw&columns=title,date,friendly_url&order_cols=date&order_dirs=DESC&results_per_page=2000&restrict_keys=type&restrict_vals=news_article&restrict_ops='
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # def parse(self, response):
    #     for tr in response.css('tbody'):
            
    #         yield {'title': titleText, 'summary': summary}
    #         filename = 'haha.txt'
    #         with open(filename, 'wb') as f:
    #             f.write(titleText)
    #             f.write(summary)
    #         self.log('Saved file %s' % filename)
        # href = title.css('a ::attr(href)').get()
        # if href is not None:
        #     next_page_link= response.urljoin(href)
        #     # yield{"next page link": next_page_link}
        #     yield scrapy.Request(url=next_page_link, callback=self.next)
        #     yield {'title': titleText, 'href': href}
    # def next(self, response):
    #     allContent = ''
    #     for content in response.css('.field-item.even>p'):
    #         if content.css('p ::text').get() is not None:
    #             allContent += content.css('p ::text').get()
    #     if allContent is '':
    #         for content in response.css('.field-item.even>p'):
    #             if content.css('span ::text').get() is not None:
    #                 allContent += content.css('span ::text').get()
    #     yield {"content": allContent}

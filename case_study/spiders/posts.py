import scrapy


class PostsSpider(scrapy.Spider):
    name = 'posts'
    allowed_domains = ['reddit.com']
    start_urls = ['http://reddit.com/']

    def parse(self, response):
        headers=response.css('h3._eYtD2XCVieq6emjKBH3m::text').extract()
        votes=response.xpath('.//div[@class="_1rZYMD_4xY3gRcSS3p8ODO _3a2ZHWaih05DgAOtvu6cIo "]/text()').extract()
        dates=response.xpath('.//a[@class="_3jOxDPIQ0KaOWpzvSQo-1s"]/text()').extract()
        links=response.css('a._3jOxDPIQ0KaOWpzvSQo-1s::attr(href)').extract()
        
        lst = []
        items=zip(headers, votes, dates, links)
        for i in items:
            dict_posts = {'Headers': i[0],
                          'Votes': i[1],
                          'Dates': i[2],
                          'Links': i[3]}
            lst.append(dict_posts)
            yield dict_posts
        
        print(lst)



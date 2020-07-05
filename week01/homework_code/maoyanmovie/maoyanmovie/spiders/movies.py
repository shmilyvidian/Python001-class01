import scrapy
from bs4 import BeautifulSoup as bs
from maoyanmovie.items import MaoyanmovieItem
from scrapy.selector import Selector

class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def start_requests(self):
        yield scrapy.Request(url='https://maoyan.com/films?showType=3', callback=self.parse,dont_filter=False)

    def parse(self, response):
        movies_list = []
        movie_type = None
        movie_time = None
        maoyan_movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        for movie in maoyan_movies[0:10]:
            m = MaoyanmovieItem()
            movie_name = movie.xpath('./div[1]/span[1]/text()').extract()[0]
            movie_type = movie.xpath('./div[2]/text()').extract()[1].strip()
            movie_time = movie.xpath('./div[4]/text()').extract()[1].strip()
            m['movie_name'] = movie_name
            m['movie_type'] = movie_type
            m['movie_time'] = movie_time
            movies_list.append(m)
        return movies_list

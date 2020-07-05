import scrapy
from bs4 import BeautifulSoup as bs
from maoyanmovie.items import MaoyanmovieItem
from scrapy.selector import Selector

class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def start_requests(self):
        yield scrapy.Request(url='https://maoyan.com/films?showType=3', callback=self.parse)

    def parse(self, response):
        items = []
        movie_type = None
        movie_time = None
        soup = bs(response.text, 'html.parser')
        title_list = soup.find_all('div', attrs={'class': 'movie-hover-info'}, limit=10)
        for tags in title_list:
            m = MaoyanmovieItem()
            move_name = tags.find('span', attrs={'class': 'name'}).text
            m['movie_name'] = move_name
            for i, div in enumerate(tags.find_all('div')):
                if i == 1:
                    movie_type = div.contents[2].strip()
                if i == 3:
                    movie_time = div.contents[2].strip()
            m['movie_type'] = movie_type
            m['movie_time'] = movie_time
            items.append(m)
        return items

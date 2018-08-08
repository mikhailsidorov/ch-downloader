import os

import scrapy
from scrapy.loader import ItemLoader

from ch_downloader import items, settings


class CHSpider(scrapy.Spider):
    name = "ch"

    def __init__(self, url=None, *args, **kwargs):
        super().__init__(url, **kwargs)
        self.start_urls = [url]

    def parse(self, response):
        yield self.load_course(response)

        # file_urls = response.css('.lessons-list__li').xpath(
        #     './/link[@itemprop=$itemprop]', itemprop="contentUrl").css(
        #         '::attr(href)').extract()

        for selector in self.get_lessons_selector(response):
            yield self.load_lesson(selector)

        # filename = os.path.join(settings.FILES_STORE, 'info.txt')
        # with open(filename, 'w') as f:
        #     for url in file_urls:
        #         f.write(url)
        # self.log('Saved file %s' % filename)

    def get_lessons_selector(self, response):
        return response.css('.lessons-list__li')

    def load_course(self, response):
        course_loader = ItemLoader(item=items.Course(), response=response)
        course_loader.add_css('name', 'article header.standard-block h1::text')
        course_loader.add_css('original_name',
                              'article header div.original-name::text')
        course_loader.add_css('description',
                              'article div.standard-block p::text')
        course_loader.add_css(
            'materials', 'article div.standard-block a.downloads::attr(href)')
        duration = response.css(
            'article div.standard-block__duration::text').extract_first().split(' ')[1]
        course_loader.add_value('duration', duration)

        return course_loader.load_item()

    def load_lesson(self, selector):
        lesson_loader = ItemLoader(items.Lesson(), selector)
        name = selector.xpath(
            './/span[@itemprop="name"]/text()').extract_first()
        url = selector.xpath(
            './/link[@itemprop="contentUrl"]/@href').extract_first()
        extention = url.split('.')[-1]
        filename = f'{name}.{extention}'
        lesson_loader.add_value('name', name)
        lesson_loader.add_value('file_urls', url)
        lesson_loader.add_value('filename', filename)
        lesson_loader.add_css('duration', 'em.lessons-list__duration::text')

        return lesson_loader.load_item()

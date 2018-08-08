import os

from scrapy import Request
from scrapy.pipelines.files import FilesPipeline
from scrapy.exceptions import DropItem

from .items import Course, Lesson
from . import settings


class CourseInfoStoringPipeline(object):
    def open_spider(self, spider):
        self.info_file = open(os.path.join(
            settings.FILES_STORE, 'info.txt'), 'w')

    def close_spider(self, spider):
        self.info_file.close()

    def process_item(self, item, spider):
        if isinstance(item, Lesson):
            self.store_lesson_info(item)
        elif isinstance(item, Course):
            self.store_course_info(item)
            raise DropItem
        return item

    def store_course_info(self, course):
        course_info = f'''Name: {course['name']}
        Original name: {course['original_name']}
        Duration: {course['duration']}
        Description: {course['description']}

        Lesson list:
        '''
        self.info_file.write(course_info)

    def store_lesson_info(self, lesson):
        lesson_info = f'{lesson["name"]} ({lesson["duration"]})'
        self.info_file.write(lesson_info)


class LessonLinkStoringPipeline(object):
    def open_spider(self, spider):
        self.links_file = open(os.path.join(
            settings.FILES_STORE, 'links.txt'), 'w')

    def close_spider(self, spider):
        self.links_file.close()

    def process_item(self, item, spider):
        if isinstance(item, Lesson):
            self.store_link(item)
            raise DropItem
        else:
            return item

    def store_link(self, lesson):
        self.links_file.write(f'{lesson["file_urls"][0]}\n')


class CleanFileNamesPipeline(object):
    def process_item(self, item, spider):
        if 'filename' in item.keys():
            item['filename'][0] = item['filename'][0].replace('!', '')
        return item


class CustomNamingFilesPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None):
        return request.meta.get('filename', '')

    def get_media_requests(self, item, info):
        filename = item.get('filename', None)
        meta = {'filename': filename[0]} if filename else {}
        return [Request(x, meta=meta) for x in item.get(self.files_urls_field, [])]

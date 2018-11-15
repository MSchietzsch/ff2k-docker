from elasticsearch import Elasticsearch
from elasticsearch_dsl import DocType, Text, Date, Search, Nested, Keyword, Mapping, Integer
from elasticsearch_dsl.connections import connections
from elasticsearch.helpers import bulk
from django.db import models
from . import models
from django.conf import settings

if settings.ENVIRONMENT != "dev":
    connections.create_connection(hosts=['elasticsearch'], timeout=20, sniff_on_start=True)


class StoryIndex(DocType):
    storyID = Text()
    story_title = Text()
    author = Text()
    story_description = Text()
    story_initial_release = Date()
    story_last_modified = Date()

    class Index:
        name = 'profile-index'

class ChapterIndex(DocType):
    id = Text()
    storyID = Text()
    story_title = Text()
    chapter_title = Text()
    chapter_number = Integer()
    chapter_release = Date()

    class Index:
        name = 'profile-index'

if settings.ENVIRONMENT == "dev":

    def bulk_indexing():
        StoryIndex.init(index='ff2k-index')
        ChapterIndex.init(index='ff2k-index')
        es = Elasticsearch()
        bulk(client=es, actions=(b.indexing() for b in models.Story.objects.all().iterator()))
        bulk(client=es, actions=(b.indexing() for b in models.Chapter.objects.all().iterator()))
    
    def search(author):
        s = Search().filter('term', author=author)
        response = s.execute()
        return response

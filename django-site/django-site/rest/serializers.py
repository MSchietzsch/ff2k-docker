from rest_framework import serializers
from ff2ksite.models import Story, Chapter, Fandom, Categories, Tags


class StoriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Story
        fields = ('story_title', 'auto_uid')

class StorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Story
        fields = ('story_title', 'auto_uid', 'story_initial_release', 'story_last_modified', 'story_description')

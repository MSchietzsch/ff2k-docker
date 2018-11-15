from rest_framework import serializers
from ff2ksite.models import Story, Chapter, Fandom, Categories, Tags


class UserSerializer_auth(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)

class StoriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Story
        fields = ('story_title', 'auto_uid')

class StorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Story
        fields = ('story_title', 'auto_uid', 'story_initial_release', 'story_last_modified', 'story_description')

    def get_chapter(self, obj):
        chapter_list = Chapter.objects.filter(story=id).exclude(chapter_flag_hidden=True)
        return serializers.HyperlinkedModelSerializer()

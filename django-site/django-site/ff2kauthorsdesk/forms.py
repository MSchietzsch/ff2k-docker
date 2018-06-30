from django import forms

from ff2ksite.models import Story, Chapter, Fandom

class PostStory(forms.ModelForm):

    class Meta:
        model = Story
        fields = ('story_title', 'story_description', 'fandom', 'story_cat', 'story_tags', 'story_is_save',)
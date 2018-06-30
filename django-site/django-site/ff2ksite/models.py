import datetime
import uuid
from django.db import models, IntegrityError
from django.db.models import Value
from django.db.models.signals import post_save
from django.db.models.functions import Concat
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.utils import timezone
from django.dispatch import receiver
from django.conf import settings


class Profile(models.Model):
    username = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='user')
    bio = models.TextField()
    birth_date = models.DateField(null=True, blank=True)
    country = CountryField()


class Categories(models.Model):
    cat_name = models.CharField(
        max_length=32, unique=True, blank=False, db_index=True)
    cat_descr = models.TextField(max_length=300, blank=True)

    def __str__(self):
        return self.cat_name


class Fandom(models.Model):
    fandom_name = models.CharField(
        max_length=32, unique=True, blank=False, db_index=True)
    fandom_descr = models.TextField(max_length=1200, blank=True)
    fandom_short = models.CharField(max_length=8, unique=True, blank=False)

    def __str__(self):
        return self.fandom_name


class Tags(models.Model):
    tag_name = models.CharField(max_length=32, blank=False, db_index=True)
    tag_descr = models.TextField(max_length=1200, blank=True)

    def __str__(self):
        return self.tag_name


class Character(models.Model):
    # char_name = models.CharField(max_length=16, unique=True, blank=False, db_index=True)
    # if char_name is changed the Pairings will we be changed and therfore messed up, reference from pairings to char will be name not ID
    char_firstname = models.CharField(max_length=32, blank=True)
    char_surname = models.CharField(max_length=32, blank=True)
    char_name = models.CharField(
        max_length=100, default='blank', editable=False)

    def save(self):
        new_id = self.id

        self.char_name = "{firstname} {surname}".format(
            firstname=self.char_firstname, surname=self.char_surname)
        super(Character, self).save()

    char_descr = models.CharField(max_length=128, blank=True)
    fandom = models.ForeignKey(Fandom, on_delete=models.CASCADE)

    def __str__(self):
        return self.char_name


class Story(models.Model):
    story_title = models.CharField(max_length=256, blank=False)
    story_description = models.TextField()
    story_initial_release = models.DateTimeField(auto_now_add=True, blank=True)
    story_last_modified = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.story_title

    def was_updated_recently(self):
        return self.story_last_modified >= timezone.now() - datetime.timedelta(days=14)
    auto_uid = models.CharField(
        max_length=8, blank=True, editable=False, unique=True, db_index=True)
    # add index=True if you plan to look objects up by it
    # blank=True is so you can validate objects before saving - the save method will ensure that it gets a value

    def save(self, *args, **kwargs):
        if not self.auto_uid:
            self.auto_uid = uuid.uuid4().hex[:8]
            # using your function as above or anything else
        success = False
        failures = 0
        while not success:
            try:
                super(Story, self).save(*args, **kwargs)
            except IntegrityError:
                failures += 1
                if failures > 5:  # or some other arbitrary cutoff point at which things are clearly wrong
                    raise
                else:
                    # looks like a collision, try another random value
                    self.auto_uid = uuid.uuid4().hex[:8]
            else:
                success = True
    fandom = models.ForeignKey(Fandom, on_delete=models.CASCADE)
    story_cat = models.ManyToManyField(Categories)
    story_tags = models.ManyToManyField(Tags)
    story_is_save = models.BooleanField(default=False)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)

    if settings.ENVIRONMENT != "dev":
        def indexing(self):
            from .search import StoryIndex
            obj = StoryIndex(
                meta={'id': self.auto_uid},
                storyID=self.auto_uid,
                story_title=self.story_title,
                author=self.author.username,
                story_description=self.story_description,
                story_initial_release=self.story_initial_release,
                story_last_modified=self.story_last_modified,
            )
            obj.save()
            return obj.to_dict(include_meta=True)


class Chapter(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    chapter_number = models.PositiveSmallIntegerField(unique=False)
    chapter_title = models.CharField(max_length=64, blank=False)
    chapter_text = models.TextField()
    chapter_flag_hidden = models.BooleanField(default=False)
    chapter_release = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.chapter_title

    if settings.ENVIRONMENT != "dev":

        def indexing(self):
            from .search import ChapterIndex
            obj = ChapterIndex(
                meta={'id': self.id},
                storyID=self.story.auto_uid,
                story_title=self.story.story_title,
                chapter_title=self.chapter_title,
                chapter_number=self.chapter_number,
                chapter_release=self.chapter_release,
            )
            obj.save()
            return obj.to_dict(include_meta=True)

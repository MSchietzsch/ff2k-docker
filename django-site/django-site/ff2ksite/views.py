from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.template import loader
from django.views.decorators.cache import cache_page
from django.contrib.auth.models import User 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from .models import Story, Chapter, Tags, Fandom, Profile

@cache_page(60 * 15)
def index(request):
    latest_story_list = Story.objects.order_by('-story_last_modified')[:5]
    latest_story_list_save = Story.objects.order_by(
        '-story_last_modified').filter(story_is_save=True)[:5]
    template = loader.get_template('ff2ksite/index.html')
    context = {'latest_story_list': latest_story_list,
               'latest_story_list_save': latest_story_list_save}
    return render(request, 'ff2ksite/index.html', context)


@cache_page(60 * 0)
def profile(request):
    users = User.objects.all().select_related('profile')
    template = loader.get_template('ff2ksite/profile.html')
    context = {'users': users}
    return render(request, 'ff2ksite/profile.html', context)


@cache_page(60 * 60)
def profile_other(request, username):
    username = User.objects.get(username=username)
    prof = Profile.objects.get(username=username)
    story_list = Story.objects.filter(
        author=username).order_by('-story_initial_release')
    template = loader.get_template('ff2ksite/profile_other.html')
    context = {'username': username, 'prof': prof, 'story_list': story_list}
    return render(request, 'ff2ksite/profile_other.html', context)  


@cache_page(60 * 60)
def detail(request, auto_uid):
    qs = Story.objects.get(auto_uid=auto_uid)
    chapter_list = Chapter.objects.filter(
        story=qs).exclude(chapter_flag_hidden=True)
    template = loader.get_template('ff2ksite/story.html')
    context = {'chapter_list': chapter_list, 'story': qs}
    return render(request, 'ff2ksite/story.html', context)


#@cache_page(60 * 60)
def chapter_view(request, auto_uid, chapter_number):
    qs = Story.objects.get(auto_uid=auto_uid)
    qc = Chapter.objects.filter(story=qs)
    chapter_list = qc.exclude(chapter_flag_hidden=True).order_by('chapter_number')
    chapter = qc.get(chapter_number=chapter_number)

    paginator = Paginator(chapter_list, 12) # Show 12 chapters per page
    page = request.GET.get('page')
    chapters = paginator.get_page(page)

    context = {'chapter': chapter, 'chapter_list': chapter_list, 'story': qs, 'chapters': chapters }    
    return render(request, 'ff2ksite/chapter.html', context)


@cache_page(60 * 60)
def fandom(request, fandom_short):
    qf = Fandom.objects.get(fandom_short=fandom_short)
    story_list = Story.objects.order_by(
        '-story_last_modified').filter(fandom_id=qf)
    story_list_save = story_list.filter(story_is_save=True)
    context = {'story_list': story_list,
               'story_list_save': story_list_save, 'fandom': qf}
    return render(request, 'ff2ksite/fandom.html', context)


def search(request):
    return render(request, 'ff2ksite/search.html')

@cache_page(60 * 60)
def about(request):
    return render(request, 'ff2ksite/about.html')


@cache_page(60 * 60)
def privacy(request):
    return render(request, 'ff2ksite/privacy_policy.html')

@cache_page(60 * 60)
def disclaimer(request):
    return render(request, 'ff2ksite/disclaimer.html')

@cache_page(60 * 60)
def tags(request):
    all_tags = Tags.objects.all()
    context = {'tags': all_tags}
    return render(request, 'ff2ksite/tags.html', context)


def redir_home(request):
    return redirect('/')

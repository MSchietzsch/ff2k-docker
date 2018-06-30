from django.shortcuts import render
from .forms import PostStory
from ff2ksite.models import Story, Chapter
from django.contrib.auth.models import User


def ad(request):
    current_user = request.user
    story_list = Story.objects.filter(author=current_user.id).order_by('-story_initial_release')
    context = {'story_list': story_list}
    return render(request, 'ff2kauthorsdesk/ad.html', context)

def ad_story_detail(request, auto_uid):
    qs = Story.objects.get(auto_uid=auto_uid)
    chapter_list = Chapter.objects.filter(story=qs)
    context = {'chapter_list': chapter_list, 'story': qs}
    return render(request, 'ff2kauthorsdesk/ad_story_detail.html', context) 


def story_new(request):
    if request.method == "POST":
        form = PostStory(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostStory()
    return render(request, 'ff2kauthorsdesk/ad_chapter_create.html', {'form': form})

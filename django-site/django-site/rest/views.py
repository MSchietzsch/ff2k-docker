from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from ff2ksite.models import Story, Chapter, Fandom
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest.serializers import StoriesSerializer, StorySerializer, UserSerializer, UserSerializer_auth, FandomSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from django.http import HttpResponseForbidden

@permission_classes((permissions.AllowAny,))
class rest_story_list(APIView):
    def get(self, request, format=None):
        if request.user.is_authenticated == True:
            stories = Story.objects.all()
        else:
            stories = Story.objects.filter(story_is_save=True) 
        serializer = StoriesSerializer(stories, many=True)
        return Response(serializer.data)

@permission_classes((permissions.AllowAny,))
class rest_story_detailas_view(APIView):
    def get_object(self, auto_uid):
        try:
            return  Story.objects.get(auto_uid=auto_uid)
        except Story.DoesNotExist:
            raise Http404
    def get(self, request, auto_uid, format=None):
        story = Story.objects.get(auto_uid=auto_uid)
        if story.story_is_save == True:
            serializer = StorySerializer(story)
            return Response(serializer.data)
        else:
            return HttpResponseForbidden()

@permission_classes((permissions.AllowAny,))
class rest_user_list(APIView):
    def get(self, request, format=None):
        authors = User.objects.all()
        if request.user.is_authenticated == True:
            serializer = UserSerializer_auth(authors, many=True)
        else:
            serializer = UserSerializer(authors, many=True)
        return Response(serializer.data)

@permission_classes((permissions.AllowAny,))
class rest_fandoms_list(APIView):
    def get(self, request, format=None):
        fandoms = Fandom.objects.all()
        serializer = FandomSerializer(fandoms, many=True)
        return Response(serializer.data)

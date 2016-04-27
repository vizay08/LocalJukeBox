from django.shortcuts import render
from django.http import HttpResponse
from Music.models import Song
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def playingSong(request):
    song  = Song.objects.all().filter(is_playing=True)
    if song:
        song = song[0]

    #song = None
    if song:
        htmlCode  = song.title

    else:
        htmlCode = "No Song is playing"


    return HttpResponse(htmlCode)

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from Music.models import Song
import json
#import Music

@csrf_exempt
def playListView(request):
    #retrieving top 10 items
    playlist  = Song.objects.order_by('-counter').filter(is_playing=False)[:10]  #playlist = Music.models.Song._meta.db_table

    #playlist = None
    htmlcode = ""
    if playlist:
        htmlcode = [[song.title,song.token] for song in playlist]
    else:
        htmlcode = []

    return HttpResponse(json.dumps(htmlcode))


@csrf_exempt
def vote(request):
    token = request.POST.get('token','adha')
    opt = ""
    try:
        s = Song.objects.get(token=token)
        s.counter += 1
        s.save()
        opt = "success"
    except Song.DoesNotExist:
        opt = "fail:token not found"
    except:
        opt = "fail: some exception"

    return HttpResponse(opt)
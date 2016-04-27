import settings
import tokengenerator
from django.db.models import Max
from Music.models import Song
from os import walk
import pygame
import thread
import re

MUSIC_URI = settings.MUSIC_URI

#parse the Music Library and get the list
def parseMusicLibrary(path):
    opt = []
    for (dirpath,dirnames,filenames) in walk(path):
        L = []
        #print dirpath,dirnames,filenames
        for i in filenames:
            if re.search('\.mp3$',i):
                L.append(i)
        if len(L) != 0:
            m = {}
            m['dirpath'] = dirpath
            m['songslist'] = L
            opt.append(m)

    return opt

#load the music into db
def loadMusicIntoDb():
    print "loading music"
    if(len(Song.objects.all()) == 0):
        L = parseMusicLibrary(MUSIC_URI)
        print L
        for songs in L:
            for song in songs['songslist']:
                token = ""
                while True:
                    try:
                        token = tokengenerator.generate_token(6)
                        c = Song.objects.get(token=token)
                    except Song.DoesNotExist:
                        c = Song(title=song,song_directory=songs['dirpath'],token = token)
                        c.save()
                        break



def playSong(dirpath,title):
    pygame.init()
    pygame.mixer.init()
    clock = pygame.time.Clock()
    pygame.mixer.music.load(dirpath+'/'+title)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        clock.tick(1000)
    pygame.mixer.music.stop()

#Play the Music
def startMusic():
    #check if db is empty , if it is fill it
    loadMusicIntoDb()
    while True:
        print "threadd is running"
        c = Song.objects.all().aggregate(Max('counter'))

        if (len(c) == 0):
            continue
        c = Song.objects.filter(counter=c['counter__max'])[0]

        c.is_playing = True
        c.save()
        playSong(c.song_directory,c.title)
        Song.objects.filter(is_playing=True).delete()


def startMusicThread():
    thread.start_new_thread(startMusic,tuple())



if __name__ == '__main__':
    playSong("/home/vijay/Music/","02 - Cold Vs. Hot.mp3")

"""LocalJukeBox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from PlayingSong import urls
import PlayList
from Dashboard import views
import MusicLoader

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^playingsong/',include('PlayingSong.urls') ),
    url(r'^playlist/',include('PlayList.urls') ),
     url(r'^vote/',PlayList.views.vote,name='vote'),
    url(r'^$',views.presentDashboard,name='dashboardview'),]

MusicLoader.startMusicThread()
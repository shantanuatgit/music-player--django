"""musicplayer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from boom import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('', views.home_view, name='home'),
    path('searchresult',views.searchresults_view,name='searchresult'),
    path('allplaylists/',views.allplaylists_view,name='allplaylists'),
    path('allplaylists/<int:pk>',views.deleteplaylists_view,name='allplaylists'),
    path('playlistsongs/',views.playlistsongs_view,name='playlistsongs'),
    path('createplaylist/',views.createplaylist_view,name='createplaylist'),
    path('createplaylist/<int:pk>',views.addsongs_view,name='addsongs'),
    path('backtoplaylist',views.backtoplaylist_view,name='backtoplaylist'),
    path('<int:pk>',views.addtofavourites_view,name='favourites'),
    path('favourites/',views.favourites_view,name='favourites'),
    path('favourites/<int:pk>',views.deletefavourite_view,name='favourites'),
    path('<int:pk> <int:year>',views.playsong_view,name='playsong'),
    path('favourites/<int:pk> <str:singer>',views.playfavsong_view,name='playfavsong'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

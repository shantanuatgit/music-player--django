from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# Create your views here.


def home_view(request):
    songs=Song.objects
    if not request.user.is_anonymous:
        recent=list(Recent.objects.filter(user=request.user))
        recents=Recent.objects.filter(user=request.user).order_by("-id")
        if (len(recents)>6):
            R=recent[0]
            R.delete()
            recent.pop(0)
            recents=Recent.objects.filter(user=request.user)
            return render(request,'home.html',{'songs':songs, 'recents':recents})
        return render(request,'home.html',{'songs':songs, 'recents':recents})
    else:
        return render(request,'home.html',{'songs':songs})


@login_required(login_url="/accounts/signup")
def allplaylists_view(request):
    playlists=Playlist.objects.filter(user=request.user)
    return render(request,'allplaylists.html',{'playlists':playlists})

@login_required(login_url="/accounts/signup")
def playlistsongs_view(request):
    playlistName=request.GET.get('name')
    playlistName=playlistName.split(',')
    playlists=Playlist.objects.filter(id=playlistName[1])
    currentuser=request.user
    return render(request,'playlistsongs.html',{'playlists':playlists, 'playlistName':playlistName[0],'playlist_id':playlistName[1],'currentuser':currentuser})

@login_required(login_url="/accounts/signup")
def createplaylist_view(request):
    songs=Song.objects
    playlists=Playlist.objects.all()
    if request.method == 'POST':
        playlist=Playlist()
        playlist.list_name=request.POST['playlistname']
        playlist.user=request.user
        global name
        name=playlist.list_name
        playlist.save()
        global ID
        ID=playlist.id
        return render(request,'addsongs.html',{'songs':songs, 'name':name})
    else:
        return render(request,'createplaylist.html',{'songs':songs})

@login_required(login_url="/accounts/signup")
def addsongs_view(request,pk):
    songs=Song.objects.all()
    if request.method == 'GET':
        global q
        q=request.GET['query']
        obj_list=Song.objects.filter(Q(movie__icontains=q) | Q(song_name__icontains=q) | Q(artist__icontains=q))
        return render(request,'addsongs.html',{'songs':songs,'name':name, 'obj_list':obj_list})

    if request.method == 'POST':
        item=Song.objects.get(id=pk)
        playlist=Playlist.objects.filter(id=ID)
        for fields in playlist.all():
            fields.song.add(item)
        obj_list=Song.objects.filter(Q(movie__icontains=q) | Q(song_name__icontains=q) | Q(artist__icontains=q))
        return render(request,'addsongs.html',{'songs':songs,'name':name,'obj_list':obj_list})
    return render(request,'addsongs.html',{'songs':songs,'name':name})

@login_required(login_url="/accounts/signup")
def backtoplaylist_view(request):
    playlists=Playlist.objects.filter(id=ID)
    return render(request,'backtoplaylist.html',{'playlists':playlists, 'name':name})

@login_required(login_url="/accounts/signup")
def deleteplaylists_view(request,pk):
    playlist=Playlist.objects.filter(user=request.user,id=pk)
    playlist.delete()
    return redirect('allplaylists')

@login_required(login_url="/accounts/signup")
def addtofavourites_view(request,pk):
    item=Song.objects.get(id=pk)
    favs=Favourite.objects.all()
    if favs.filter(song=item):
        return redirect('/')
    if request.method == 'POST':
        fav=Favourite()
        fav.user=request.user
        fav.song=item
        fav.save()
        return redirect('/')

@login_required(login_url="/accounts/signup")
def favourites_view(request):
    favs=Favourite.objects.filter(user=request.user)
    return render(request,'favourites.html',{'favs':favs})

@login_required(login_url="/accounts/signup")
def deletefavourite_view(request,pk):
    fav=Favourite.objects.filter(user=request.user,id=pk)
    fav.delete()
    return redirect('favourites')

@login_required(login_url="/accounts/signup")
def playsong_view(request,pk,year):
    track=Song.objects.get(id=pk)
    songs=Song.objects
    recents=Recent.objects.filter(user=request.user).order_by("-id")
    r=Recent.objects.all()
    if r.filter(song=track, user=request.user):
        remove=r.filter(song=track, user=request.user)
        remove.delete()
    if not r.filter(song=track, user=request.user):
        recent=Recent()
        recent.user=request.user
        recent.song=track
        recent.save()
    if request.method == 'GET':
        track=Song.objects.get(id=pk)
        print(track.movie)
        return render(request,'home.html',{'track':track,'songs':songs, 'recents':recents})

@login_required(login_url="/accounts/signup")
def playfavsong_view(request,pk,singer):
    favs=Favourite.objects.filter(user=request.user)
    track=Song.objects.get(id=pk)
    r=Recent.objects.all()
    if r.filter(song=track, user=request.user):
        remove=r.filter(song=track, user=request.user)
        remove.delete()
    if not r.filter(song=track, user=request.user):
        recent=Recent()
        recent.user=request.user
        recent.song=track
        recent.save()
    if request.method == 'GET':
        track=Song.objects.get(id=pk)
        print(track.movie)
        return render(request,'favourites.html',{'track':track,'favs':favs})


@login_required(login_url="/accounts/signup")
def searchresults_view(request):
    q=request.GET['query']
    obj_list=Song.objects.filter(Q(movie__icontains=q) | Q(song_name__icontains=q) | Q(artist__icontains=q))
    return render(request,'searchresult.html',{'obj_list':obj_list})

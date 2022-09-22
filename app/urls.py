from django.urls import path
from . import views
from .views import MusicListDeleteView,BookListDeleteView,TheirListView,TheirDetailView,ListCreateView,ListDeleteView,TheirListMusicView,TheirListBookView,TheirDetailBookView,TheirDetailMusicView,ListCreateBookView,ListCreateMusicView

app_name = "app"

urlpatterns = [
    path('chat_room/',views.Chat.as_view(),name='chat'),
    path('about-us/',views.AboutUs.as_view(),name='about_us'),
    path('feedback/',views.Feedback.as_view(),name='feedback'),
    path('guidelines/',views.Guidelines.as_view(),name='guidelines'),
    path('', views.HomeView.as_view(),name='home'),
    path('list/',TheirListView.as_view(),name = 'list'),
    path('booklist/',TheirListBookView.as_view(),name = 'booklist'),
    path('musiclist/',TheirListMusicView.as_view(),name = 'musiclist'),
    path('list/<slug:slug>/', TheirDetailView.as_view(),name='list_detail'),
    path('booklist/<slug:slug>/', TheirDetailBookView.as_view(),name='booklist_detail'),
    path('musiclist/<slug:slug>/', TheirDetailMusicView.as_view(),name='musiclist_detail'),
    path('create_book_list/',ListCreateBookView.as_view(),name="book_create_list"),
    path('create_music_list/',ListCreateMusicView.as_view(),name="music_create_list"),
    path('create_list/',ListCreateView.as_view(),name="create_list"),
    path('delete_list/<slug:slug>',ListDeleteView.as_view(),name="delete_movie"),
    path('delete_musiclist/<slug:slug>',MusicListDeleteView.as_view(),name="delete_music"),
    path('delete_booklist/<slug:slug>',BookListDeleteView.as_view(),name="delete_book"),
    path('search/',views.search, name='search'),
    path('film/',views.film, name='film'),
    path('film/<str:query>',views.film, name='film'),
    path('all',views.all, name='all'),

]
from django.urls import path
from . import views
from .views import TheirListView,TheirDetailView,ListCreateView,ListDeleteView,TheirListMusicView,TheirListBookView,TheirDetailBookView,TheirDetailMusicView,ListCreateBookView,ListCreateMusicView

app_name = "app"

urlpatterns = [
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
    path('delete_list/<int:pk>',ListDeleteView.as_view()),
    path('search/',views.search, name='search'),
    path('film/',views.film, name='film'),
    path('film/<str:query>',views.film, name='film'),
    path('all',views.all, name='all'),

]
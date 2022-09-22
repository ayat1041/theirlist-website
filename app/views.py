from app.models import List,MusicList,BookList
from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy,reverse
from django.views.generic import TemplateView,ListView,DetailView,CreateView,DeleteView
from django.core.paginator import Paginator
from datetime import timedelta
from django.utils import timezone
# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'

class AboutUs(TemplateView):
    template_name = 'app/about_us.html'

class Chat(TemplateView):
    template_name = 'app/chat_room.html'

class Feedback(TemplateView):
    template_name = 'app/feedback.html'

class Guidelines(TemplateView):
    template_name = 'app/guidelines.html'

class TheirListBookView(ListView): #books
    model = BookList
    template_name ='app/Booklist_list.html'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.order_by("-id")
        return qs

class TheirListMusicView(ListView): #music
    model = MusicList
    template_name ='app/Musiclist_list.html'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.order_by("-id")
        return qs

class TheirListView(ListView): #movies
    model = List
    paginate_by = 8
    template_name ='app/List_list.html'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.order_by("-id")
        # qs = qs.filter(author__name="Ayat")
        # qs = qs.filter(genre__name="Drama")
        return qs

class TheirDetailBookView(DetailView): #books
    model = BookList

class TheirDetailMusicView(DetailView): #music
    model = MusicList

class TheirDetailView(DetailView):
    model = List


class ListCreateBookView(CreateView): #book
    model = BookList
    # fields = "__all__"
    fields = ['title','author','genre','content']
    success_url = reverse_lazy("app:booklist") 
class ListCreateMusicView(CreateView): #music
    model = MusicList
    # fields = "__all__"
    fields = ['title','author','genre','content']
    success_url = reverse_lazy("app:musiclist") 

class ListCreateView(CreateView):
    model = List
    # fields = "__all__"
    fields = ['title','author','genre','content']
    # success_url = "/home/list/"
    # def get_success_url(self):
    #     return reverse('app:list')
    success_url = reverse_lazy("app:list") 

class ListDeleteView(DeleteView):
    model = List
    success_url ="/home/all"
    template_name = "app/list_confirm_delete.html"
class MusicListDeleteView(DeleteView):
    model = MusicList
    success_url ="/home/all"
    template_name = "app/musiclist_confirm_delete.html"
class BookListDeleteView(DeleteView):
    model = BookList
    success_url ="/home/all"
    template_name = "app/booklist_confirm_delete.html"


def search(request):
    query = request.GET['query']
    allPoststit = List.objects.filter(title__icontains=query)
    allPostscont = List.objects.filter(content__icontains=query)
    allPosts = allPoststit.union(allPostscont)
    
    # allPosts = List.objects.filter(title__search=query)
    params = {'allPosts' : allPosts, 'query':query}
    return render(request, 'app/search.html', params)
    #return HttpResponse('this is search')



def film(request,query=None):
    if not query:
        qs = List.objects.all()
    else:
        qs = List.objects.filter(genre__name__icontains=query)
    return render(request, 'app/film.html', {'query': qs, 'result' : query} )

# def choose_list_type(request):
#     return render(request, 'app/choose_list_type.html')
# # def action(request):
# #     #query = Movie.objects.get(id=id)
# #     query = 'Action'
# #     allPosts = List.objects.filter(genre__name__icontains=query)
# #     # allPosts = List.objects.filter(title__search=query)
# #     params = {'allPosts' : allPosts, 'query':query}
# #     return render(request, 'app/action.html', params)


def all(request):
    # movie = List.objects.all()
    # music = MusicList.objects.all()
    # book = BookList.objects.all()
    
    movie = List.objects.filter(posted__gte=timezone.now() - timedelta(days=30)).all().order_by("-id")
    music = MusicList.objects.filter(posted__gte=timezone.now() - timedelta(days=30)).all().order_by("-id")
    book = BookList.objects.filter(posted__gte=timezone.now() - timedelta(days=30)).all().order_by("-id")
    

    # a = movie.union(music)
    # allPosts = a.union(book)
    allPosts = list(movie)
    allPostsmusic = list(music)
    allPostsbook = list(book)
    # p = Paginator(allPosts, 2)
    
    # allPosts = List.objects.filter(title__search=query)
    params = {'allPosts' : allPosts, 'allPostsmusic' : allPostsmusic, 'allPostsbook' : allPostsbook}
    return render(request, 'app/all.html', params)


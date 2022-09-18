from django.contrib import admin
from app.models import Comment,Genre,Author,List,MusicGenre,MusicList,BookGenre,BookList
# Register your models here.



admin.site.register(MusicGenre)
admin.site.register(MusicList)
admin.site.register(BookGenre)
admin.site.register(BookList)
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(List)
admin.site.register(Comment)

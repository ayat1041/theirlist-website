from django.contrib import admin
from app.models import Genre,List,MusicGenre,MusicList,BookGenre,BookList
# Register your models here.



admin.site.register(MusicGenre)
admin.site.register(MusicList)
admin.site.register(BookGenre)
admin.site.register(BookList)
admin.site.register(Genre)
admin.site.register(List)

from email.policy import default
from django.db import models
from ckeditor.fields import RichTextField

#alllist


#music
class MusicList(models.Model):
    title = models.CharField(max_length=65)
    author = models.ForeignKey('Author',on_delete=models.SET_NULL,null=True)
    genre = models.ManyToManyField('MusicGenre')
    posted = models.DateTimeField(auto_now_add=True)
    content = RichTextField(null=True,default=' ')


    def __str__(self):
        return f'{self.title}'

class MusicGenre(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name





#books
class BookList(models.Model):
    title = models.CharField(max_length=65)
    author = models.ForeignKey('Author',on_delete=models.SET_NULL,null=True)
    genre = models.ManyToManyField('BookGenre')
    posted = models.DateTimeField(auto_now_add=True)
    content = RichTextField(null=True,default=' ')


    def __str__(self):
        return f'{self.title}'

class BookGenre(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


#movie
class List(models.Model):
    title = models.CharField(max_length=65)
    author = models.ForeignKey('Author',on_delete=models.SET_NULL,null=True)
    genre = models.ManyToManyField('Genre')
    posted = models.DateTimeField(auto_now_add=True)
    content = RichTextField(null=True,default=' ')


    def __str__(self):
        return f'{self.title}'

class Genre(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

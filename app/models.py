from email.policy import default
from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse_lazy,reverse
from django.utils.text import slugify
from django.conf import settings
from django.contrib.auth.models import User
#alllist


#music
class MusicList(models.Model):
    title = models.CharField(max_length=65)
    #author = models.ForeignKey('Author',on_delete=models.SET_NULL,null=True)
    genre = models.ManyToManyField('MusicGenre')
    creator = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True, null=True)
    posted = models.DateTimeField(auto_now_add=True)
    content = RichTextField(null=True,default=' ')
    type = models.CharField(max_length=10,default="Music")
    slug = models.SlugField(max_length= 300,null=True, blank = True, unique=True)


    def __str__(self):
        return f'{self.title}'
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title + str(self.posted))
        super(MusicList,self).save(*args, **kwargs)



class MusicGenre(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


#books
class BookList(models.Model):
    title = models.CharField(max_length=65)
    #author = models.ForeignKey('Author',on_delete=models.SET_NULL,null=True)
    creator = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True, null=True)
    genre = models.ManyToManyField('BookGenre')
    posted = models.DateTimeField(auto_now_add=True)
    content = RichTextField(null=True,default=' ')
    type = models.CharField(max_length=10,default="book")
    slug = models.SlugField(max_length= 300,null=True, blank = True, unique=True)


    def __str__(self):
        return f'{self.title}'
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title + str(self.posted))
        super(BookList,self).save(*args, **kwargs)

class BookGenre(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


#movie
class List(models.Model):
    title = models.CharField(max_length=65)
    #author = models.ForeignKey('Author',on_delete=models.SET_NULL,null=True)
    genre = models.ManyToManyField('Genre')
    creator = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True, null=True)
    posted = models.DateTimeField(auto_now_add=True)
    content = RichTextField(null=True,default=' ')
    type = models.CharField(max_length=10,default="Movie")
    slug = models.SlugField(max_length= 300,null=True, blank = True, unique=True)


    def __str__(self):
        return f'{self.title}'
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title + str(self.posted))
        super(List,self).save(*args, **kwargs)


class Genre(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

# class Author(models.Model):
#     name = models.CharField(max_length=300)

#     def __str__(self):
#         return self.name

# class Memer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     mobile = models.CharField(max_length=16, blank=True, null=True)
#     bio = models.CharField(max_length=150, blank=False, null=False, default="Hey! I'm new here.")
#     cover = models.ImageField(upload_to='cover-images/%y/%m/%d/', default='cover-images/default/memerrank-bg.jpg', blank=False, null=False)
#     profile = models.ImageField(upload_to='profile-images/%y/%m/%d/', default='profile-images/default/memerrank-no-dp.jpg', blank=False, null=False)
#     def __str__(self):
#         return str(self.user)

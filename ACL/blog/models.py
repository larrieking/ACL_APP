from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import  User


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published'
                                                                    )


class Category(models.Model):
    category_name = models.CharField(max_length=50)


class Post(models.Model):

    def get_absolute_url(self):
        return reverse('post_detail', args = [self.publish.year, self.publish.month, self.publish.day, self.slug])
    objects = models.Manager()
    published = PublishedManager()


    STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'),)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    img = models.ImageField(upload_to='images/', blank=True)




class Meta:
    ordering = ('-publish',)

def __str__(self):
    return self.title
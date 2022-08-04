#from django.shortcuts import render

# Create your views here.
from django.shortcuts import  render, get_object_or_404
from .models import Post, Category

def post_list(request):
    posts = Post.published.all().order_by('publish')
    cover = posts[len(posts)-1]
    categories = Category.objects.all()

    return render(request, 'list.html', {'posts':posts, 'cover':cover, 'categories':categories})

def post_details(request, year, month, day, post):
    post = get_object_or_404(Post, slug = post, status='published', publish_year=year, publish_month=month, publish_day=day )
    return render(request, 'detail.html', {'post':post})
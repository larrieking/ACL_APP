#from django.shortcuts import render

# Create your views here.
from django.shortcuts import  render, get_object_or_404
from .models import Post, Category, Comment
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def post_list(request):


    posts = Post.published.all()
    paginator = Paginator(posts,4)
    page = request.GET.get('page')
    cover = posts[len(posts)-1]


    try:
        postss = paginator.page(page)
    except PageNotAnInteger:
        postss = paginator.page(1)
    except EmptyPage:
        postss = paginator.page(paginator.num_pages)


    return render(request, 'list.html', {'posts':postss, 'cover':cover,  'page':page})

def post_details(request, year, month, day, post):
    name = request.POST.get('name')
    email = request.POST.get('email')
    body = request.POST.get('body')



    post = get_object_or_404(Post, slug = post, status='published', publish__year=year, publish__month=month, publish__day=day )
    comments = post.comments.filter(active=True)
    new_comment = None



    if request.method == "POST":
        c1 = Comment(name=name, email=email, body=body, post = post)

        c1.save()
        print(comments)


    return render(request, 'detail.html', {'post':post,  "comments":comments})

def create_comment(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    body = request.POST.get('body')
    print(body)
    return render(request, 'detail.html')

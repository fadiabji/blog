from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm

def index(request):
    """ The home page for Blogs"""
    return render(request, 'blogs/index.html')

def posts(request):
    """ page shows all posts"""
    posts = BlogPost.objects.order_by('date_added')
    context = {'posts':posts}
    return render(request, 'blogs/posts.html', context)

def new_post(request):
    """ page to add a new post"""
    post = BlogPost
    if request.method != 'POST':
        #No data submitted; create a blank form.
        form = BlogPostForm()
    else:
        # POST data submitted; process data
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.post = post
            new_post.save()
            return redirect('blogs:posts')
    context = {'post':post, 'form':form}
    return render(request, 'blogs/new_post.html', context)  



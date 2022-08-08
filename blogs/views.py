from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

def index(request):
    """ The home page for Blogs"""
    return render(request, 'blogs/index.html')

def posts(request):
    """ page shows all posts"""
    posts = BlogPost.objects.order_by('date_added')
    author = posts.order_by('-date_added')
    context = {'posts':posts,'author':author}
    return render(request, 'blogs/posts.html', context)

@login_required
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
            new_post.author = request.user
            new_post.save()
            return redirect('blogs:posts')
    context = {'post':post, 'form':form}
    return render(request, 'blogs/new_post.html', context)  

@login_required
def edit_post(request, post_id):
    """Edit an existing post."""
    post = BlogPost.objects.get(id=post_id)
    check_post_author(request,post )
    if request.method != 'POST':
    # Initial request; pre-fill form with the current post.
        form = BlogPostForm(instance=post)
    else:
    # POST data submitted; process data.
        form = BlogPostForm(instance=post, data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('blogs:posts')
    context = {'post': post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)
        

def check_post_author(request, post):
    # Make sure the topic belongs to the current user.
    if post.author != request.user:
        raise Http404

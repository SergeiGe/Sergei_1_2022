from django.shortcuts import render
from .models import Post, Comment
from .forms import CommentForm
from django.http import HttpResponseRedirect

def blog_index(request):
    posts = Post.objects.all().order_by('-last_modified')
    context = {'posts': posts}
    return render(request, 'blog_index.html', context)

def blog_detail(request, primary_key):
    post = Post.objects.get(pk=primary_key)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post=post
            )
            comment.save()
            return HttpResponseRedirect(f'/blog/{primary_key}')

    comments = Comment.objects.filter(post=post).order_by('-created_on')
    context = {'post': post,
               'comments': comments,
               'form': form
               }
    return render(request, 'blog_detail.html', context)

def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category
    ).order_by('categories')
    context = {'category': category, 'posts': posts}
    return render(request, 'blog_category.html', context)


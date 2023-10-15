from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Post, Comment ,Category
from .forms import CommentForm


def blog_index(request):
   posts = Post.objects.filter(status=1).order_by('-created_on')
   categories = Category.objects.order_by('name')
   context = {
         "posts_all": posts,
         "categories_all":categories,
     }
   return render(request, "blog/blog_index.html", context)



def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog/blog_category.html", context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
    if form.is_valid():

        comment = Comment(
        author = form.cleaned_data["author"],
        body = form.cleaned_data["body"],
        post = post
           )
        comment.save()


    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }

    return render(request, "blog/blog_detail.html", context)
from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from .form import PostForm
from django.utils import timezone

# Create your views here.
def post_list(request):
    postsObject=Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts':postsObject})

def post_detail(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': posts})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
        return render(request, 'blog/post_new.html', {'form': form})
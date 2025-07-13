from django.shortcuts import render, get_object_or_404
from .models import Post
def all_blogs(request):
    posts = Post.objects.all()
    return render(request,'blogs/all_blogs.html',{'posts':posts})

def detail(request,blog_id):
    blog = get_object_or_404(Post,pk=blog_id)
    return render(request,'blogs/detail.html',{'blog':blog})
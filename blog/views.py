from django.shortcuts import render, get_object_or_404
from .models import Blog


# This function all_blogs was temporary to confirm we can display the all_blogs.html file
# def all_blogs(request):
#     return render(request, 'blog/all_blogs.html')


# # Create your views here.
def all_blogs(request):
    # create variable to get all blog objects
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})


def detail(request, blog_id):
# variable blog = retrieve Blog object that corresponds to the Blogs pk or primary key
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, "blog/detail.html",{'blog':blog})

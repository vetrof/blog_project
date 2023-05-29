from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import Post


class BlogListView(ListView):
    template_name = 'home.html'
    model = Post
    context_object_name = 'post_list'


# class BlogDetailView(DetailView):
#     model = Post
#     template_name = 'post_detail.html'



def BlogDetailView(request, pk):
    post_detail = Post.objects.get(pk=pk)
    contex = {'post_detail': post_detail}
    return render(request, 'post_detail.html', contex)

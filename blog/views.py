from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

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


class BlogCreateView(CreateView):
    template_name = 'post_new.html'
    fields = '__all__'
    model = Post
    # success_url = '/'


class BlogUpdateView(UpdateView):
    model = Post
    fields = ['title', 'body']
    template_name = 'post_edit.html'


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

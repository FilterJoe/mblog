from django.shortcuts import render, render_to_response
# from django.template import RequestContext # to get my css file to be seen
from django.views.generic import ListView, DetailView
from .models import Post


class PublishedPostsMixin(object):
    def get_queryset(self):
        queryset = super(PublishedPostsMixin, self).get_queryset()
        return queryset.filter(published=True)


class PostListView(PublishedPostsMixin, ListView):
    model = Post

    # def get_queryset(self):
    #     queryset = super(PostListView, self).get_queryset()
    #     return queryset.filter(published=True)


class PostDetailView(PublishedPostsMixin, DetailView):
    model = Post





# def blog_list(request, *args, **kwargs):
#     post_list = Post.objects.filter(published=True)
#     template_name = "post_list.html"
#     context = {
#         "post_list": post_list
#     }
#
#     return render(request, template_name, context)

# def blog_detail(request, pk, *args, **kwargs):
#     post = Post.objects.get(pk=pk, published=True)
#     template_name = "post_detail.html"
#     context = {
#         "post": post
#     }
#
#     return render(request, template_name, context)



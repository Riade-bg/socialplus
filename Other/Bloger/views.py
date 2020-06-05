from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, 
                                  DetailView, 
                                  CreateView,
                                  UpdateView, 
                                  DeleteView)
from .models import Post
# Create your views here.
from django.http import HttpResponse


class PostListView(ListView):
    model = Post
    template_name="index.html"
    context_object_name = 'posts'
    ordering = ["-date"]

class PostDetailView(DetailView):
    model = Post
    template_name="detail.html"


class PostCreatelView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'content']
    template_name="post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user        
        return super().form_valid(form)

class PostUpdatelView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name="post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user        
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeletelView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Post
    success_url = 'Bloger:home'
    template_name="post_confirm_delete.html"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
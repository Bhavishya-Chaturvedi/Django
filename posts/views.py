from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm


# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'post/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post_detail.html'

class PostCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post/post_form.html'
    success_url = reverse_lazy('posts:post_list')
    succes_message = "Post was created successfully!"

    def form_valid(sefl, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/posts_form.html'
    success_message = "Post was updated successfully!"

    def get_succes_url(self):
      return reverse_lazy('posts:post_detail',kwargs={'pk':self.object.pk})  

class PostDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Post 
    success_url = reverse_lazy('posts:post_list')
    success_message = "Post was deleted successfully!"
    
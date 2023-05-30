from typing import Optional
from django.shortcuts import render
# from django.http import HttpResponse #we dont need this as we are now using html directly
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def home(request):
    # return HttpResponse('<h1>Blog Home</h1>') #eta use kora jabe na karon httpsrespons e eto boro html code lekha jhamela. tai amra arekta use kori
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted'] #we have put a minus before it because it will sort the post based on new to old time.
    paginate_by = 2

    
class PostDetailView(DetailView): #<app>/<model>_<viewpoint>.html --> ei jaigai khujbe era here app name is blog and model name is Post. and viewpoint would be detail
    model = Post
     
class PostCreateView(LoginRequiredMixin,CreateView): # we need LoginRequireMixin to ensure that we are logged in when we creating a new post. otherwise it will send us to log in page.
    model = Post
    fields = ['title', 'content']

    def form_valid(self,form):
        form.instance.author = self.request.user #making the post author to current logged in user
        return super().form_valid(form)  #validating the form and creating the post

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView): # we need LoginRequireMixin to ensure that we are logged in when we creating a new post. otherwise it will send us to log in page.
    model = Post
    fields = ['title', 'content']

    def form_valid(self,form):
        form.instance.author = self.request.user #making the post author to current logged in user
        return super().form_valid(form)  #validating the form and creating the post
    
    def test_func(self):  #to check if the real author trying to update the post or not
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView): #loginreq and userpass both should be on left side
    model = Post
    success_url = '/'  #where should we land after deleting the psot

    def test_func(self):  #to check if the real author trying to update the post or not
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'}) 
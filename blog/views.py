from django.shortcuts import render
# from django.http import HttpResponse #we dont need this as we are now using html directly
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


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

class PostDetailView(DetailView): #<app>/<model>_<viewpoint>.html --> ei jaigai khujbe era here app name is blog and model name is Post. and viewpoint would be detail
    model = Post
     
class PostCreateView(LoginRequiredMixin,CreateView): # we need LoginRequireMixin to ensure that we are logged in when we creating a new post. otherwise it will send us to log in page.
    model = Post
    fields = ['title', 'content']

    def form_valid(self,form):
        form.instance.author = self.request.user #making the post author to current logged in user
        return super().form_valid(form)  #validating the form and creating the post

class PostUpdateView(LoginRequiredMixin,CreateView): # we need LoginRequireMixin to ensure that we are logged in when we creating a new post. otherwise it will send us to log in page.
    model = Post
    fields = ['title', 'content']

    def form_valid(self,form):
        form.instance.author = self.request.user #making the post author to current logged in user
        return super().form_valid(form)  #validating the form and creating the post


def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'}) 
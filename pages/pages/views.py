from django.views.generic import TemplateView,ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

class BlogListView(ListView):
    model =Post
    template_name='hero.html'

class BlogDetailView(DetailView):
    model=Post
    template_name='hero_detail.html'

class HeroAddView(CreateView):
    model=Post
    template_name='hero_add.html'
    fields='__all__'

class HeroEditView(UpdateView):
    model=Post
    template_name='hero_add.html'
    fields='__all__'


class BasePage(TemplateView):
    template_name="superhero_theme.html"

class HomePage(TemplateView):
    template_name='home.html'

#class BlogCreateView(CreateView):
    #model=Post
    #template_name='post_new.html'
    #fields=['title', 'author', 'body']

#class BlogUpdateView(UpdateView):
    #model=Post
    #template_name='post_edit.html'
    #fields=['title', 'body']

#class BlogDeleteView(DeleteView):
    #model=Post
    #template_name='post_delete.html'
    #success_url=reverse_lazy('home')
# Create your views here.

from django.urls import path
from .views import BlogListView, BlogDetailView, HeroAddView, HeroEditView, HomePage, BasePage


urlpatterns = [
    path('hero',BlogListView.as_view(), name='hero'),  
    path('<int:pk>', BlogDetailView.as_view(), name='hero_detail'),
    path('add', HeroAddView.as_view(),name='hero_add'),
    path('<int:pk>/',HeroEditView.as_view(), name='hero_edit'),
    path('', HomePage.as_view(), name='home'),
    path('home', HomePage.as_view(), name='home'),
    
]
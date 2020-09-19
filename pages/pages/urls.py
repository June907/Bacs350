from pages.views import AboutPage, BasePage, HeroView,IndexPage
from django.urls import path

urlpatterns = [
    path('', IndexPage.as_view()),
    path('about', AboutPage.as_view()),
    path('base', BasePage.as_view()),
    path('<str:identity>', HeroView.as_view()),
]
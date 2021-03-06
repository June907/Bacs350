from django.urls import path

from .views import *


urlpatterns = [
    
    path('workshop/', HomeView.as_view(), name='workshop'),

    path('workshop/card',  CardView.as_view(), name='card'),
    path('workshop/cards',  CardsView.as_view(), name='cards'),
    path('workshop/doc/<str:doc>',  DocumentView.as_view(), name='doc'),
    
    path('workshop/table',  TableView.as_view(), name='table'),
    path('workshop/tabs',  TabsView.as_view(), name='tabs'),

    path('workshop/accordion',  AccordionView.as_view(), name='accordion'),
    path('workshop/carousel',  CarouselView.as_view(), name='carousel'),
    path('workshop/superview',  SuperView.as_view(), name='superview'),

]
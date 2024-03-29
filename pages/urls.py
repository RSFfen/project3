from django.urls import path

from .views import HomePageView, AboutPageView # new
from .views import CarsPageView # new
from .views import HelpPageView # new
from .views import CommentCreateView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'), # new
    path('', HomePageView.as_view(), name='home'),
    path('cars/', CarsPageView.as_view(), name='cars'), # new
    path('help/', HelpPageView.as_view(), name='help'), # new
    path('comment_new/', CommentCreateView.as_view(), name='comment_new'),    
]

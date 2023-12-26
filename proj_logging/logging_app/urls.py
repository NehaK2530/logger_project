from django.urls import path
from .views import PostAPI 


urlpatterns = [
   path('posts/',PostAPI.as_view()),

]
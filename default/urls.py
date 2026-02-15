from django.urls import path
from . import views

urlpatterns = [
    path('menu/' , views.PollList.as_view()),

]
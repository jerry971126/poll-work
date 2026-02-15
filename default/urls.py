from django.urls import path
from . import views

urlpatterns = [
    path('store/' , views.PollList.as_view()),

]
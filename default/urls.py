from django.urls import path
from . import views

urlpatterns = [
    path('store/' , views.PollList.as_view()),
    path('store/<int:pk>/', views.PollDetail.as_view()),
    path('submit_order/', views.submit_order, name='submit_order'),
]
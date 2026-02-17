from django.urls import path
from . import views

urlpatterns = [
    path('store/' , views.PollList.as_view()),
    path('store/<int:pk>/', views.PollDetail.as_view()),
    path('submit_order/', views.submit_order, name='submit_order'),
    path('order_success/<int:order_id>/', views.order_success, name='order_success'),
    path('all_order/', views.AllOrders.as_view(), name='all_orders'),
    path('store/create/', views.PollCreate.as_view()),
    path('poll/<int:pk>/update/', views.PollUpdate.as_view()),
    
]
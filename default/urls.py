from django.urls import path, include
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('',RedirectView.as_view(url='store')),
        path('accounts/', include('django.contrib.auth.urls')),
    path('store/' , views.PollList.as_view()),
    path('store/<int:pk>/', views.PollDetail.as_view() , name='poll_view'),
    path('submit_order/', views.submit_order, name='submit_order'),
    path('order_success/<int:order_id>/', views.order_success, name='order_success'),
    path('all_order/', views.AllOrders.as_view(), name='all_orders'),
    path('store/create/', views.PollCreate.as_view()),
    path('store/<int:pk>/update/', views.PollUpdate.as_view()),
    path('store/<int:pk>/delete/', views.PollDelete.as_view()),
    path('option/create/<int:pid>/', views.OptionCreate.as_view()), 
    path('option/<int:pk>/update/', views.OptionUpdate.as_view()),
    path('option/<int:pk>/delete/', views.OptionDelete.as_view()),
    path('register/', views.register, name='register'),
]
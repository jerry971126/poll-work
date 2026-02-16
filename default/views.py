from django.shortcuts import render ,redirect
from django.views.generic import ListView , DetailView
from .models import *

# Create your views here.
class PollList(ListView):
    model=Poll
    template_name ='default/poll_list.html'

class PollDetail(DetailView):
    model = Poll
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['options'] = Option.objects.filter(poll=self.get_object())
        context['sugar_levels'] = SugarLevel.objects.all()
        context['ice_levels'] = IceLevel.objects.all()
        context['toppings'] = Topping.objects.all()
        return context
def submit_order(request):      #接下來這裡是整理飲料的所有參數

    if request.methond == 'POST':  
        return#未結束  
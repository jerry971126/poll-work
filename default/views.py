from django.shortcuts import render ,redirect, get_object_or_404
from django.views.generic import ListView , DetailView
from .models import *
from django.views.generic.edit import CreateView,UpdateView,DeleteView

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

    if request.method == 'POST':  
        drink_id = request.POST.get('drink')
        sugar_id = request.POST.get('sugar')
        ice_id = request.POST.get('ice')
        topping_id = request.POST.get('topping')
    new_order = Order.objects.create(
            drink_id=drink_id,
            sugar_id=sugar_id,
            ice_id=ice_id,
            customer_name=request.user.username if request.user.is_authenticated else "匿名同學"
        )
    if topping_id:
            new_order.toppings.set(topping_id)

        # 存完後跳轉到結果頁面，並帶上訂單 ID
    return redirect('order_success', order_id=new_order.id)
def order_success(request, order_id): #這邊我要建立一的頁面
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'default/order_success.html', {'order': order})
class AllOrders(ListView):
     model = Order
     template_name = 'default/all_orders.html'
     context_object_name = 'order'
class PollCreate(CreateView):
     model = Poll
     fields = ['subject']
     success_url = '/store/'
     template_name = 'default/general_form.html'
class PollUpdate(UpdateView):
     model = Poll
     fields = ['subject']
     success_url = '/store/'
     template_name = 'default/general_form.html'
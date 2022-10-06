from django.shortcuts import render
from .models import Order
from .forms import OrderForms
from cms.models import CmsSlider
from price.models import *
from telebot.sendmessage import *


# Create your views here.


def first_page(request):
    slider_list = CmsSlider.objects.all()
    pc_1 = PriceCard.objects.get(id=1)
    pc_2 = PriceCard.objects.get(id=2)
    pc_3 = PriceCard.objects.get(id=3)
    price_table = PriceTable.objects.all()
    form = OrderForms()
    dict_obj = {'slider_list': slider_list,
                'pc_1': pc_1,
                'pc_2': pc_2,
                'pc_3': pc_3,
                'price_table': price_table,
                'form': form
                }
    return render(request, './index.html', dict_obj)


def thanks_page(request):
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        element = Order(order_name=name, order_phone=phone)
        element.save()
        SendTelegramm(tg_name=name, tg_phone=phone)
        return render(request, './thanks.html', {'name': name})
    else:
        return render(request, './thanks.html')




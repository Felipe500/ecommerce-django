from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View


class PayOrderView(ListView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('s')


class DetailOrderView(ListView):
    pass


class SaveOrder(ListView):
    pass




from django.shortcuts import render
from django.views import View
from .models import Subscriptions


class HOME(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


def Subscribe(request):
    plans = Subscriptions.objects.all()
    for p in plans:
        temp = p.Devices.split('+')
        p.Devices = temp
    context = {'plans': plans}
    return render(request, 'monthlyPlan.html', context)


def SubscribeYearly(request):
    plans = Subscriptions.objects.all()
    for p in plans:
        temp = p.Devices.split('+')
        p.Devices = temp
    context = {'plans': plans}
    return render(request, 'yearlyPlan.html', context)


def confirm(request):
    context = {}
    monthly = request.POST.get('monthly', None)
    plans = Subscriptions.objects.all()
    for p in plans:
        temp = p.Devices.split('+')
        p.Devices = temp
    print(monthly)
    context['monthly'] = monthly
    context['plans'] = plans
    return render(request, 'payment.html', context)


def confirmYearly(request):
    context = {}
    yearly = request.POST.get('yearly', None)
    plans = Subscriptions.objects.all()
    for p in plans:
        temp = p.Devices.split('+')
        p.Devices = temp
    print(yearly)
    context['yearly'] = yearly
    context['plans'] = plans
    return render(request, 'payment.html', context)

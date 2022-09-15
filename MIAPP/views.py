
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import View
from .models import Subscriptions
#from django.conf import settings
#from django.shortcuts import redirect


class HOME(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


@login_required(redirect_field_name='MI:HOME')
def Subscribe(request):
    plans = Subscriptions.objects.all()
    for p in plans:
        temp = p.Devices.split('+')
        p.Devices = temp
    context = {'plans': plans}
    return render(request, 'monthlyPlan.html', context)


@login_required(redirect_field_name='MI:HOME')
def SubscribeYearly(request):
    plans = Subscriptions.objects.all()
    for p in plans:
        temp = p.Devices.split('+')
        p.Devices = temp
    context = {'plans': plans}
    return render(request, 'yearlyPlan.html', context)


@login_required(redirect_field_name='MI:HOME')
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


@login_required(redirect_field_name='MI:HOME')
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

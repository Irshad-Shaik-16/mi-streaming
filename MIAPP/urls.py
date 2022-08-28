
from django.urls import path
from .views import HOME, Subscribe, SubscribeYearly, confirm, confirmYearly

app_name = 'MIAPP'

urlpatterns = [
    path('', HOME.as_view(), name='HOME'),
    path('Subscribe', Subscribe, name='Subscribe'),
    path('SubscribeYearly', SubscribeYearly, name='SubscribeYearly'),
    path('payment/', confirm, name='confirm'),
    path('paymentYearly/', confirmYearly, name='confirmYearly')
]

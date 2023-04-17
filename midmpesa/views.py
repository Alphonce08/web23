from __future__ import unicode_literals
from django.http import HttpResponse, JsonResponse
from django_daraja.mpesa.core import MpesaClient
from django.shortcuts import render

cl = MpesaClient()
stk_push_callback_url = 'https://api.darajambili.com/expess-payment'
b2c_callback_urs = 'https://api.darajambili.com/b2c/results'


def cauth_success(request):
    r = cl.access_token()
    return JsonResponse(r, safe=False)


def index(request):
    if request.method == 'POST':
        phone_number = request.POST.get('form')
        amount = request.POST.get("amount")
        amount = int(amount)
        account_refeence = "Victor"
        transaction_description = "STK Push Description"
        callback_url = stk_push_callback_url
        r = cl.stk_push(phone_number, amount, account_refeence, transaction_description, callback_url)
        return JsonResponse(r.response_description, safe=False)
    return render(request, 'index.html')

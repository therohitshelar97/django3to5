from django.shortcuts import render, HttpResponse
from django.contrib import messages
# from razorpay import Client
import razorpay

# Create your views here.

def Pay(request):
    client = razorpay.Client(auth=("rzp_test_nTflZwWcazIDRj","xi"))
    amount = 165
    data = { "amount": amount, "currency": "INR", "receipt": "order_rcptid_11" }
    # payment = client.order.create(data=data)  
    context = {}
    context['name'] = 'Rohit Shelar'
    context['email'] = 'example@gmail.com'
    context['amt'] = data['amount']*100
    print(context)
    return render(request,'pay.html',context)

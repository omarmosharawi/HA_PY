import math

from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from book_store import settings
from .forms import UserInfoForm, MyPayPalPaymentsForm
from .models import Transaction, PaymentMethod
from store.models import Product, Cart, Order
# from django.core.mail import send_mail
# from django.template.loader import render_to_string
from django.utils.translation import gettext as _
from paypal.standard.forms import PayPalPaymentsForm
from django.http import HttpResponse

import stripe


# Create your views here.


# def makeOrder(request):
#     if request.method != 'POST':
#         return redirect('store.checkout')
#
#     form = UserInfoForm(request.POST)
#     if form.is_valid():
#         cart = Cart.objects.filter(session=request.session.session_key).last()
#         products = Product.objects.filter(pk__in=cart.item)
#
#         total = 0
#         for item in products:
#             total += item.price
#
#         if total <= 0:
#             return redirect('store.cart')
#
#         order = Order.objects.create(customer=form.cleaned_data, total=total)
#         for product in products:
#             order.orderproduct_set.create(product_id=product.id, price=product.price)
#
#         send_orderEmail(order, products)
#
#         cart.delete()
#         return redirect('store.checkout-complete')
#     else:
#         return redirect('store.checkout')


def stripe_config(request):
    return JsonResponse({
        'public_key': settings.STRIPE_PUBLISHABLE_KEY
    })


def stripe_transaction(request):
    transaction = makeTransaction(request, PaymentMethod.Stripe)
    if not transaction:
        return JsonResponse({
            'message': _('Please enter valid information.')
        }, status=400)
    stripe.api_key = settings.STRIPE_SECRET_KEY
    intent = stripe.PaymentIntent.create(
        amount=transaction.amount * 100,
        currency=settings.CURRENCY,
        payment_method_types=['card'],
        metadata={
            'transaction': transaction.id
        }
    )
    return JsonResponse({
        'client_secret': intent['client_secret']
    })


def paypal_transaction(request):
    transaction = makeTransaction(request, PaymentMethod.Paypal)
    if not transaction:
        return JsonResponse({
            'message': _('Please enter valid information.')
        }, status=400)

    form = MyPayPalPaymentsForm(initial={
        'business': settings.PAYPAL_EMAIL,
        'amount': transaction.amount,
        'invoice': transaction.id,
        'currency_code': settings.CURRENCY,
        'return_url': f'http://{request.get_host()}{reverse("store.checkout-complete")}?invoice='+str(transaction.id),
        'cancel_url': f'http://{request.get_host()}{reverse("store.checkout")}',
        'notify_url': f'http://{request.get_host()}{reverse("checkout.paypal-webhook")}',
    })

    return HttpResponse(form.render())


def makeTransaction(request, pm):
    form = UserInfoForm(request.POST)
    if form.is_valid():
        cart = Cart.objects.filter(session=request.session.session_key).last()
        products = Product.objects.filter(pk__in=cart.item)

        total = 0
        for item in products:
            total += item.price

        if total <= 0:
            return None

        return Transaction.objects.create(
            customer=form.cleaned_data,
            session=request.session.session_key,
            payment_method=pm,
            items=cart.item,
            amount=math.ceil(total))


# def send_orderEmail(order, products):
#     msg_html = render_to_string('emails/order.html',
#                                 {
#                                     'order': order,
#                                     'products': products,
#                                 })
#     send_mail(
#         subject='New Order',
#         html_message=msg_html,
#         message=msg_html,
#         from_email='noreply@example.com',
#         recipient_list=[order.customer['email']]
#     )

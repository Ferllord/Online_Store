from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from .forms import OrderForm
from django.shortcuts import reverse
import stripe
from django.conf import settings
from django.shortcuts import HttpResponseRedirect
from http import HTTPStatus

stripe.api_key = settings.STRIPE_SECRET_URL


class SuccerssView(TemplateView):
    template_name = 'orders/success.html'


class CanceledView(TemplateView):
    template_name = 'orders/cancled.html'


class OrderCreateView(CreateView):
    template_name = 'orders/order-create.html'
    form_class = OrderForm
    success_url = reverse_lazy('orders:order_create')

    def post(self, request, *args, **kwargs):
        super(OrderCreateView, self).post(request, *args, **kwargs)
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': 'price_1NpHFlEKFOE4tPlt3yVZNFWI',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=f'{settings.DOMAIN_NAME}{reverse("orders:order_success")}',
            cancel_url=f'{settings.DOMAIN_NAME}{reverse("orders:order_canceled")}',
        )
        return HttpResponseRedirect(checkout_session.url, status=HTTPStatus.SEE_OTHER)

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super(OrderCreateView, self).form_valid(form)

@csrf_exempt
def my_webhook_view(request):
  payload = request.body
  print(payload)

  return HttpResponse(status=200)
from django.shortcuts import render
from django.views.generic import TemplateView
from hotel.models import *


class IndexPage(TemplateView):
    def get(self, request, **kwargs):
        hotel_data = []
        all_hotels = Hotel.objects.order_by('star').all()[:6]

        for hotel in all_hotels:
            hotel_data.append({
                'name': hotel.name,
                'cover': hotel.cover.url,
                'star': hotel.star,
                't': 5 - hotel.star,
                'price': hotel.price,
                'city': hotel.city,
            })

        context = {
            'hotel_data': hotel_data,
        }

        return render(request, 'index.html', context)


class LoginPage(TemplateView):
    template_name = "login.html"

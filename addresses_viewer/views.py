#!/usr/bin/python
from django.http import HttpResponse, JsonResponse
from django.template import loader

from .models import Address
from addresses_viewer import fusion_tables


def index(request):
    addresses = Address.objects.all()

    template = loader.get_template('index.html')
    context = {
        'addresses': addresses,
    }
    return HttpResponse(template.render(context, request))


def get_addresses(request):
    return JsonResponse({"rows": fusion_tables.all()})
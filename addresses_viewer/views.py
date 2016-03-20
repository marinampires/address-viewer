#!/usr/bin/python
from django.http import HttpResponse, JsonResponse
from django.template import loader

from .models import Address
from .fusion_tables import get_fusion_table_id, get_fusion_table_addresses

def viewport(request):
    addresses = Address.objects.all()

    template = loader.get_template('viewport.html')
    context = {
        'addresses': addresses,
    }
    return HttpResponse(template.render(context, request))


def get_table_id(request):
    return JsonResponse({"table_id": get_fusion_table_id()})


def get_addresses(request):
    return JsonResponse({"rows": get_fusion_table_addresses()})
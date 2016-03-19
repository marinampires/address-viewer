from django.http import HttpResponse
from django.template import loader

from .models import Address

def viewport(request):
    addresses = Address.objects.all()

    template = loader.get_template('viewport.html')
    context = {
        'addresses': addresses,
    }
    return HttpResponse(template.render(context, request))


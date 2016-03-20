#!/usr/bin/python
from django.http import HttpResponse
from django.template import loader

from .models import Address

# import simplejson, httplib

def viewport(request):
    addresses = Address.objects.all()

    template = loader.get_template('viewport.html')
    context = {
        'addresses': addresses,
    }
    return HttpResponse(template.render(context, request))


def insert_address(request):
    print ('IMPORT ROWS')

    from datetime import datetime
    import requests

    api_key = "AIzaSyChheeZwvelzt1iEjLSWlRlMF3UmZI6afU"
    tableid = "12a2tPdPOGzY-draRlwRrHtAirL1JC7GUXlq"
    date = str(datetime.now().date())
    data = {'Date': date,
            'Address Name': 'Teste',
            'Location': '(-22.74642, -43.17489624)',
            'Place ID': 'fafasffsoooo9888'}
    url = 'https://www.googleapis.com/upload/fusiontables/v1/tables/%s/import' % tableid # self.params is access token
    print (url)

    importRow = requests.post(url, params=data, headers={'Authorization': api_key})
    import ipdb;ipdb.set_trace()

    return HttpResponse("done")
#     client_id = "1061866540241-l5urrj9976mjg3ffjmmckirq6k6bc39j.apps.googleusercontent.com"
#     client_secret = "guLy57Zq7op2KHX9POn-H-5M"
#     redirect_uri = "http://test.com/oauth2callback"a3e8T"

#     data = '''{
#       "Address Name": "teste",
#       "tableId": %s
#     }''' % (tableid)
#     response = self.runRequest(
#       "POST",
#       "/fusiontables/v1/tables/%s/styles%s" % \
#         (tableid, self.params),
#       data,
#       headers={'Content-Type':'application/json'})
#     json_response = simplejson.loads(response)
#     return json_response["styleId"]


# def runRequest(self, method, url, data=None, headers=None):
#     request = httplib.HTTPSConnection("www.googleapis.com")

#     if data and headers: request.request(method, url, data, headers)
#     else: request.request(method, url)
#     response = request.getresponse()
#     print (response.status, response.reason)
#     response = response.read()
#     print response
    # return response
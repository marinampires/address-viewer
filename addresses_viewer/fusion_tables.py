import json
from django.conf import settings
from datetime import datetime

import os

from oauth2client.client import flow_from_clientsecrets
import httplib2

from apiclient import discovery
from oauth2client import client
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials


CLIENT_SECRETS = os.path.join(os.path.dirname(__file__), 'oauth_credentials.json')
scopes = ['https://www.googleapis.com/auth/fusiontables']

def _get_service():
    credentials = ServiceAccountCredentials.from_json_keyfile_name(CLIENT_SECRETS, scopes)
    http_auth = credentials.authorize(httplib2.Http())
    service = build('fusiontables', 'v2', http=http_auth)
    return service


def save(address):
    service = _get_service()

    #get the table
    table_id = get_fusion_table_id()

    date = datetime.now().strftime("%Y-%m-%d")
    sql_insert = "INSERT INTO %s (date,address,lat_long) VALUES('%s', '%s', '(%f,%f)')" % (table_id, date, address.address_name, address.lat, address.lng)
    sql = service.query().sql(sql=sql_insert).execute()


def get_fusion_table_addresses():
    service = _get_service()
    table_id = get_fusion_table_id()
    sql_list = "select address, lat_long from %s" % table_id
    sql = service.query().sql(sql=sql_list).execute()

    return sql['rows']


def get_fusion_table_id():
    service = _get_service()
    table_list = service.table().list().execute()

    if "items" not in table_list.keys():
        #do not have table
        table_definition = {"columns": [{"name": "address","type": "STRING"},{"name": "lat_long","type": "LOCATION"}, {"name":"date", "type": "DATETIME"}],"isExportable": True,"name": "addresses"}
        service.table().insert(body=table_definition).execute()
        table_list = service.table().list().execute()

    #get the table
    table_id = [table['tableId'] for table in table_list['items']][0]

    return table_id
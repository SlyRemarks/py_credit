#!/usr/bin/env python

import requests
import config
import json

clientId    = config.bigCommerce['client_id']
storeHash   = config.bigCommerce['store_hash']
accessToken = config.bigCommerce['access_token']
order_id    = config.bigCommerce['order_id']

headers = {

    'X-Auth-Client' : clientId,
    'X-Auth-Token'  : accessToken,
    'Accept'        : 'application/json',
    'Content-Type'  : 'application/json'
}

params = {
    
    'min_id' : order_id
}

r = requests.get(
        'https://api.bigcommerce.com/stores/' +
        storeHash +
        '/v2/orders',
        params=params, headers=headers
    )

r = r.json()

with open('latestOrders.json', 'w') as outfile:
    json.dump(r, outfile)
#!/usr/bin/env python

import requests
import json

client_id    = 'xxxxxxxxx'
store_hash   = 'xxxxxxxxx'
access_token = 'xxxxxxxxx'

headers = {
    'X-Auth-Client' : client_id,
    'X-Auth-Token'  : access_token,
    'Accept'        : 'application/json',
    'Content-Type'  : 'application/json'
}

r = requests.put(
    'https://api.bigcommerce.com/stores/' +
    store_hash +
    '/v2/hooks/xxxxxxxxx',
    json = {
        'is_active'   : 1,
        'scope'       : 'xxxxxxxxx',
        'destination' : 'xxxxxxxxx',
        'headers'     : {'accesskey' :'xxxxxxxxx'}},
    headers=headers
)

print r

r = r.json()

print r

#----------------------------------------------------------------------------------------
'''
#GET_webhook

import requests
import json

clientId    = 'xxxxxxxxx'
storeHash   = 'xxxxxxxxx'
accessToken = 'xxxxxxxxx'

headers = {
'X-Auth-Client' : clientId,
'X-Auth-Token'  : accessToken,
'Accept'        : 'application/json',
'Content-Type'  : 'application/json'
}
 
params = {
'scope'       : 'xxxxxxxxx',
'destination' : 'xxxxxxxxx',
'is_active'   : 1,
}

r = requests.get(
'https://api.bigcommerce.com/stores/' +
storeHash +
'/v2/hooks',
headers=headers
)

r = r.json()

print r
'''
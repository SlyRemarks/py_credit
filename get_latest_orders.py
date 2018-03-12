#!/usr/bin/env python

import requests
import config
import json

#------------------------------------------------------------------------------------

class GetLatestOrders:

    clientId    = config.bigcommerce['client_id']
    storeHash   = config.bigcommerce['store_hash']
    accessToken = config.bigcommerce['access_token']
    order_id    = config.bigcommerce['order_id']

    headers = {
    'X-Auth-Client' : clientId,
    'X-Auth-Token'  : accessToken,
    'Accept'        : 'application/json',
    'Content-Type'  : 'application/json'
    }

    def __init__(self, last_known_order):
        self.last_known_order = last_known_order

    def get_latest_order(self):
        params = {'min_id' : self.last_known_order}

        r = requests.get(
        'https://api.bigcommerce.com/stores/' +
        self.storeHash +
        '/v2/orders',
        params=params, headers=self.headers
        )

        r = r.json()

        e = []
        
        for key in r:
            
            a = 0
            b = 0
            c = ""
            d = ""
            
            for item in key:
                
                if item == "customer_id":
                    if key[item] != 0:
                        a = key[item]
        
                if item == "id":
                    if key[item] != 0:
                        b = key[item]
        
                if item == "subtotal_ex_tax":
                        c = key[item]
                        c = float(c)
        
                if item == "status":
                        d = key[item]
                        d = d.encode('utf8')
                
            if a != 0:
                if d == "Shipped":
                        e.append([a,b,c,d])
            
        for x in e:
            print x
        
#------------------------------------------------------------------------------------

last_known_order = '17240' #last number in list
y = GetLatestOrders(last_known_order)
y.get_latest_order()

#with open('data/latestOrders.json', 'w') as outfile:
#    json.dump(r, outfile)





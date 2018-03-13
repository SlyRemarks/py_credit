#!/usr/bin/env python

import requests
import json
import MySQLdb
import assets.config as config

#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

#class DatabaseInput:
    
#    mydb = MySQLdb.connect(
        
#    host   = config.database['host'],
#    user   = config.database['user'],
#    passwd = config.database['passwd'],
#    db     = config.database['db']
    
#    )

    
    #cursor = mydb.cursor()

#file = open("data/customerList.csv", "rb")
#reader = csv.reader(file)
##################next(file) # ignore header
#for row in reader:
#####################    valid = True   # isdigit
###################    id = row[0]
#################    if not numeric id: valid = False
    
#    cursor.execute('INSERT INTO customers( id, email, spend )' \
#    'VALUES( %s, %s, %s)',(int(float(row[0])),row[1],row[9]))
    
#mydb.commit()
#cursor.close()
#print "Done"

#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
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
    
#------------------------------------------------------------------------------------

    def __init__(self, last_known_order):
        self.last_known_order = last_known_order

#------------------------------------------------------------------------------------

    def get_latest_orders(self):
        params = {'min_id' : self.last_known_order}

        r = requests.get(
        'https://api.bigcommerce.com/stores/' +
        self.storeHash +
        '/v2/orders',
        params=params, headers=self.headers
        )
        
        try:
            api_result = r.json()
        except ValueError:
            return False
        return api_result

#------------------------------------------------------------------------------------
        
    def sort_latest_orders(self, x):
        
        result = []
        
        for key in x:
            
            customer_id = 0
            order_id    = 0
            subtotal    = 0
            status      = ""
            
            for item in key:
                
                if item == "customer_id":
                    if key[item] != 0:
                        customer_id = key[item]
        
                if item == "id":
                    if key[item] != 0:
                        order_id = key[item]
        
                if item == "subtotal_ex_tax":
                        subtotal = key[item]
                        subtotal = float(subtotal)
        
                if item == "status":
                        status = key[item]
                        status = status.encode('utf8')
                
            if customer_id != 0:
                if status == "Shipped" and subtotal != 0:
                        result.append([customer_id, order_id, subtotal, status])
            
        return result

#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

last_known_order = '17220'
get_orders       = GetLatestOrders(last_known_order)
api_result       = get_orders.get_latest_orders()

if api_result is not False:
    c = get_orders.sort_latest_orders(api_result)
    print c
else:
    print 'ah well, maybe another time...'
    
#------------------------------------------------------------------------------------






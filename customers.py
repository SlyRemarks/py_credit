#!/usr/bin/env python

import requests
import config
import json

data = {}

with open('latestOrders.json', 'r') as data_file:
    data = json.load(data_file)

e = []

for key in data:
    
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

        if item == "status":
                d = key[item]
                
    
    e.append([a,b,c,d])
    
for x in e:
    print x
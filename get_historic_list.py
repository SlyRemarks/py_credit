#!/usr/bin/env python

# -----------------------------------------------------------------------------------
# ---------- Extract historic data from BigCommerce csv file (emonCredit) -----------
# -----------------------------------------------------------------------------------

import csv

#------------------------------------------------------------------------------------

def orders_sort():
    a = []
    with open('data/orders.csv') as open_csv:
        reader = csv.reader(open_csv)
        sort_list = sorted(reader, key=lambda x: int(x[3]), reverse = False) #-- sort by customer id
        for i,row in enumerate(sort_list):
            if row[1] == "Shipped": # ----------------------------------------- make sure order has been shipped
                if int(row[3]) != 0:
                    a.append(row[2:5])
                #if(i >= 50): # ------------------------------------------- limit inputs
                    #break
    return a
    
#------------------------------------------------------------------------------------

def orders_cast():
    a = orders_sort()
    b = []
    for foo in a :
        foo[0] = float(foo[0])
        foo[1] = int(foo[1])
        b.append(foo)
        
    return b

# -----------------------------------------------------------------------------------

def orders_combine():
    
    b = orders_cast()
    c = []
    idCheck = 0
    spendCheck = 0
    emailCheck = ""
    
    for foo in b:
        if foo[1] == idCheck:
            foo[0] = foo[0] + spendCheck
            spendCheck = foo[0]
            idCheck = foo[1]
            emailCheck = foo[2]
        else:
            sumCheck = [spendCheck,idCheck,emailCheck]
            if idCheck != False:
                c = c[:-1]
                c.append(sumCheck)
            idCheck = foo[1]
            spendCheck = foo[0]
            emailCheck = foo[2]
            c.append(foo)

    return c
    
# -----------------------------------------------------------------------------------

c = orders_combine()

close_csv = open('data/customerList.csv', 'w')
with close_csv:
    writer = csv.writer(close_csv)
    writer.writerows(c)

# -----------------------------------------------------------------------------------
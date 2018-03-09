#!/usr/bin/env python

# -----------------------------------------------------------------------------------
# ---------------- Extract historic data from BigCommerce csv file ------------------
# -----------------------------------------------------------------------------------

import csv

# -----------------------------------------------------------------------------------

a = []
b = []
c = []

#------------------------------------------------------------------------------------

with open('data/orders.csv') as openCsv:
    reader = csv.reader(openCsv)
    sortList = sorted(reader, key=lambda x: int(x[3]), reverse = False) #-- sort by customer id
    for i,row in enumerate(sortList):
        if row[1] == "Shipped": # ----------------------------------------- make sure order has been shipped
            if int(row[3]) != 0:
                a.append(row[2:5])
                #if(i >= 50): # ------------------------------------------- limit inputs
                    #break

#------------------------------------------------------------------------------------

for foo in a :
    foo[0] = float(foo[0])
    foo[1] = int(foo[1])
    b.append(foo)

# -----------------------------------------------------------------------------------

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

# -----------------------------------------------------------------------------------

closeCsv = open('data/customerList.csv', 'w')
with closeCsv:
    writer = csv.writer(closeCsv)
    writer.writerows(c)

# -----------------------------------------------------------------------------------
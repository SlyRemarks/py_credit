#!/usr/bin/env python

import MySQLdb
import csv

host = config.bigCommerce['host']
user = config.bigCommerce['user']
passwd = config.bigCommerce['passwd']
db = config.bigCommerce['db']

mydb = MySQLdb.connect(
    host   = host,
    user   = user,
    passwd = passwd,
    db     = db
    )
    
cursor = mydb.cursor()

file = open("customers.csv", "rb")
reader = csv.reader(file)
next(file) # ignore header
for row in reader:
#    valid = True   # isdigit
#    id = row[0]
#    if not numeric id: valid = False
    
    cursor.execute('INSERT INTO customers( id, email, spend )' \
    'VALUES( %s, %s, %s)',(int(float(row[0])),row[1],row[9]))
    
mydb.commit()
cursor.close()
print "Done"
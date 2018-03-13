#!/usr/bin/env python

import MySQLdb
import csv
import assets.config as config

#------------------------------------------------------------------------------------

host   = config.database['host']
user   = config.database['user']
passwd = config.database['passwd']
db     = config.database['db']

mydb = MySQLdb.connect(
    host   = host,
    user   = user,
    passwd = passwd,
    db     = db
)
 
#------------------------------------------------------------------------------------
    
cursor = mydb.cursor()

file = open("assets/customerList.csv", "rb")
reader = csv.reader(file)
#next(file) # ignore header
for row in reader:
#    valid = True   # isdigit
#    id = row[0]
#    if not numeric id: valid = False
    
    cursor.execute('INSERT INTO customers( id, email, spend )' \
    'VALUES( %s, %s, %s)',(row[1],row[2],row[0]))

mydb.commit()
cursor.close()

print "Done"
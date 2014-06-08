 #!/bin/python

from datetime import datetime

loc_offers = "../data/offers_backup.csv"
loc_transactions = "../data/transactions.csv"
loc_train = "../data/trainHistory.csv"
loc_reduced = "../data/reduced_by_customer.csv" # will be created

def reduce_data_by_category(loc_offers, loc_transactions, loc_reduced):

    start = datetime.now()
    #get all categories on offer in a dict
    offers = {}
    for e, line in enumerate( open(loc_offers) ):
        offers[ line.split(",")[1] ] = 1

    #open output file
    with open(loc_reduced, "wb") as outfile:
        #go through transactions file and reduce
        reduced = 0
        for e, line in enumerate( open(loc_transactions) ):
            if e == 0:
                outfile.write( line ) #print header
            else:
                #only write when category in offers dict
                if line.split(",")[3] in offers:
                    outfile.write( line )
                    reduced += 1
            #progress
            if e % 5000000 == 0:
                print e, reduced, datetime.now() - start
    print e, reduced, datetime.now() - start

def reduce_data_by_customer(loc_offers, loc_transactions, loc_reduced, loc_train):

    start = datetime.now()
    #get all categories on offer in a dict
    customer = {}
    for e, line in enumerate( open(loc_train) ):
        customer[ line.split(",")[0] ] = 1

    #open output file
    with open(loc_reduced, "wb") as outfile:
        #go through transactions file and reduce
        reduced = 0
        for e, line in enumerate( open(loc_transactions) ):
            if e == 0:
                outfile.write( line ) #print header
            else:
                #only write when category in offers dict
                if line.split(",")[0] in customer:
                    outfile.write( line )
                    reduced += 1
            #progress
            if e % 5000000 == 0:
                print e, reduced, datetime.now() - start
    print e, reduced, datetime.now() - start

reduce_data_by_customer(loc_offers, loc_transactions, loc_reduced, loc_train)

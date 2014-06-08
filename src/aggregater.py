#!/bin/python

# Script to aggregate the data according to customer id

from datetime import datetime

loc_transactions = "../data/trans_cat.csv"
loc_joined = "../data/offersAndTrainJoined.csv"
loc_aggregated = "../data/aggregated_by_customer_train_cat.csv" # will be created

def aggregate_by_customer(loc_joined, loc_transactions, loc_aggregated):

    start = datetime.now()

    customer = {}
    for e, row in enumerate( open(loc_joined) ):
        if row.split(",")[0] in customer:
            pass
        else:
            # list order is: category, company, brand and date
            customer[row.split(",")[0]] = [row.split(",")[8], row.split(",")[10], row.split(",")[12].split("\n")[0], row.split(",")[6]]

    aggregated = {}
    for key in customer:
        aggregated[key] = [0,0,0,0,0,0,0]

    for e, line in enumerate(open(loc_transactions)):
        if e == 0:
            pass
        else:
            if line.split(",")[0] in customer and customer[line.split(",")[0]][3] > line.split(",")[6]:
                # Aggregate on category
                if str(line.split(",")[3]) == str(customer[line.split(",")[0]][0]):
                    aggregated[line.split(",")[0]][0] +=1
                else:
                    pass

                # Aggregate on company
                if line.split(",")[4] == customer[line.split(",")[0]][1]:
                    aggregated[line.split(",")[0]][1] += 1
                else:
                    pass

                # Aggregate on brand
                if line.split(",")[5] == customer[line.split(",")[0]][2]:
                    aggregated[line.split(",")[0]][2] += 1
                else:
                    pass

                # Aggregate number of purchases not relative to offer
                if  line.split(",")[3] != customer[line.split(",")[0]][0] and line.split(",")[4] != customer[line.split(",")[0]][1] and line.split(",")[5] != customer[line.split(",")[0]][2]:
                    aggregated[line.split(",")[0]][3] += 1
                else:
                    pass

                # Aggregate if company, category and brand all align on the offer information
                if  line.split(",")[3] == customer[line.split(",")[0]][0] and line.split(",")[4] == customer[line.split(",")[0]][1] and line.split(",")[5] == customer[line.split(",")[0]][2]:
                    aggregated[line.split(",")[0]][4] += 1
                else:
                    pass

                # Number of total purchases
                aggregated[line.split(",")[0]][5] += 1
                aggregated[line.split(",")[0]][6] = int(line.split(",")[0])

            else:
                pass
        if e%100000 == 0:
            print "Runnig: " + str(e)

    with open(loc_aggregated, 'wb') as out_file:
        out_file.write('category_aggregated, company_aggregated, brand_aggregated, non_offer_aggregated, offer_aggregated, total_purchases, id' + '\n')
        for key in aggregated:
            info = aggregated[key]
            #out_file.write(str(info[0]) + "," + str(info[1]) + "," + str(info[2]) + "," + str(info[3]) + "," + str(info[4]) + "," + str(info[5]) + "," + str(info[6]) + "," + str(key) + "\n")
            out_file.write(str(info) + "\n")

aggregate_by_customer(loc_joined, loc_transactions, loc_aggregated)

#!/bin/python

list_a = [0,1322,3718,4294,5072,6926,7668,15889,17286,17311,26189,26456,64486,102504]
list_b = [875,3718,5072,6732,6926,7668,13474,13791,15889,28840,64486,102504]

for item in list_b:
    if item not in  list_a:
        list_a.append(item)

print list_a

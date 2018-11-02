import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori

med_dataset = pd.read_csv('med_dataset.csv')
med_list = med_dataset.astype(str).values.tolist()

print(med_list[0][0])
print(type(med_list[0][0]))

# remove nan values
# for i in range(len(med_list)):
#     med_list[i] = [x for x in med_list[i] if x != 'nan']

print('length of list is',len(med_list))
# print(med_list)

# create test set for first 100 records
test_list = med_list[:500]
# print(med_list)

# run apriori algo on med list to find association rules
association_rules = apriori(med_list, min_support=0.00002, min_confidence=0.7, min_lift=3, min_length=2)
association_results = list(association_rules)

print(len(association_results))
print(association_results[0])

for item in association_results:

    # first index of the inner list
    # Contains base item and add item
    pair = item[0]
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")

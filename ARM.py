import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori

# create main dataset
main_dataset = pd.read_csv("dataset.csv")
main_dataset.drop(main_dataset.columns[0], axis=1, inplace=True)

# different datasets based on race
asian_data = main_dataset.loc[main_dataset['race'] == 'Asian']
white_data = main_dataset.loc[main_dataset['race'] == 'Caucasian']
minorities = ['AfrianAmerican','Hispanic','Other']
minor_data = main_dataset.loc[main_dataset['race'].isin(minorities)]

# percentage of ppl who have diabetes medicine prescribed
prescribed_med = main_dataset['diabetesMed'].value_counts(normalize=True)
print(prescribed_med)

# dataset of ppl who were not readmitted
no_readmin = main_dataset.loc[main_dataset['readmitted'] == 'NO']

# percentage of no_readmin who took drugs
no_readmin_prescribed = no_readmin['diabetesMed'].value_counts(normalize=True)

# cleaned dataset of no_readmin
med_cols = ['metformin','repaglinide','nateglinide','chlorpropamide',\
            'glimepiride','acetohexamide','glipizide','glyburide','tolbutamide',\
           'pioglitazone','rosiglitazone','acarbose','miglitol','troglitazone',\
           'tolazamide','examide','citoglipton','insulin','glyburide.metformin',\
           'glipizide.metformin','glimepiride.pioglitazone','metformin.rosiglitazone',\
           'metformin.pioglitazone']
no_readmin_cleaned = no_readmin[med_cols]

# clean no_readmin dataset
for col in no_readmin_cleaned:
    print(col)
    for index, row in no_readmin_cleaned.iterrows():
        if row[col] == 'Steady' or row[col] == 'Up' or row[col] == 'Down':
            row[col] = col
    print('iterated through whole col')

print('new dataset created')

# replace all no values with nan
no_readmin_cleaned = no_readmin_cleaned.replace('No',np.nan)
print('values are replaced')

no_readmin_cleaned.to_csv('med_dataset', encoding='utf-8', index=False)
print('csv created')

# # create records list for ARM algo
# records = []
# for i in range(0, 52338):
#     print(i)
#     if i%1000==0:
#         print(i,'rows completed')
#     records.append([str(no_readmin_cleaned.values[i,j]) for j in range(0, 23)])

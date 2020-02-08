# make_dataset.py
#
# Anders Poirel
# 7-02-2020
#
# Script for downloading and formatting properly the data for Data Science Slugs''
# Datathon One. Saves training and validation sets to a csv file

import os
import pandas as pd
import itertools
import requests
from sklearn.model_slection import train_test_split


def make_dataset():
    RAW_DATA_PATH = '../../data/raw'
    PROCESSED_DATA_PATH =  '../../data/processed'
    data_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00437/Residential-Building-Data-Set.xlsx'

    r = requests.get(train_features_url)
    with open(os.path.join(RAW_DATA_PATH, "house_prices.xlsx"), 'wb') as f:
        f.write(r.content)
    
    dataset = pd.read_excel('../../data/house_prices.xlsx')

    data_p = dataset.drop('Unnamed: 108', axis = 1)

    calendar_vars = list(dataset.iloc[0, 0:4])
    nontime_vars = ['V-' + str(i) for i in range(1,9)]
    time_vars = ['V-' + str(i) for i in range(11, 30)] 

    time_lags = ['T1', 'T2', 'T3', 'T4', 'T5']
     = [t + ' ' + v for (t,v) in itertools.product(time_lags, time_vars)]

    col_names = calendar_vars + nontime_vars + imp_time_vars + ['House price']
    data_p.drop(labels = 0, inplace = True, axis = 0)
    data_p.columns = col_names

    features = data_p.drop(labels = 'House price', axis = 1)
    labels = data_p['House price']

    train_features, test_features, train_labels, test_labels = train_test_split(
        features, labels, test_size = 0.3
    )

    train_features.to_csv('../../data/processed/train_features.csv', index = False)
    test_features.to_csv('../../data/processed/train_features.csv', index = False)
    train_labels.to_csv('../../data/processed/train_features.csv', index = False)
    test_labels.to_csv('../../data/processed/train_features.csv', index = False)

    return

if __name__ == "__main__":
    make_dataset()


    

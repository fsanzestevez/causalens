# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 17:50:18 2020

@author: Fran
"""

import os
import pandas as pd

import warnings 
from createDB import CreateDB
from modelling import Modelling



if __name__ == "__main__":
    warnings.simplefilter(action='ignore', category=Warning)
    if os.path.isfile('data/full_DB.pkl'):
        fullDB = pd.read_pickle('data/full_DB.pkl')
    else:
        create = CreateDB()
        fullDB = create.fullDB.copy()
        
    test_size = 0.15
    n = len(fullDB)
    split_index = int(n*(1-test_size))
    train = fullDB.iloc[:split_index, :]
    test = fullDB.iloc[split_index:, :]

    if os.path.isfile('data/EN_model.pickle'):
        clf_en = pd.read_pickle('data/EN_model.pickle')
        clf_gbm = pd.read_pickle('data/GBM_model.pickle')
        clf_rf = pd.read_pickle('data/RF_model.pickle')
    else:
        models = Modelling(train, test)
        clf_en = models.clf_en
        clf_gbm = models.clf_gbm
        clf_rf = models.clf_rf
        
    
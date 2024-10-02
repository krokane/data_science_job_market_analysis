#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 17:05:09 2024

@author: kevin
"""
import pandas as pd

apartments = pd.read_csv('./apartments.csv')

location_id = {}
loc_ids = []

sorted_apt = pd.Series(pd.unique(apartments['Location'])).sort_values()
sorted_apt.index = range(10)

for i in range(len(sorted_apt)):
    location_id[sorted_apt[i]] = i
for i in range(len(apartments)):
    loc_ids.append(location_id[apartments['Location'][i]])
apartments['location_id'] = loc_ids

apartments.to_csv('./apartments.csv')

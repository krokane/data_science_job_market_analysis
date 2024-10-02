#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 18:32:57 2024

@author: kevin
"""

import pandas as pd

jobs = pd.read_csv('./jobs.csv')
jobs = jobs.drop('Unnamed: 0',axis=1)

#cleaning locations
for i in range(len(jobs)):
    usa = jobs['locations'][i].split('-').index('USA')
    new = jobs['locations'][i].split('-')[:usa]
    jobs['locations'].at[i] = ' '.join(new)

#cleaning employees data
for i in range(len(jobs)):
    if pd.isna(jobs['employees'][i]):
        continue
    else:
        jobs['employees'][i] = int(jobs['employees'][i].split()[0].replace(',',''))
        
#cleaning salary column
for i in range(len(jobs)):
    if pd.isna(jobs['salaries'][i]) == True:
        continue
    else:
        split = (jobs['salaries'][i].split()[0].replace('$','').replace('K','000').split('-'))
        if len(split) == 1:
            jobs['salaries'][i] = float(split[0])
        else:
            jobs['salaries'][i] = float(split[1])
            
#cleaning xp column
for i in range(len(jobs)):
    if pd.isna(jobs['xp_requirements'][i]) == True:
        continue
    else:
        if jobs['xp_requirements'][i] == '3-5 Years of Experience':
            jobs['xp_requirements'][i] = 'Mid'
        else:
            jobs['xp_requirements'][i] = 'Low'
          
location_id = {}
loc_ids = []

sorted_jobs = pd.Series(pd.unique(jobs['locations'])).sort_values()
sorted_jobs.index = range(10)

for i in range(len(sorted_jobs)):
    location_id[sorted_jobs[i]] = i
for i in range(len(jobs)):
    loc_ids.append(location_id[jobs['locations'][i]])
jobs['location_id'] = loc_ids

jobs.to_csv('./jobs.csv')

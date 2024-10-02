#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 09:19:21 2024

@author: kevin
"""
import argparse
import pandas as pd
import requests

from bs4 import BeautifulSoup

url_locations = ['New-York-NY-USA-New-York-County&longitude=-74.00712&latitude=40.71453',
                 'Los-Angeles-CA-USA-Los-Angeles-County&longitude=-118.24368&latitude=34.05223',
                 'San-Francisco-CA-USA-San-Francisco-County&longitude=-122.41942&latitude=37.77493',
                 'Seattle-WA-USA-King-County&longitude=-122.33207&latitude=47.60621',
                 'Boston-MA-USA&longitude=-71.05674&latitude=42.35866',
                 'Austin-TX-USA&longitude=-97.74299&latitude=30.26759',
                 'Chicago-IL-USA&longitude=-87.63245&latitude=41.88425',
                 'Denver-CO-USA-City-and-County-of-Denver&longitude=-104.99202&latitude=39.74001',
                 'Washington-DC-USA-District-of-Columbia&longitude=-77.03196&latitude=38.89037',
                 'San-Diego-CA-USA&longitude=-117.16171&latitude=32.71568']

companies = []
titles = []
locations = []
employees = []
salaries = []
xp_requirements = []

for i in range(len(url_locations)):
    for j in range(1,3):
        url = 'https://builtin.com/jobs/remote/hybrid/office/entry-level/mid-level?search=%22Data%20Scientist%22&location=' + url_locations[i] + '&searcharea=25&page=' + str(j)
        site = requests.get(url)
        text = site.text
        soup = BeautifulSoup(text,'html.parser')
        
        jobs_text = soup.find_all('div', class_ = 'position-relative job-bounded-responsive border rounded-3 border-gray-02 position-relative bg-white p-md')
        
        fte_usd_xp_list = []
        
        for k in range(len(jobs_text)):
            company = jobs_text[k].find('div', class_ = 'font-barlow fs-md fs-xl-xl d-inline-block m-0 hover-underline').text
            job_title = jobs_text[k].find('a', class_ = 'card-alias-after-overlay hover-underline link-visited-color text-break').text
            location = url_locations[i].split('&')[0]
            fte_usd_xp = jobs_text[k].find('div', class_ = 'd-none d-xl-block fill-even').find_all('div', class_ = 'd-flex align-items-start gap-sm')
            companies.append(company)
            titles.append(job_title)
            locations.append(location)
            fte_usd_xp_list.append(fte_usd_xp)
        
        for m in range(len(fte_usd_xp_list)):
            if len(fte_usd_xp_list[m]) < 3:
                employees.append(None)
                salaries.append(None)
                xp_requirements.append(None)
            else:
                employees.append(fte_usd_xp_list[m][0].span.text)
                salaries.append(fte_usd_xp_list[m][1].span.text)
                xp_requirements.append(fte_usd_xp_list[m][2].span.text)

df = pd.DataFrame([titles, companies, locations, employees, salaries, xp_requirements]).T
df.columns = ['titles', 'companies', 'locations', 'employees', 'salaries', 'xp_requirements']

if __name__ == '__main__': 
    parser = argparse.ArgumentParser()

    parser.add_argument('--scrape', type=int, nargs='+')
    parser.add_argument('--save', nargs='+')

    args = parser.parse_args()
    
    if (args.scrape != None and len(args.scrape) > 0):
        n = args.scrape[0]
        print(df.head(n))
    
    if (args.save != None and len(args.save) > 0):
        path = args.save[0]
        df.to_csv(str(path))

    else: print(df)
        
        

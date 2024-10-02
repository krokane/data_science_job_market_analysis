#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 09:16:17 2024

@author: kevin
"""
import pandas as pd
from amadeus import Client, ResponseError

'''
key = ***********************
secret = ****************

amadeus = Client(
    client_id=key,
    client_secret=secret)

try:
    airport_input = input('Please input an IATA Airport Code. \n')
    output = amadeus.airport.direct_destinations.get(departureAirportCode=airport_input, arrivalCountryCode ='US')
    df = pd.DataFrame(output.data)
except ResponseError as error:
    raise error
'''   
print(df.columns)

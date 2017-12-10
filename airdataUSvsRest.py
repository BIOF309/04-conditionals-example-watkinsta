import numpy as np
import pandas as pd
airdata = pd.read_excel('airdata.xlsx', index_col = 0)
#Very similar concept to 03 assignment, which contains both a loop
#and conditional. This also contains both, but with a different comparison:
#average US particulate vs. average rest of world

US_count = 0
US_partic = 0
rest_count = 0
rest_partic = 0
for i in range(len(airdata) - 1):
    if airdata['iso3'].iloc[i] == 'USA':
        US_count = US_count + 1
        US_partic = US_partic + airdata['PM10 Annual mean, ug/m3'].iloc[i]
    else:
        rest_count = rest_count + 1
        rest_partic = rest_partic + airdata['PM10 Annual mean, ug/m3'].iloc[i]
print('The average PM10 recorded in the US is %d ug/ml.' %(US_partic/US_count))
print('The average PM10 recorded in the rest of the world is %d ug/ml.' %(rest_partic/rest_count))

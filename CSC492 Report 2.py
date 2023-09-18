#!/usr/bin/env python
# coding: utf-8

# In[88]:


import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np


#Load Data
fires_df = pd.read_csv(r"C:\Users\jpper\Documents\CSC492\forestfires.csv", encoding='utf8')
fires_df.info()
#create numerical distributions
fires_df.describe()



# In[89]:


#apply logarithmic transformation to area based on comments in data explanation
fires_df['area_log_actual'] = np.log2(fires_df['area_log'])

fires_df.hist(bins=50, figsize=(20,15))
plt.show()

#apply logarithmic transformation to area based on comments in data explanation


# In[90]:


#Create pearson distributuons between variables
area = fires_df['area']
area_log = fires_df['area_log_actual']
ffmc = fires_df['FFMC']
dmc = fires_df['DMC']
dc = fires_df['DC']
isi = fires_df['ISI']
temp = fires_df['temp']
RH = fires_df['RH']
wind = fires_df['wind']
rain = fires_df['rain']


print("FFMC Pearson")
print(area.corr(ffmc))
print("FFMC Pearson, normalized area")
print(area_log.corr(ffmc))


plt.scatter(ffmc, area)
#create line of best fit to show correlation
a, b = np.polyfit(ffmc, area, 1)
plt.xlabel("ffmc")
plt.xlim(0, 150)
plt.ylim(0, 1200)
plt.plot(area, a*ffmc+b, color='purple')      
plt.show()
plt.scatter(ffmc, area_log)
#create line of best fit to show correlation
a, b = np.polyfit(ffmc, area_log, 1)
plt.xlabel("ffmc")
plt.xlim(0, 150)
plt.ylim(0, 50)
plt.plot(area_log, a*ffmc+b, color='purple')      
plt.show()


# In[91]:


print("DMC Pearson")
print(area.corr(dmc))

print("DMC Pearson, normalized area")
print(area_log.corr(dmc))

plt.scatter(dmc, area)
#create line of best fit to show correlation
a, b = np.polyfit(dmc, area, 1)
plt.xlabel("dmc")
plt.xlim(0, 400)
plt.ylim(0, 1200)
plt.plot(area, a*dmc+b, color='purple')      
plt.show()
plt.scatter(dmc, area_log)
#create line of best fit to show correlation
a, b = np.polyfit(dmc, area_log, 1)
plt.xlabel("dmc")
plt.xlim(0, 400)
plt.ylim(0, 100)
plt.plot(area_log, a*dmc+b, color='purple')      
plt.show()


# In[92]:


print("DC Pearson")
print(area.corr(dc))
print("DC Pearson, normalized area")
print(area_log.corr(dc))

plt.scatter(dc, area)
#create line of best fit to show correlation
a, b = np.polyfit(dc, area, 1)
plt.xlabel("dc")
plt.xlim(0, 1000)
plt.ylim(0, 1200)
plt.plot(area, a*dc+b, color='purple')      
plt.show()
plt.scatter(dc, area_log)
#create line of best fit to show correlation
a, b = np.polyfit(dc, area_log, 1)
plt.xlabel("dc")
plt.xlim(0, 1000)
plt.ylim(0, 100)
plt.plot(area_log, a*dc+b, color='purple')      
plt.show()


# In[93]:


print("ISI Pearson")
print(area.corr(isi))

print("ISI Pearson")
print(area_log.corr(isi))

plt.scatter(isi, area)
#create line of best fit to show correlation
a, b = np.polyfit(isi, area, 1)
plt.xlabel("isi")
plt.xlim(0, 60)
plt.ylim(0, 1200)
plt.plot(area, a*isi+b, color='purple')      
plt.show()

plt.scatter(isi, area_log)
#create line of best fit to show correlation
a, b = np.polyfit(isi, area_log, 1)
plt.xlabel("isi")
plt.xlim(0, 60)
plt.ylim(0, 50)
plt.plot(area_log, a*isi+b, color='purple')      
plt.show()


# In[94]:


print("TEMP Pearson")
print(area.corr(temp))

print("TEMP Pearson, normalized area")
print(area_log.corr(temp))

plt.scatter(temp, area)
#create line of best fit to show correlation
a, b = np.polyfit(temp, area, 1)
plt.xlabel("temp")
plt.xlim(0, 50)
plt.ylim(0, 1200)
plt.plot(area, a*temp+b, color='purple')      
plt.show()

plt.scatter(temp, area_log)
#create line of best fit to show correlation
a, b = np.polyfit(temp, area_log, 1)
plt.xlabel("temp")
plt.xlim(0, 50)
plt.ylim(0, 100)
plt.plot(area_log, a*temp+b, color='purple')      
plt.show()


# In[95]:


print("RH Pearson")
print(area.corr(RH))
print("RH Pearson, normalized area")
print(area_log.corr(RH))

plt.scatter(RH, area)
#create line of best fit to show correlation
a, b = np.polyfit(RH, area, 1)
plt.xlabel("RH")
plt.xlim(0, 100)
plt.ylim(0, 1200)
plt.plot(area, a*RH+b, color='purple')      
plt.show()

plt.scatter(RH, area_log)
#create line of best fit to show correlation
a, b = np.polyfit(RH, area_log, 1)
plt.xlabel("RH")
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.plot(area_log, a*RH+b, color='purple')      
plt.show()


# In[96]:


print("WIND Pearson")
print(area.corr(wind))
print("WIND Pearson, normalized area")
print(area_log.corr(wind))

plt.scatter(wind, area)
#create line of best fit to show correlation
a, b = np.polyfit(wind, area, 1)
plt.xlabel("wind")
plt.xlim(0, 10)
plt.ylim(0, 1200)
plt.plot(area, a*wind+b, color='purple')      
plt.show()

plt.scatter(wind, area_log)
#create line of best fit to show correlation
a, b = np.polyfit(wind, area_log, 1)
plt.xlabel("wind")
plt.xlim(0, 10)
plt.ylim(0, 100)
plt.plot(area_log, a*wind+b, color='purple')      
plt.show()


# In[97]:


print("RAIN Pearson")
print(area.corr(rain))

print("RAIN Pearson, normalized area")
print(area_log.corr(rain))

plt.scatter(rain, area)
#create line of best fit to show correlation
a, b = np.polyfit(rain, area, 1)
plt.xlabel("rain")
plt.xlim(0, 5)
plt.ylim(0, 1200)
plt.plot(area, a*rain+b, color='purple')      
plt.show()

plt.scatter(rain, area_log)
#create line of best fit to show correlation
a, b = np.polyfit(rain, area_log, 1)
plt.xlabel("rain")
plt.xlim(0, 5)
plt.ylim(0, 100)
plt.plot(area_log, a*rain+b, color='purple')      
plt.show()


# In[ ]:





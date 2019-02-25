import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dfbcg = pd.read_csv('BCG.csv', na_values="n.a")
dfbcg = dfbcg.interpolate()
dfdpt = pd.read_csv('DPT.csv',na_values="n.a")
dfdpt = dfdpt.interpolate()
dfcampak = pd.read_csv('Campak.csv',na_values="n.a")
dfcampak = dfcampak.interpolate()
dfpolio = pd.read_csv('Polio.csv',na_values="n.a")
dfpolio = dfpolio.interpolate()

plt.figure('Figure 1: Persentase balita terimunisasi 1995-2017',figsize=(12,12))
plt.subplot(321)
plt.bar(dfbcg.ix[:,0],dfbcg.ix[:,1], color='r')
plt.xticks(np.arange(1995,2017), rotation=90)
plt.title('BCG')
plt.subplot(322)
plt.bar(dfcampak.ix[:,0],dfcampak.ix[:,1], color='g')
plt.xticks(np.arange(1995,2017), rotation=90)
plt.title('Campak')
plt.subplot(325)
plt.bar(dfdpt.ix[:,0],dfdpt.ix[:,1], color='y')
plt.xticks(np.arange(1995,2017), rotation=90)
plt.title('DPT')
plt.subplot(326)
plt.bar(dfpolio.ix[:,0],dfpolio.ix[:,1], color='b')
plt.xticks(np.arange(1995,2017), rotation=90)
plt.title('Polio')
# plt.show()
'''
% Balita tidak terimunisasi
'''
dfbcg.ix[:,1] = 100-dfbcg.ix[:,1]
dfcampak.ix[:,1] = 100-dfcampak.ix[:,1]
dfdpt.ix[:,1] = 100-dfdpt.ix[:,1]
dfpolio.ix[:,1] = 100-dfpolio.ix[:,1]

plt.figure('Figure 2: Persentase balita tak terimunisasi 1995-2017',figsize=(12,12))
plt.subplot(321)
plt.bar(dfbcg.ix[:,0],dfbcg.ix[:,1], color='r')
plt.xticks(np.arange(1995,2017), rotation=90)
plt.title('BCG')
plt.subplot(322)
plt.bar(dfcampak.ix[:,0],dfcampak.ix[:,1], color='g')
plt.xticks(np.arange(1995,2017), rotation=90)
plt.title('Campak')
plt.subplot(325)
plt.bar(dfdpt.ix[:,0],dfdpt.ix[:,1], color='y')
plt.xticks(np.arange(1995,2017), rotation=90)
plt.title('DPT')
plt.subplot(326)
plt.bar(dfpolio.ix[:,0],dfpolio.ix[:,1], color='b')
plt.xticks(np.arange(1995,2017), rotation=90)
plt.title('Polio')
plt.show()



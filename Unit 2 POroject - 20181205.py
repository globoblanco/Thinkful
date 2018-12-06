import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

df = pd.read_csv('Food Imports F.csv', 
                 index_col='Food Group')

plt.rcParams['figure.figsize'] = (10, 6)
plt.plot(df.loc['Total U.S. food imports'])
plt.plot(df.loc['Total animal foods'])
plt.plot(df.loc['Total plant foods'])
plt.plot(df.loc['Total beverages'])
plt.ylabel('$ (Millions)')
plt.xlabel('Years')
plt.title('U.S Food Imports\nIn Millions')
plt.legend()

plt.show()
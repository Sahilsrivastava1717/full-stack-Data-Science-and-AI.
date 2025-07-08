import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv(r"C:\Users\sahil\Downloads\Salary_Data.csv")

x = df.iloc[:,:-1]
y = df.iloc[:, -1]

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.20, random_state = 0 )

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)

y_pred = regressor.predict(x_test)


comparison = pd.DataFrame({'actual': y_test, 'predicted': y_pred})
print(comparison)

plt.scatter(x_test,y_test)
plt.xlabel('yrs of exp')
plt.ylabel('salary')
plt.title('company')
plt.plot(x_train,regressor.predict(x_train),color = 'blue')
plt.show()



m_slope = regressor.coef_
print(m_slope)

c_intercept = regressor.intercept_
print(c_intercept)

#pred:1
y_12 = (m_slope*12) + c_intercept
print(y_12)

#pred:2
y_20 = (m_slope*20) + c_intercept
print(y_20)

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv(r"C:\Users\sahil\Downloads\Salary_Data.csv")


df.mean()

df['Salary'].mean()

df.median()

df['Salary'].median()

df['Salary'].mode()

df.var()

df['Salary'].var()

df.std()

df['Salary'].std()

#coeff of variation 

from scipy.stats import variation 

variation(df)

variation(df['Salary'])

df.corr()

df['Salary'].corr(df['YearsExperience'])

#skew
df.skew()

df['Salary'].skew()

#standard error 
df.sem()

df['Salary'].sem()


import scipy.stats as stats 
df.apply(stats.zscore)
stats.zscore(df['Salary'])



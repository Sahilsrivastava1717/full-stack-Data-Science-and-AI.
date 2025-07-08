import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv(r"C:\Users\sahil\Downloads\canada_per_capita_income.csv")

x = df.iloc[:,:-1]
y = df.iloc[:,-1]

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.20,random_state = 0)

from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(x_train,y_train )

y_predict = reg.predict(x_test)

comparison = pd.DataFrame({'actual': y_test, 'predicted': y_predict})
print(comparison)

plt.scatter(x_test, y_test,color = "red")
plt.xlabel("year")
plt.ylabel("per capita income")
plt.title("canada_per_capita_income")
plt.plot(x_train,reg.predict(x_train),color = 'blue')
plt.show()


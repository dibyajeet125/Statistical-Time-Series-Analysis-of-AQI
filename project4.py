import pandas as pd
from sklearn.metrics import mean_squared_error
from math import sqrt
import matplotlib.pyplot as plt

df = pd.read_excel("linearReg.xlsx")
print(df)

df.drop(df.iloc[:, :1], inplace=True, axis=1)
print(df)

df.info()

year_mean=df[['Year', 'pm25']].groupby('Year').mean().sort_values(by='Year')
print('Year-wise Mean: ', '\n', year_mean)

plt.style.use('seaborn')
year_mean.plot(color='Blue')

#for removing guide
plt.legend('')

#title and labels
plt.title('Distribution of AQI over 2014-2022', fontsize=20)
plt.xlabel('Year', fontsize=15)
plt.ylabel('PM 2.5', fontsize=15)

plt.show()

X = year_mean.values
X = X.astype('float32')

#fixing length
train_size = int(len(X) * 0.2)
#splitting the data into 2:train & test
train, test = X[0:train_size], X[train_size:]
history = [x for x in train]
predictions = list()
for i in range(len(test)):
    #negative indexes for selecting in reverse order
    #[-1] = first item from last
    #here suppose in array [243.222, 130.526]
    #last element is 130.526 & goes on...
    yhat = history[-1]
    predictions.append(yhat)
    obs = test[i]
    history.append(obs)
    print('Predictions=%.3f, Actual=%.3f' % (yhat, obs))

#calculate mean squared error
#(predicted val - actual val)^2
#then add all squared differences
#then divide the value by the total number of items in the list
#((predicted val - actual val)^2)/n
mse = mean_squared_error(test, predictions)
print('MSE: %.3f' % mse)

#calculate root mean squared error
#sqrt(((predicted val - actual val)^2)/n)
rmse = sqrt(mean_squared_error(test, predictions))
print('RMSE: %.3f' % rmse)

plt.style.use('seaborn')
#plt.scatter(test, predictions)
plt.plot(test, color='green')
plt.plot(predictions, color='red')

#modify x-axis ticks name
plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8], ['2014','2015','2016','2017','2018','2019','2020','2021','2022'])

#guide
plt.legend(['Actual', 'Predictions'])

#title and labels
plt.title('Actual & Predicted Distributions of AQI over 2014-2022', fontsize=20)
plt.xlabel('Year', fontsize=15)
plt.ylabel('PM 2.5', fontsize=15)

plt.show()

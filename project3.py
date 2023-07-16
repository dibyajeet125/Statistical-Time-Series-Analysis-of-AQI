import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from math import sqrt

#past 94 months data
#read a CSV File
df = pd.read_csv("kolkata-us consulate-air-quality.csv")
print(df)

#name or rename columns
df.columns = ['Year/Month/Date', 'pm25']

#split the particular col. "Year/Month/Date" into three
df[['Year', 'Month', 'Date']]=df['Year/Month/Date'].str.split('/', expand=True)
print(df)

#group year-wise avg,var,std of pm2.5
year_mean=df[['Year', 'pm25']].groupby('Year').mean().sort_values(by='Year')
print('Year-wise Mean: ', '\n', year_mean)

year_variance=df[['Year', 'pm25']].groupby('Year').var().sort_values(by='Year')
print('Year-wise Variance: ', '\n', year_variance)

year_stdDev=df[['Year', 'pm25']].groupby('Year').std().sort_values(by='Year')
print('Year-wise Standard Deviance: ', '\n', year_stdDev)

#"to_excel"~have to install openpyxl module
#copy Year & pm2.5 table to excel
df[['Year','pm25']].to_excel('linearReg.xlsx')

def function():
    # read a excel File
    f = pd.read_excel("linearReg.xlsx")
    print(f)

    # remove column (here, unnamed)
    f.drop(f.iloc[:, :1], inplace=True, axis=1)
    print(f)

    # name or rename columns
    f.columns = ['x', 'y']
    print(f)

    # define x & y
    x = f.iloc[:, 0]
    y = f.iloc[:, 1]

    # before plotting the regression line
    plt.scatter(x, y)

    # put the labels
    plt.xlabel('x')
    plt.ylabel('y')

    # show plot
    plt.show()

    # number of columns
    n = np.size(x)

    # mean of x and y
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    # calculate cross-deviation and deviation about x
    S_xy = np.sum(x * y) - n * x_mean * y_mean
    S_xx = np.sum(x * x) - n * x_mean * x_mean

    # calculate linear regression coefficients
    slope_b = S_xy / S_xx
    intercept_a = y_mean - slope_b * x_mean

    # plot the points at scatter plot
    plt.scatter(x, y)

    # predicted y
    y_pred = intercept_a + slope_b * x

    # plot the regression line
    plt.plot(x, y_pred, color="black")

    # put the labels
    plt.xlabel('x')
    plt.ylabel('y')

    # show plot
    plt.show()

    # estimate coefficients
    print("|---|---------------------|")
    print("| a | {}    |".format(intercept_a))
    print("|---|---------------------|")
    print("| b | {}  |".format(slope_b))
    print("|---|---------------------|")
    print()
    # y = a + bx
    print("Equation of linear regression is: \n|-------------------------------------------------| \
        \n| y_pred = {} + {}x | \
        \n|-------------------------------------------------|".format(intercept_a, slope_b))

    # defining the regression line
    plot_regression_line = 0

function()
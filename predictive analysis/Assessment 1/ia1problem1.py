# -*- coding: utf-8 -*-
"""IA1Problem1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19uZCRtoDCG6XmmuBifVc3orMQz36HeCW
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df=pd.read_csv(r'/content/expenses.csv')

df.head()

df.shape

df.info()

df.size

df.dtypes

#finding missing values
df.isna().sum()

df['bmi']

#changing the missing values with the mean of the bmi
df=df.fillna(value=df['bmi'].mean())

df.isna().sum()

#outliers

numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
for column in numerical_columns:
  plt.figure(figsize=(10,6))
  sns.boxplot(x=df[column])
  plt.show()

#Encoding Categorical Data
df.head()

df=pd.get_dummies(df,columns=['sex','smoker','region'])

df.head(10)

df.dtypes

#duplicates
df.duplicated().sum()

df.dtypes

duplicated_rows = df[df.duplicated(keep=False)]
print(duplicated_rows)

df.drop_duplicates(inplace=True)

df.duplicated().sum()

#correlation for numerical variables
numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
correlation_matrix = df[numerical_columns].corr()
print("Correlation matrix:\n", correlation_matrix)
# Plot the correlation matrix as a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True)
plt.title('Heatmap')
plt.show()

#scatter plot
numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
for i in range(len(numerical_columns)):
 for j in range(i + 1, len(numerical_columns)):
  plt.figure(figsize=(10, 6))
  sns.scatterplot(data=df, x=numerical_columns[i], y=numerical_columns[j])
  plt.title(f'Scatter Plot between {numerical_columns[i]} and {numerical_columns[j]}')
  plt.show()

df.head()

#data labelling
X = df.drop(columns = ["charges"])
y = df["charges"]
#data splitting
X_train,X_test,y_train,y_test= train_test_split(X, y , test_size = 0.3)

X_train.shape

y_train.shape

scaler= MinMaxScaler()
X_train=pd.DataFrame(scaler.fit_transform(X_train[list(X.columns)]), columns=X.columns)
X_test=pd.DataFrame(scaler.transform(X_test[list(X.columns)]),columns=X.columns)

#model training
model= LinearRegression()
model.fit(X_train, y_train)
y_pred=model.predict(X_test)

from sklearn.metrics import mean_squared_error, mean_absolute_error

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
rmse = mean_squared_error(y_test, y_pred,squared=False)
print("Root Mean Squared Error:", rmse)

from sklearn.metrics import r2_score

# Coefficients and intercept
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
r2_s = r2_score(y_test, y_pred)
print("R2 Score:", r2_s)
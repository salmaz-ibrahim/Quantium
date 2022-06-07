# Task 1

# The output file should contain three fields:
# Sales
# Date
# Region


import csv
import pandas as pd
import numpy as np

# for the first  CSV file
df_0 = pd.read_csv('C:/Users/MaNo/Documents/GitHub/Quantium/quantium-starter-repo-main/data/daily_sales_data_0.csv')
df_0 = df_0.iloc[:, [0, 1, 2, 4]]
df_0 = df_0.loc[df_0["product"] == "pink morsel"]

df_0["price"] = df_0["price"].str.replace('\$', '', regex=True).astype(float)
df_0["quantity"] = df_0["quantity"].astype(float)
df_0["sales"] = df_0["price"] * df_0["quantity"]

df_0 = df_0.drop(columns=['price', 'quantity'], axis=1)

# for the second  CSV file
df_1 = pd.read_csv('C:/Users/MaNo/Documents/GitHub/Quantium/quantium-starter-repo-main/data/daily_sales_data_1.csv')
df_1 = df_1.iloc[:, [0, 1, 2, 4]]
df_1 = df_1.loc[df_1["product"] == "pink morsel"]

df_1["price"] = df_1["price"].str.replace('\$', '', regex=True).astype(float)
df_1["quantity"] = df_1["quantity"].astype(float)
df_1["sales"] = df_1["price"] * df_1["quantity"]

df_1 = df_1.drop(columns=['price', 'quantity'], axis=1)

# for the third  CSV file
df_2 = pd.read_csv('C:/Users/MaNo/Documents/GitHub/Quantium/quantium-starter-repo-main/data/daily_sales_data_0.csv')
df_2 = df_2.iloc[:, [0, 1, 2, 4]]
df_2 = df_2.loc[df_2["product"] == "pink morsel"]

df_2["price"] = df_2["price"].str.replace('\$', '', regex=True).astype(float)
df_2["quantity"] = df_2["quantity"].astype(float)
df_2["sales"] = df_2["price"] * df_2["quantity"]

df_2 = df_2.drop(columns=['price', 'quantity'], axis=1)

print("The first Database \n", df_0.head(5), "\n \n The second Database \n", df_1.head(5), "\n \n The third Database \n"
      , df_2.head(5))

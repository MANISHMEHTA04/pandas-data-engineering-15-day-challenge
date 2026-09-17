import pandas as pd
import os

# print(os.getcwd())

df = pd.read_csv("day01_ecommerce_order_explorer\orders.csv")
print(df)


print(df.head(5))

print(df.shape)

print(df.dtypes) 

print(df[["order_id","customer_id","amount"]])

print(df.columns)

print(df[df["amount"] > 10000]) 

print(df[df["status"] == "CANCELLED"])

print(df[df["category"] == "Electronics"])
import pandas as pd 

df = pd.read_csv("bank_transactions.csv")
print(df.head())
print(df.shape)
print(df.dtypes)
df.info()

#Find all records where customer_id is missing.
print(df[df["customer_id"].isna()])

#find the actual records where amount is missing.
print(df[df["amount"].isna()])

#Find the actual duplicate transaction records based on transaction_id.
print(df[df.duplicated(subset=["transaction_id"])])

#Remove duplicate transactions based on transaction_id, keeping the first occurrence.
df = df.drop_duplicates(subset = ["transaction_id"],
                   keep = "first")

#Transactions with a missing customer_id are invalid.
df = df.dropna(subset = ["customer_id"])

#A missing amount should be treated as 0.
df["amount"] = df["amount"].fillna(0)

#convert the amount column explicitly to float.
df["amount"] = df["amount"].astype(float)

#Clean transaction_type so values such as
df["transaction_type"] = df["transaction_type"].str.strip().str.upper()

#Do the same standardization for city.
df["city"] = df["city"].str.strip().str.upper()

#Rename the column
df = df.rename(
    columns = {
                "transaction_type" : "txn_type"
            }
)

print(df)
print(df.shape)
print(df.dtypes)
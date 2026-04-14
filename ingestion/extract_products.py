import pandas as pd
import datetime


def extract_products():

 df=pd.read_csv("data\olist_products_dataset.csv.zip")
 print(df.head())
 print(df.columns)
 return df

print(extract_products())

import pandas as pd
import datetime


def extract_order():

 df=pd.read_csv("data\olist_orders_dataset.csv.zip")
 return df

print(extract_order())
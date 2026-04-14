from extract_orders import extract_order
from extract_products import extract_products
from load_to_raw import load_to_raw

#df = extract_order()
#load_to_raw(df, "orders")


df1 = extract_products()
load_to_raw(df1, "products")
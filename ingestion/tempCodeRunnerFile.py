from extract_orders import extract_order
from load_to_raw import load_to_raw

df = extract_order()
load_to_raw(df, "orders")
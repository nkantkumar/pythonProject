import pandas as pd

sales = pd.read_csv("sales.csv")
#print(sales.loc[2:8, ["product_code","product_group"]])
#print(sales.head())
#print(sales.shape)

#print(sales.size)

p= list(sales["product_group"].value_counts().sort_values().index)
#print(p)
#print(len(sales))

#print(sales.dtypes)

sales_filtered = sales[sales["product_group"] == "PG2"]
#print(sales_filtered)

sales = pd.read_csv("sales.csv", usecols=["product_code","product_group","stock_qty"])


#sales_filtered = sales[sales["price"] > 100]
s_filtered = sales[~sales["product_group"].isin(["PG1","PG2","PG3"])]
#print(sales.head())
print(s_filtered)
import numpy as np
import pandas as pd

arr = np.random.randint(1, 10, size=(3,5))

df = pd.DataFrame(arr, columns=["A","B","C","D","E"])

#print(df)
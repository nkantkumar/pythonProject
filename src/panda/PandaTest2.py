import pandas as pd

staff = pd.read_csv("staff.csv")

print(f"\nStaff data frame has the following columns: \n{list(staff.columns)}\n")

#print(staff)
print(staff["name"].str[0:3])

print(staff["name"].str[-2:])

staff["last_name"] = staff["name"].str.split(" ", expand=True)[1]

print(staff[["name","last_name"]])
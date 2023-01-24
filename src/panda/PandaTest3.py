import pandas as pd
mydate = pd.to_datetime("2021-12-21 00:00:00")


print(f"The date part is {mydate.date()}")
print(f"The day of week is {mydate.weekday()}")
print(f"The name of the month is {mydate.month_name()}")
print(f"The name of the day is {mydate.day_name()}")

# read DataFrame
staff = pd.read_csv("staff.csv")

# change the data type of date columns
staff = staff.astype({
    "date_of_birth": "datetime64",
    "start_date": "datetime64[ns]",
})

# create start_month column
staff["start_month"] = staff["start_date"].dt.month

print(staff[["start_date","start_month"]])

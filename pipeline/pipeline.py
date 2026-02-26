import sys
import pandas as pd

print("arguments", sys.argv)

month = int(sys.argv[1])

df = pd.DataFrame({"Day": [1, 2], "No. of Passengers": [3, 4]})
df['Month'] = month
print(df.head())

df.to_parquet(f"output_month_{sys.argv[1]}.parquet")

print(f"Running pipeline for month {month}")
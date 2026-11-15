# check_dataset.py

import pandas as pd

df = pd.read_csv("data/patents.csv")

print(df.columns)
print("Rows:", len(df))

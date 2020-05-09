import pandas as pd

data = pd.read_csv("altered.csv")

print(data.iloc[1, data.columns.get_loc('codeParent')])
print(data.iloc[1, data.columns.get_loc('parentURL')])
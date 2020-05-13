import pandas as pd
import sys

data = pd.read_csv("altered.csv")

i=int(sys.argv[1])
print(data.iloc[i, data.columns.get_loc('parentURL')])
print(data.iloc[i, data.columns.get_loc('codeParent')])
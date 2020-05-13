import json
import pandas as pd

with open('writeFileToCSVCellSettings.json', 'r') as infile:
    settings = json.load(infile)

data = pd.read_csv(settings["csvFrom"])

with open(settings["fileFrom"], 'r') as infile:
    txt = infile.read()

if __name__ == "__main__":
    data.iloc[int(settings["rowToInserInto"]), data.columns.get_loc(settings["columnNameTo"])] = txt
    # print(data.iloc[int(settings["rowToInserInto"]), data.columns.get_loc(settings["columnNameTo"])])
    print(data.loc[[settings["rowToInserInto"]]])
    print(data.iloc[int(settings["rowToInserInto"]), data.columns.get_loc(settings["columnNameTo"])])
    data.to_csv(settings["csvTo"], index=False)
    print("actually saving and reopeneing file")
    data2 = pd.read_csv(settings["csvTo"])
    print(data2.iloc[int(settings["rowToInserInto"]), data.columns.get_loc(settings["columnNameTo"])])
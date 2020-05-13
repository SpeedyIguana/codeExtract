import os
import sys
import pandas as pd
from tld import get_tld
import requests
from bs4 import BeautifulSoup
from extractCodeFromUrl import *
from functionCalls import *

data = pd.read_csv("tt - tt.csv")

num_rows = data.shape[0]

# print(data.columns)

if len(sys.argv) > 1:
    iend = int(sys.argv[1])
else:
    iend = num_rows

if __name__ == '__main__':
    for i in range(iend):
        parentUrl = data.iloc[i, data.columns.get_loc('parentURL')]
        commitUrl = data.iloc[i, data.columns.get_loc('commitURL')]
        if not pd.isnull(parentUrl) and not pd.isnull(commitUrl):
            pres = get_tld(parentUrl, as_object=True)
            cres = get_tld(commitUrl, as_object=True)
            parentDomain = pres.parsed_url.netloc
            commitDomain = cres.parsed_url.netloc
            if requests.get(parentUrl).ok and requests.get(commitUrl).ok:
                fn = functionCalls.get(parentDomain, None)
                if fn is None:
                    print("*" * 20)
                    print("Missing Dict Entry for i = ", i, ", domain = ", parentDomain)
                    print("*" * 20)
                    continue
                print("-------------------------------------")
                print(i, parentUrl, commitUrl)
                data.iloc[i, data.columns.get_loc('codeParent')] = fn(parentUrl)
                data.iloc[i, data.columns.get_loc('codeCommit')] = fn(commitUrl)
                print("-------------------------------------")

    data.to_csv('altered.csv', index=False)

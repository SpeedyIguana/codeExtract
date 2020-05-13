import os
import sys
import pandas as pd
from tld import get_tld
import requests
from extractCodeFromUrl import *
from functionCalls import *

data = pd.read_csv("z.csv")

num_rows = data.shape[0]

# print(data.columns)

if len(sys.argv) > 1:
    iend = int(sys.argv[1])
else:
    iend = num_rows

badIs = []

pindent = 50

if __name__ == '__main__':
    # for i in range(260, 268):
    for i in range(iend):
        print("\n\n\n\n\n")
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
                    print("*" * pindent)
                    print("Missing Dict Entry for i = ", i, ", domain = ", parentDomain)
                    badIs.append(i)
                    print("*" * pindent)
                    continue
                parentCode = fn(parentUrl)
                commitCode = fn(commitUrl)
                if parentCode is None or commitCode is None:
                    print("*" * pindent)
                    print("Not able to GET for i = ", i, ", domain = ", parentDomain)
                    badIs.append(i)
                    print("*" * pindent)
                    continue
                else:
                    print("-" * pindent)
                    print("Able to GET for i = ", i, ", domain = ", parentDomain)
                    data.iloc[i, data.columns.get_loc('codeParent')] = parentCode
                    data.iloc[i, data.columns.get_loc('codeCommit')] = commitCode
                    data.to_csv('altered.csv', index=False)
                    print("-" * pindent)
                    data.to_csv('altered.csv', index=False)
            else:
                print("*" * pindent)
                print("Not OK HTTP request for i = ", i, ", domain = ", parentDomain)
                badIs.append(i)
                print("*" * pindent)
                continue



    data.to_csv('altered.csv', index=False)
    print(badIs)

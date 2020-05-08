import os
import pandas as pd
from tld import get_tld
import requests
from bs4 import BeautifulSoup
from extractCodeFromSoup import *

data = pd.read_csv("tt - tt.csv")

testedDomains = []

def writeParentAndCommitCode(parentcode, commitcode, parenturl, commiturl, row):
    dirx ="code/"+ str(row) + "/"
    fname = dirx +"smth.txt"
    if not os.path.exists(os.path.dirname(fname)):
        os.makedirs(os.path.dirname(fname))

    p = open(dirx + "parentCode.txt","w+")
    p.write(parentcode)
    p.close()

    c = open(dirx +"commitCode.txt","w+")
    c.write(commitcode)
    c.close()

    p = open(dirx + "parentUrl.txt","w+")
    p.write(parenturl)
    p.close()

    c = open(dirx + "commitUrl.txt","w+")
    c.write(commiturl)
    c.close()

if __name__ == '__main__':
    for i in range(data.shape[0]):
    # for i in range(1):
        parentUrl = data.iloc[i, 22]
        commitUrl = data.iloc[i, 23]
        if not pd.isnull(parentUrl) and not pd.isnull(commitUrl):
            pres = get_tld(parentUrl, as_object=True)
            cres = get_tld(commitUrl, as_object=True)
            parentDomain = pres.parsed_url.netloc
            commitDomain = cres.parsed_url.netloc
            if parentDomain not in testedDomains and commitDomain not in testedDomains:
                testedDomains.append(parentDomain)
                # continue testing
                parentReq = requests.get(parentUrl)
                commitReq = requests.get(commitUrl)
                if parentReq.ok and commitReq.ok:
                    parentHTML = parentReq.text
                    commitHTML = commitReq.text
                    psoup = BeautifulSoup(parentHTML, 'html.parser')
                    csoup = BeautifulSoup(commitHTML, 'html.parser')

                    if parentDomain == 'git.savannah.gnu.org':
                        # writeParentAndCommitCode(gitsavannahgnuorgCode(psoup),gitsavannahgnuorgCode(csoup),parentUrl,commitUrl,i)
                        continue
                    elif parentDomain == 'git.samba.org':
                        # writeParentAndCommitCode(gitsambaorg(psoup),gitsambaorg(csoup),parentUrl,commitUrl,i)
                        continue
                    elif parentDomain == 'git.php.net':
                        # writeParentAndCommitCode(gitphpnet(psoup),gitphpnet(csoup),parentUrl,commitUrl,i)
                        continue
                    elif parentDomain == 'cgit.kde.org':
                        # writeParentAndCommitCode(cgitkdeorg(parentUrl),cgitkdeorg(commitUrl),parentUrl,commitUrl,i)
                        continue
                    elif parentDomain == 'git.ganeti.org':
                        # writeParentAndCommitCode(gitganetiorg(psoup),gitganetiorg(csoup),parentUrl,commitUrl,i)
                        continue
                    else:
                        print(i + 2)
                        break

    print(testedDomains)
import os
import pandas as pd
from tld import get_tld
import requests
from bs4 import BeautifulSoup
from extractCodeFromSoup import *

data = pd.read_csv("tt - tt.csv")

# testedDomains = []

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
    # for i in range(data.shape[0]):
    for i in range(320, data.shape[0]):
        parentUrl = data.iloc[i, 22]
        commitUrl = data.iloc[i, 23]
        if not pd.isnull(parentUrl) and not pd.isnull(commitUrl):
            pres = get_tld(parentUrl, as_object=True)
            cres = get_tld(commitUrl, as_object=True)
            parentDomain = pres.parsed_url.netloc
            commitDomain = cres.parsed_url.netloc
            # if parentDomain not in testedDomains and commitDomain not in testedDomains:
            # testedDomains.append(parentDomain)
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
                elif parentDomain == 'git.busybox.net':
                    # writeParentAndCommitCode(gitbusyboxnet(parentUrl),gitbusyboxnet(commitUrl),parentUrl,commitUrl,i)
                    continue
                elif parentDomain == 'git.tt-rss.org':
                    # writeParentAndCommitCode(gitttrssorg(parentUrl),gitttrssorg(commitUrl),parentUrl,commitUrl,i)
                    continue
                elif parentDomain == 'git.openssl.org':
                    # writeParentAndCommitCode(gitopensslorg(psoup),gitopensslorg(csoup),parentUrl,commitUrl,i)
                    continue
                elif parentDomain == 'git.kernel.org':
                    # writeParentAndCommitCode(gitkernelorg(psoup),gitkernelorg(csoup),parentUrl,commitUrl,i)
                    continue
                elif parentDomain == 'git.ghostscript.com':
                    # writeParentAndCommitCode(gitghostscriptcom(parentUrl),gitghostscriptcom(commitUrl),parentUrl,commitUrl,i)
                    continue
                elif parentDomain == 'git.moodle.org':
                    # writeParentAndCommitCode(gitmoodleorg(psoup),gitmoodleorg(csoup),parentUrl,commitUrl,i)
                    continue
                elif parentDomain == 'git.spip.net':
                    # writeParentAndCommitCode(gitspipnet(parentUrl),gitspipnet(commitUrl),parentUrl,commitUrl,i)
                    continue
                elif parentDomain == 'git.haproxy.org':
                    # writeParentAndCommitCode(githaproxyorg(psoup),githaproxyorg(csoup),parentUrl,commitUrl,i)
                    continue
                elif parentDomain == 'cgit.freedesktop.org':
                    # writeParentAndCommitCode(cgitfreedesktoporg(parentUrl),cgitfreedesktoporg(commitUrl),parentUrl,commitUrl,i)
                    continue
                elif parentDomain == 'git.shibboleth.net':
                    # writeParentAndCommitCode(gitshibbolethnet(parentUrl),gitshibbolethnet(commitUrl),parentUrl,commitUrl,i)
                    continue
                elif parentDomain == 'git.pengutronix.de':
                    # writeParentAndCommitCode(gitpengutronixde(parentUrl),gitpengutronixde(commitUrl),parentUrl,commitUrl,i)
                    continue
                elif parentDomain == 'git.netfilter.org':
                    # writeParentAndCommitCode(gitnetfilterorg(parentUrl),gitnetfilterorg(commitUrl),parentUrl,commitUrl,i)
                    continue
                elif parentDomain == 'git.qemu.org':
                    # writeParentAndCommitCode(gitqemuorg(parentUrl),gitqemuorg(commitUrl),parentUrl,commitUrl,i)
                    continue
                elif parentDomain == 'git.linuxtv.org':
                    # writeParentAndCommitCode(gitlinuxtvorg(parentUrl),gitlinuxtvorg(commitUrl),parentUrl,commitUrl,i)
                    continue
                elif parentDomain == 'git.musl-libc.org':
                    # writeParentAndCommitCode(gitmusllibcorg(parentUrl),gitmusllibcorg(commitUrl),parentUrl,commitUrl,i)
                    continue
                elif parentDomain == 'git.infradead.org':
                    # writeParentAndCommitCode(gitinfradeadorg(parentUrl),gitinfradeadorg(commitUrl),parentUrl,commitUrl,i)
                    continue
                elif parentDomain == 'anongit.mindrot.org':
                    # writeParentAndCommitCode(anongitmindrotorg(parentUrl),anongitmindrotorg(commitUrl),parentUrl,commitUrl,i)
                    continue
                elif parentDomain == 'git.postgresql.org':
                    # writeParentAndCommitCode(gitpostgresql(parentUrl),gitpostgresql(commitUrl),parentUrl,commitUrl,i)
                    continue
                elif parentDomain == 'git.hylafax.org':
                    # writeParentAndCommitCode(githylafaxorg(parentUrl),githylafaxorg(commitUrl),parentUrl,commitUrl,i)
                    continue
                elif parentDomain == 'git.linux-nfs.org':
                    writeParentAndCommitCode(gitlinuxnfsorg(parentUrl),gitlinuxnfsorg(commitUrl),parentUrl,commitUrl,i)
                    continue
                else:
                    print(i + 2, parentDomain)
                    break

    # print(testedDomains)
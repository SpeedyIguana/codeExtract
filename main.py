import os
import pandas as pd
from tld import get_tld
import requests
from bs4 import BeautifulSoup
from extractCodeFromUrl import *

data = pd.read_csv("tt - tt.csv")

num_rows = data.shape[0]

# print(data.columns)

functionCalls = {
    'git.savannah.gnu.org': gitsavannahgnuorgCode,
    'git.samba.org': gitsambaorg,
    'git.php.net': gitphpnet,
    'cgit.kde.org': cgitkdeorg,
    'git.ganeti.org': gitganetiorg,
    'git.busybox.net': gitbusyboxnet,
    'git.tt-rss.org': gitttrssorg,
    'git.openssl.org': gitopensslorg,
    'git.kernel.org': gitkernelorg,
    'git.ghostscript.com': gitghostscriptcom,
    'git.moodle.org': gitmoodleorg,
    'git.spip.net': gitspipnet,
    'git.haproxy.org': githaproxyorg,
    'cgit.freedesktop.org': cgitfreedesktoporg,
    'git.shibboleth.net': gitshibbolethnet,
    'git.pengutronix.de': gitpengutronixde,
    'git.netfilter.org': gitnetfilterorg,
    'git.qemu.org': gitqemuorg,
    'git.linuxtv.org': gitlinuxtvorg,
    'git.musl-libc.org': gitmusllibcorg,
    'git.infradead.org': gitinfradeadorg,
    'anongit.mindrot.org': anongitmindrotorg,
    'git.postgresql.org': gitpostgresql,
    'git.hylafax.org': githylafaxorg,
    'git.linux-nfs.org': gitlinuxnfsorg,
    'git.linaro.org': gitlinaroorg,
    'git.altlinux.org': gitaltlinuxorg,
    'git.gnupg.org': gitgnupgorg,
    'git.deluge-torrent.org': gitdelugetorrentorg,
    'git.lxde.org': gitlxdeorg,
    'htcondor-git.cs.wisc.edu': htcondorgitcswiscedu,
    'git.quassel-irc.org': gitquasselircorg,
    'git.libav.org': gitlibavorg,
    'git.tartarus.org': gittartarusorg,
    'git.strongswan.org': gitstrongswanorg,
    'git.openafs.org': gitopenafsorg,
    'git.exim.org': giteximorg,
    'git.lysator.liu.se': gitlysatorliuse,
    'git.libssh.org': gitlibsshorg,
    'git.eyrie.org': giteyrieorg,
    'git.tukaani.org': gittukaaniorg,
    'git.launchpad.net': gitlaunchpadnet,
    'git.jetbrains.org': gitjetbrainsorg,
    'git.wpitchoune.net': gitwpitchounenet,
    'git.enlightenment.org': gitenlightenmentorg
}

if __name__ == '__main__':
    # for i in range(num_rows):
    for i in range(0, 10):
        parentUrl = data.iloc[i, 22]
        commitUrl = data.iloc[i, 23]
        if not pd.isnull(parentUrl) and not pd.isnull(commitUrl):
            pres = get_tld(parentUrl, as_object=True)
            cres = get_tld(commitUrl, as_object=True)
            parentDomain = pres.parsed_url.netloc
            commitDomain = cres.parsed_url.netloc
            if requests.get(parentUrl).ok and requests.get(commitUrl).ok:
                fn = functionCalls.get(parentDomain, None)
                if fn is None:
                    print(i, parentDomain)
                    break
                print("-------------------------------------")
                print(i, parentUrl, commitUrl)
                data.iloc[i, data.columns.get_loc('codeParent')] = fn(parentUrl)
                data.iloc[i, data.columns.get_loc('codeCommit')] = fn(commitUrl)
                print("-------------------------------------")

    data.to_csv('altered.csv', index=False)
import requests
import time

def download_file(url, wait=False):
    if wait:
        time.sleep(10)
    try:
        req = requests.request('GET', url, timeout = None)
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        # raise SystemExit(e)
        # print(e)
        return None
    # req = requests.get(url, timeout = None)
    return(req.text)

def gitsavannahgnuorgCode(url):
    if 'blob' in url:
        urlnew = url.replace('blob', 'blob_plain')
    elif 'tree' in url:
        urlnew = url.replace('tree','plain')
    return(download_file(urlnew))

def gitsambaorg(url):
    urlnew = url.replace('blob', 'blob_plain')
    return(download_file(urlnew, wait = True))

def gitphpnet(url):
    urlnew = url.replace('blob', 'blob_plain')
    return(download_file(urlnew))

def cgitkdeorg(url):
    urlnew = url.replace('tree', 'plain')
    return(download_file(urlnew))

def gitganetiorg(url):
    urlnew = url.replace('blob', 'blob_plain')
    return(download_file(urlnew))

def gitbusyboxnet(url):
    urlnew = url.replace('tree', 'plain')
    return(download_file(urlnew))

def gitttrssorg(url):
    urlnew = url.replace('src', 'raw')
    return(download_file(urlnew))

def gitopensslorg(url):
    urlnew = url.replace('blob', 'blob_plain')
    return(download_file(urlnew))

def gitkernelorg(url):
    urlnew = url.replace('tree', 'plain')
    return(download_file(urlnew))

def gitghostscriptcom(url):
    urlnew = url.replace('blob', 'blob_plain')
    return(download_file(urlnew))

def gitmoodleorg(url):
    urlnew = url.replace('blob', 'blob_plain')
    return(download_file(urlnew))

def gitspipnet(url):
    urlnew = url.replace('src', 'raw')
    return(download_file(urlnew))

def githaproxyorg(url):
    urlnew = url.replace('blob', 'blob_plain')
    return(download_file(urlnew))

def cgitfreedesktoporg(url):
    urlnew = url.replace('tree', 'plain')
    return(download_file(urlnew))

def gitshibbolethnet(url):
    urlnew = url.replace('blob', 'blob_plain')
    return(download_file(urlnew))

def gitpengutronixde(url):
    urlnew = url.replace('tree', 'plain')
    return(download_file(urlnew))

def gitnetfilterorg(url):
    urlnew = url.replace('tree', 'plain')
    return(download_file(urlnew))

def gitqemuorg(url):
    urlnew = url.replace('blob', 'blob_plain')
    return(download_file(urlnew))

def gitlinuxtvorg(url):
    urlnew = url.replace('tree', 'plain')
    return(download_file(urlnew))

def gitmusllibcorg(url):
    urlnew = url.replace('tree', 'plain')
    return(download_file(urlnew))

def gitinfradeadorg(url):
    urlnew = url.replace('blob', 'blob_plain')
    return(download_file(urlnew))

def anongitmindrotorg(url):
    urlnew = url.replace('tree', 'plain')
    return(download_file(urlnew, wait = True))

def gitpostgresql(url):
    urlnew = url.replace('blob', 'blob_plain')
    return(download_file(urlnew))

def githylafaxorg(url):
    urlnew = url.replace('blob', 'blob_plain')
    return(download_file(urlnew))

def gitlinuxnfsorg(url):
    urlnew = url.replace('blob', 'blob_plain')
    return(download_file(urlnew))

def gitlinaroorg(url):
    urlnew = url.replace('tree', 'plain')
    return(download_file(urlnew))

def gitaltlinuxorg(url):
    urlnew = url.replace('blob', 'blob_plain')
    return(download_file(urlnew))

def gitgnupgorg(url):
    urlnew = url.replace('blob', 'blob_plain')
    return(download_file(urlnew))

def gitdelugetorrentorg(url):
    urlnew = url.replace('tree', 'plain')
    return(download_file(urlnew))

def gitlxdeorg(url):
    urlnew = url.replace('blob', 'blob_plain')
    return(download_file(urlnew))

def htcondorgitcswiscedu(url):
    urlnew = url.replace('blob', 'blob_plain')
    return(download_file(urlnew))

def gitquasselircorg(url):
    urlnew = url.replace('blob', 'blob_plain')
    return(download_file(urlnew))

def gitlibavorg(url):
    urlnew = url.replace('blob', 'blob_plain')
    return(download_file(urlnew))

def gittartarusorg(url):
    urlnew = url.replace('blob', 'blob_plain')
    return(download_file(urlnew))

def gitstrongswanorg(url):
    urlnew = url.replace('blob', 'blob_plain')
    return(download_file(urlnew))

def gitopenafsorg(url):
    urlnew = url.replace('blob', 'blob_plain')
    return(download_file(urlnew))

def giteximorg(url):
    urlnew = url.replace('blob', 'blob_plain')
    return(download_file(urlnew))

def gitlysatorliuse(url):
    urlnew = url.replace('blob', 'raw')
    return(download_file(urlnew))

def gitlibsshorg(url):
    urlnew = url.replace('tree', 'plain')
    return(download_file(urlnew))

def giteyrieorg(url):
    urlnew = url.replace('blob', 'blob_plain')
    return(download_file(urlnew))

def gittukaaniorg(url):
    urlnew = url.replace('blob', 'blob_plain')
    return(download_file(urlnew))

def gitlaunchpadnet(url):
    urlnew = url.replace('tree', 'plain')
    return(download_file(urlnew))

def gitjetbrainsorg(url):
    urlnew = url.replace('blob', 'blob_plain')
    return(download_file(urlnew))

def gitwpitchounenet(url):
    urlnew = url.replace('blob', 'blob_plain')
    return(download_file(urlnew))

def gitenlightenmentorg(url): 
    urlnew = url.replace('tree', 'plain')
    return(download_file(urlnew))

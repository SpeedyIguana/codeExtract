from bs4 import BeautifulSoup
import requests

def gitsavannahgnuorgCode(sp):
    return(sp.code.text)

def gitsambaorg(sp):
    rtn = ""
    outerDiv = sp.findAll("div", {"class": "page_body"})
    for div in outerDiv:
        pres = div.findAll("div", {"class": "pre"})
        for pre in pres:
            txt = pre.find(text = True, recursive = False)
            rtn += txt + "\n"
    return(rtn)

def gitphpnet(sp):
    rtn = ""
    outerDiv = sp.findAll("div", {"class": "page_body"})
    for div in outerDiv:
        pres = div.findAll("div", {"class": "pre"})
        for pre in pres:
            txt = pre.find(text = True, recursive = False)
            rtn += txt + "\n"
    return(rtn)

def cgitkdeorg(url):
    urlnew = url.replace('tree', 'plain')
    req = requests.get(urlnew)
    return(req.text)

def gitganetiorg(sp):
    rtn = ""
    outerDiv = sp.findAll("div", {"class": "page_body"})
    for div in outerDiv:
        pres = div.findAll("div", {"class": "pre"})
        for pre in pres:
            spans = pre.findAll("span")
            for span in spans:
                txt = span.find(text = True, recursive = False)
                if txt is not None:
                    rtn += txt + "\n"
                else:
                    rtn += "\n"
    return(rtn)

def gitbusyboxnet(url):
    urlnew = url.replace('tree', 'plain')
    req = requests.get(urlnew)
    return(req.text)

def gitttrssorg(url):
    urlnew = url.replace('src', 'raw')
    req = requests.get(urlnew)
    return(req.text)

def gitopensslorg(sp):
    rtn = ""
    outerDiv = sp.findAll("div", {"class": "page_body"})
    for div in outerDiv:
        pres = div.findAll("div", {"class": "pre"})
        for pre in pres:
            txt = pre.find(text = True, recursive = False)
            rtn += txt + "\n"
    return(rtn)

def gitkernelorg(sp):
    rtn = ""
    outerDiv = sp.findAll("div", {"class": "highlight"})
    for div in outerDiv:
        txt = div.text
        if txt is not None:
            rtn += txt + "\n"
        else:
            rtn += "\n"
    return(rtn)

def gitghostscriptcom(url):
    urlnew = url.replace('blob', 'blob_plain')
    req = requests.get(urlnew)
    return(req.text)

def gitmoodleorg(sp):
    rtn = ""
    outerDiv = sp.findAll("div", {"class": "page_body"})
    for div in outerDiv:
        pres = div.findAll("div", {"class": "pre"})
        for pre in pres:
            txt = pre.find(text = True, recursive = False)
            rtn += txt + "\n"
    return(rtn)

def gitspipnet(url):
    urlnew = url.replace('src', 'raw')
    req = requests.get(urlnew)
    return(req.text)

def githaproxyorg(sp):
    rtn = ""
    outerDiv = sp.findAll("div", {"class": "page_body"})
    for div in outerDiv:
        pres = div.findAll("div", {"class": "pre"})
        for pre in pres:
            txt = pre.find(text = True, recursive = False)
            rtn += txt + "\n"
    return(rtn)

def cgitfreedesktoporg(url):
    urlnew = url.replace('tree', 'plain')
    req = requests.get(urlnew)
    return(req.text)

def gitshibbolethnet(url):
    urlnew = url.replace('blob', 'blob_plain')
    req = requests.get(urlnew)
    return(req.text)

def gitpengutronixde(url):
    urlnew = url.replace('tree', 'plain')
    req = requests.get(urlnew)
    return(req.text)

def gitnetfilterorg(url):
    urlnew = url.replace('tree', 'plain')
    req = requests.get(urlnew)
    return(req.text)

def gitqemuorg(url):
    urlnew = url.replace('blob', 'blob_plain')
    req = requests.get(urlnew)
    return(req.text)

def gitlinuxtvorg(url):
    urlnew = url.replace('tree', 'plain')
    req = requests.get(urlnew)
    return(req.text)

def gitmusllibcorg(url):
    urlnew = url.replace('tree', 'plain')
    req = requests.get(urlnew)
    return(req.text)

def gitinfradeadorg(url):
    urlnew = url.replace('blob', 'blob_plain')
    req = requests.get(urlnew)
    return(req.text)

def anongitmindrotorg(url):
    urlnew = url.replace('tree', 'plain')
    req = requests.get(urlnew)
    return(req.text)

def gitpostgresql(url):
    urlnew = url.replace('blob', 'blob_plain')
    req = requests.get(urlnew)
    return(req.text)

def githylafaxorg(url):
    urlnew = url.replace('blob', 'blob_plain')
    req = requests.get(urlnew)
    return(req.text)

def gitlinuxnfsorg(url):
    urlnew = url.replace('blob', 'blob_plain')
    req = requests.get(urlnew)
    return(req.text)

def gitlinaroorg(url):
    urlnew = url.replace('tree', 'plain')
    req = requests.get(urlnew)
    return(req.text)

def gitaltlinuxorg(url):
    urlnew = url.replace('blob', 'blob_plain')
    req = requests.get(urlnew)
    return(req.text)

def gitgnupgorg(url):
    urlnew = url.replace('blob', 'blob_plain')
    req = requests.get(urlnew)
    return(req.text)

def gitdelugetorrentorg(url):
    urlnew = url.replace('tree', 'plain')
    req = requests.get(urlnew)
    return(req.text)

def gitlxdeorg(url):
    urlnew = url.replace('blob', 'blob_plain')
    req = requests.get(urlnew)
    return(req.text)

def htcondorgitcswiscedu(url):
    urlnew = url.replace('blob', 'blob_plain')
    req = requests.get(urlnew)
    return(req.text)

def gitquasselircorg(url):
    urlnew = url.replace('blob', 'blob_plain')
    req = requests.get(urlnew)
    return(req.text)

def gitlibavorg(url):
    urlnew = url.replace('blob', 'blob_plain')
    req = requests.get(urlnew)
    return(req.text)

def gittartarusorg(url):
    urlnew = url.replace('blob', 'blob_plain')
    req = requests.get(urlnew)
    return(req.text)

def gitstrongswanorg(url):
    urlnew = url.replace('blob', 'blob_plain')
    req = requests.get(urlnew)
    return(req.text)

def gitopenafsorg(url):
    urlnew = url.replace('blob', 'blob_plain')
    req = requests.get(urlnew)
    return(req.text)

def giteximorg(url):
    urlnew = url.replace('blob', 'blob_plain')
    req = requests.get(urlnew)
    return(req.text)

def gitlysatorliuse(url):
    urlnew = url.replace('blob', 'raw')
    req = requests.get(urlnew)
    return(req.text)

def gitlibsshorg(url):
    urlnew = url.replace('tree', 'plain')
    req = requests.get(urlnew)
    return(req.text)

def giteyrieorg(url):
    urlnew = url.replace('blob', 'blob_plain')
    req = requests.get(urlnew)
    return(req.text)

def gittukaaniorg(url):
    urlnew = url.replace('blob', 'blob_plain')
    req = requests.get(urlnew)
    return(req.text)

def gitlaunchpadnet(url):
    urlnew = url.replace('tree', 'plain')
    req = requests.get(urlnew)
    return(req.text)

def gitjetbrainsorg(url):
    urlnew = url.replace('blob', 'blob_plain')
    req = requests.get(urlnew)
    return(req.text)
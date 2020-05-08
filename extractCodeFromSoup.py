from bs4 import BeautifulSoup

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
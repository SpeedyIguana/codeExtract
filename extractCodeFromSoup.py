from bs4 import BeautifulSoup

def gitsavannahgnuorgCode(sp):
    rtn = str(sp.code)
    rtn = rtn[6: -7]
    return rtn
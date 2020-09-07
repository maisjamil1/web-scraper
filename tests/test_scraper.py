# import requests
# from bs4 import BeautifulSoup
from web_scraper.scraper import get_citations_needed_count,get_citations_needed_report
import pytest

#get_citations_needed_count test
def test_1():
    URL = "https://en.wikipedia.org/wiki/History_of_Mexico"
    actual = 5
    expected = get_citations_needed_count(URL)
    assert actual == expected
    # assert 'hi' == 'hi'


def test_2():
    URL = "https://en.wikipedia.org/wiki/History_of_Jordan"
    actual = 3
    expected = get_citations_needed_count(URL)
    assert actual == expected



# _______________________________________________________________________


#get_citations_needed_report test

def test_3():
    URL = "https://en.wikipedia.org/wiki/History_of_Mexico"
    li1=get_citations_needed_report(URL)
    # li2=[]
    # for i in range(len(li1)):
    #     y=li1[i].split('[')[0]
    #     li2.append(y)
    
    # actual = li2[0]
    actual = li1[0]
    expected = "The first people to settle in Mexico encountered a climate far milder than the current one. In particular, the Valley of Mexico contained several large paleo-lakes (known collectively as Lake Texcoco) surrounded by dense forest. Deer were found in this area, but most fauna were small land animals and fish and other lacustrine animals were found in the lake region.[citation needed][7] Such conditions encouraged the initial pursuit of a hunter-gatherer existence."
    assert actual == expected



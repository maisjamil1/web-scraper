import requests
from bs4 import BeautifulSoup
#colors
from colorama import Fore, Back, Style,init
from termcolor import colored, cprint 
import sys 

# _________________  (colors)  ____________________
def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk)) 
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk)) 
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk)) 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk)) 
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk)) 

intro="""


 _     _  _______  _______    _______  _______  ______    _______  _______  ___   __    _  _______ 
| | _ | ||       ||  _    |  |       ||       ||    _ |  |   _   ||       ||   | |  |  | ||       |
| || || ||    ___|| |_|   |  |  _____||       ||   | ||  |  |_|  ||    _  ||   | |   |_| ||    ___|
|       ||   |___ |       |  | |_____ |       ||   |_||_ |       ||   |_| ||   | |       ||   | __ 
|       ||    ___||  _   |   |_____  ||      _||    __  ||       ||    ___||   | |  _    ||   ||  |
|   _   ||   |___ | |_|   |   _____| ||     |_ |   |  | ||   _   ||   |    |   | | | |   ||   |_| |
|__| |__||_______||_______|  |_______||_______||___|  |_||__| |__||___|    |___| |_|  |__||_______|


"""

about_the_lab="""
Scrape a Wikipedia page and record which passages need citations.
E.g. History of Mexico has 7 “citation needed” cases, as of this writing.
Your web scraper should report the number of citations needed.
Your web scraper should identify those cases AND include the relevant passage.
E.g. Citation needed for “lorem spam and impsum eggs”
Consider the “relevant passage” to be the parent element that contains the
 passage, often a paragraph element.
"""

text = colored('about_the_lab', 'yellow', attrs=['reverse', 'blink']) 



URL = "https://en.wikipedia.org/wiki/History_of_Mexico"


# test = soup.find(title="Wikipedia:Citation needed")
# print(test)


# _________________________________________
# Count function must be named get_citations_needed_count
# get_citations_needed takes in a url and returns an integer
def get_citations_needed_count(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results =soup.find_all('a', href="/wiki/Wikipedia:Citation_needed")
    prCyan(f'Total Number of citations  {len(results)}')
    prPurple('*'*100)
    return len(results)

# _________________________________________
# Report function must be named get_citations_needed_report
# get_citations_needed_report takes in a url and returns a string
# the string should be formatted with each citation needed on own line, in order found.
def get_citations_needed_report(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results =soup.find_all('a', href="/wiki/Wikipedia:Citation_needed")
    # print(results)

    # print(results[0].text.strip())
    li1=[]
    li2=[]
    for i in range (len(results)):
        x=i+1
        # print(f'citations number{x}')
        print(colored(f'citations number{x}', 'yellow', 'on_blue'))
        prLightPurple('-'*100)
        prGreen(results[i].parent.parent.parent.getText())
        li1.append(results[i].parent.parent.parent.getText())
        # li1.append(results[i].parent.parent.parent.getText().strip())
        prLightPurple('-'*100)
    # print(li1)


    for i in range(len(li1)):
        y=li1[i].split('[')[0]
        li2.append(y)
    # print(f'list 2 --->{li2}')

    return li1

  





if __name__ == "__main__":
    prCyan(intro)
    print(text) 
    prRed(about_the_lab)
    prPurple('='*100)
    get_citations_needed_count(URL)
    get_citations_needed_report(URL)
    # pass
import requests
from bs4 import BeautifulSoup

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
    print(len(results))
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
    # li2=[]
    for i in range (len(results)):
        x=i+1
        print(f'citations number{x}')
        print('-'*100)
        print(results[i].parent.parent.parent.getText())
        # li1.append(results[i].parent.parent.parent.getText())
        li1.append(results[i].parent.parent.parent.getText().strip())
        return li1


    # for i in range(len(li1)):
    #     y=li1[i].split('[')[0]
    #     li2.append(y)
    # print(f'list 2 --->{li2}')


  





if __name__ == "__main__":
    get_citations_needed_count(URL)
    get_citations_needed_report(URL)
    # pass
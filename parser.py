from bs4 import BeautifulSoup
import requests
from prettytable import PrettyTable



def pars(url):
    
    headers = {'User-Agent': "Edge/12.246"}
    page = requests.get(url)
    print(page.status_code)

    table=[]
    allNews = []

    soup = BeautifulSoup(page.content, "html5lib")

    allNews = soup.findAll('div', attrs={'class':['post-content',
                                                'text-color-dark',
                                                'post-meta']})

    for div in set(allNews):
        table.append(div.find('a').contents[0].strip().lstrip())

    t = PrettyTable(['N', 'News'])
    t.align['News'] = "l"

    #table = [x.strip(' ') for x in table]

    for i,j in enumerate(table,1):
        t.add_row([i,j])
        
    return print(t)

url = 'http://mignews.com/mobile'
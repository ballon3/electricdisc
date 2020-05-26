import httpx 
import requests
from bs4 import BeautifulSoup as bso

class BMW:

    BASE_URL = 'https://www.realoem.com/bmw/'
    LANGUAGE = 'enUS'
    URL = f"{BASE_URL}{LANGUAGE}"

    'https://www.realoem.com/bmw/enUS/partgrp?id=0573-USA-12-1991-K569-BMW-K_75_RT_0565,0573_&mg=46'
    'https://www.realoem.com/bmw/enUS/showparts?id=0573-USA-12-1991-K569-BMW-K_75_RT_0565,0573_&diagId=34_1906'
    'https://www.realoem.com/bmw/enUS/showparts?id=0573-USA-12-1991-K569-BMW-K_75_RT_0565,0573_&diagId=34_1905'

    def get_main_group(id):
        params = {'id':id}
        r = httpx.get(f'{URL}/partgrp', params=params)
        print(r)
        print(r.url)
        return r.text 


    def get_sub_group(url, filter):
        pass

    def get_part(diagId):
        pass

def extract_link(soupy):
    soup = bso(soupy, "html.parser")
            
    for links in soup.find_all("a"):
        href = links.
        print(href,title)
    

def test_main_group(id):
    BASE_URL = 'https://www.realoem.com/bmw/'
    LANGUAGE = 'enUS'
    URL = f"{BASE_URL}{LANGUAGE}"
    params = {'id':id}
    r = httpx.get(f'{URL}/partgrp', params=params)
    soup = bso(r.text, "html.parser")
            
    for links in soup.find_all("div", {"class": "mg-thumb"}):
        href = links.
        print(href,title)

K75 = '0573-USA-12-1991-K569-BMW-K_75_RT_0565%2C0573_'

test_main_group(K75)
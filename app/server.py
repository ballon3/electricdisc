from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

import json
import os
from toolz import memoize
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

app = FastAPI()

# TODO: Change origin to real domain to reject Ajax requests from elsewhere
app.add_middleware(CORSMiddleware, allow_origins=['*'])
app.mount("/static", StaticFiles(directory="static"), name="static")


# SCRAPE UTILS 

def get_heading(diag):
    pass


url = 'https://www.python.org/static/img/python-logo@2x.png'

myfile = requests.get(url)

async def get_image(url):
    # download full size realoem image to folder /static/realoem/bike_id/
    if main:
        pass
    elif group:
        pass
    else:
        pass

    path = f"./static/realoem/{}/"
    url = diag.find_all("a", "href")
    for e in url:
        image = httpx.get(url)
        open(path, 'wb').write(myfile.content)

    pass 

def get_title(diag):
    pass

# COMPARE BIKES

def get_main_group(id: str):
    pass

def get_part_group(id: str):
    pass

def get_part(id: str):
    pass


# LiST TOOLS FOR PART, GRP, or BIKE

# PRICE BREAKDOWN


@app.get('/api/verse/{book}/{chapter}/{verse}')
def load_k75(book: str, chapter: int, verse: int):
    
    #

    try:
        return {'text': data()[book][str(chapter)][str(verse)]}
    except KeyError as e:
        return {'error': str(e), 'type': 'KeyError'}


import pydantic 
from typing import Optional, List


class Diagram(BaseModel):
    number: id 
    description: Optional[str]
    supply: Optional[str]
    qauntity: Optional[int]
    date: Optional[str]
    end_date: Optional[str]
    part_number: int 
    part_link: Optional[str]
    price: Optional[int]
    notes: Optional[str]
    image: Optional[str]

class Component(BaseModel):
    image: Optional[str]
    diagram: Optional[Diagram] 
    title: str
    heading: str 

class Part(BaseModel):
    heading: str 
    components: List[Component]

class PartGrp(BaseModel):
    groups: List[Part]

class System:
    image: Optional[str]
    system: str
    url: Optional[str] 

class MainGrp(BaseModel):
    systems: List[System]


No.	Description	Supp.	Qty	 From 	 Up To 	Part Number	Price		Notes
01	Black engine		1			11001461242			ENDED, +core
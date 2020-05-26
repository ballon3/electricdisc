from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

import json
import os
from toolz import memoize
import httpx 

app = FastAPI()

# TODO: Change origin to real domain to reject Ajax requests from elsewhere
app.add_middleware(CORSMiddleware, allow_origins=['*'])
app.mount("/static", StaticFiles(directory="static"), name="static")

@memoize
def data():
    with open(os.path.join(os.path.dirname(__file__), 'esv.json')) as f:
        return json.load(f)



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
class partComponent(BaseModel):
    image: Optional[str]
    diagram: Optional[Diagram] 
    title: str
    heading: str 
class Part(BaseModel):
    heading: str 
    components: List[partComponent]

class partGroup(BaseModel):
    groups: List[Part]

class Systems:
    image: Optional[str]
    system: str
    url: Optional[str] 

class mainGroup(BaseModel):
    systems: List[Systems]


No.	Description	Supp.	Qty	 From 	 Up To 	Part Number	Price		Notes
01	Black engine		1			11001461242			ENDED, +core
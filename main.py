import re
from urllib import request
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

@app.get("/")
def index():
    # return 'hi'
    return {'data':{"name":'sabeel','age':22}}

@app.get('/about')
def about():
    return {'data':'about page'}

@app.get("/blog")
def blog():
    return {"data":"blog list"}

@app.get("/blogs")
def blog(published:bool=True,limit:int=10,sort:Optional[str]=None):
    if published:
      return {"data":f'{limit} blogs'}
    return {"data":'all blogs'}

@app.get('/blog/unpublished')
def show():
    return {'data':'unpublished blogs'}


@app.get('/blog/{id}')
def show(id:int):
    return {'data':id}

@app.get('/blog/{id}/comments')
def comments(id):
    return {'data':{'1','2'}}

 

@app.post('/blog')
def checkhing():
    return {'data':'this is post method'}

class Blog(BaseModel):
    title : str
    body : str
    published_at : Optional[bool]


@app.post('/blogs')
def create_blog(request:Blog):
    return f'blog created with title {request.title}'


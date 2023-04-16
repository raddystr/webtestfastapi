from typing import Optional
from enum import Enum
from fastapi import FastAPI

app = FastAPI()

 
@app.get('/')
def index():
    return {'message': 'Hello world!'}


@app.get('/blog/all')
def get_all_blogs(page=1, page_size: Optional[int]=None):
    if page_size:
        return {'message': f'All {page_size} blogs on page {page}'}
    return {'message': f'We are on {page}'}


@app.get('/blog/{id}/comments/{comment_id}')
def get_comment(id: int, comment_id: int, 
    valid: bool=True, username: Optional[str]=None):
     return{'message': (f'blog_id {id} comment_id'
        f'{comment_id} username {username}')}
     


class BlogType(str, Enum):
        short = 'short'
        story = 'story'
        howto = 'howto'


@app.get('/blog/type/{type}')
def get_blog_type(type: BlogType):
      return {'message': f'blog type {type}'}
      

@app.get('/blog/{id}')
def get_blog(id: int):
     return {'message': f'Blog with id {id}'}



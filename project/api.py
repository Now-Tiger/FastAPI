#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
from fastapi import FastAPI
import uvicorn as uv

from model import Post

app = FastAPI(
    Title="Simple Crud Operations",
)

# Dummy database to hold the all the posts
posts = list()


@app.get("/")
async def root() -> dict:
    return { "message": "Success!" }


@app.get("/api/v1/posts")
async def get_posts() -> dict:
    # GET method to fetch all the posts.
    return { "Posts": posts }


@app.get("/api/v1/posts/{postid}")
async def get_single_post(post_id: int) -> dict:
    """ GET single post from posts checking user given
        post id if not available return `ERROR MESSAGE`! 
    """
    for post in posts:
        if post_id == post.id:
            return { "post": post }
        else:
            return { "message": "Please check entered post id!" }


@app.post("/api/v1/post")
async def post_item(post: Post) -> dict:
    # POST method to post data body at the endpoint
    if posts is not None:
        posts.append(post)
        return { "message": "Successfully added a post" }

    return { "message": "Some error occured!\nPlease check your internet connection" }


def main() -> None:
    # PUT MAIN METHOE HERE
    uv.run(
        "api:app",
        port=8000,
        reload=True
    )
    

if __name__ == "__main__":
    main()
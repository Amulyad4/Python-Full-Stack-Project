# api/main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sys, os

# Add src to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.logic import UserManager, PostManager, CommentManager, LikeManager

# --- FastAPI app ---
app = FastAPI(title="Blog Application API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

user_manager = UserManager()
post_manager = PostManager()
comment_manager = CommentManager()
like_manager = LikeManager()

# --- Models ---
class UserCreate(BaseModel):
    email: str
    password: str

class UserUpdate(BaseModel):
    email: str

class PostCreate(BaseModel):
    title: str
    content: str
    author_id: str

class PostUpdate(BaseModel):
    title: str = None
    content: str = None

class CommentCreate(BaseModel):
    post_id: str
    user_id: str
    content: str

class CommentUpdate(BaseModel):
    content: str

# --- Routes ---
@app.get("/")
def home():
    return {"message": "Blog API is running!"}

# Users
@app.get("/users")
def get_users():
    return user_manager.list_users()

@app.post("/users")
def create_user(user: UserCreate):
    result = user_manager.add_user(user.email, user.password)
    if not result.get("success"):
        raise HTTPException(status_code=400, detail=result.get("Message"))
    return result

@app.put("/users/{user_id}")
def update_user(user_id: str, user: UserUpdate):
    result = user_manager.edit_user(user_id, email=user.email)
    if not result.get("success"):
        raise HTTPException(status_code=400, detail=result.get("Message"))
    return result

@app.delete("/users/{user_id}")
def delete_user(user_id: str):
    return user_manager.remove_user(user_id)

# Posts
@app.get("/posts")
def get_posts():
    return post_manager.list_posts()

@app.post("/posts")
def create_post(post: PostCreate):
    result = post_manager.add_post(post.title, post.content, post.author_id)
    if not result.get("success"):
        raise HTTPException(status_code=400, detail=result.get("Message"))
    return result

@app.put("/posts/{post_id}")
def update_post(post_id: str, post: PostUpdate):
    result = post_manager.edit_post(post_id, title=post.title, content=post.content)
    if not result.get("success"):
        raise HTTPException(status_code=400, detail=result.get("Message"))
    return result

@app.delete("/posts/{post_id}")
def delete_post(post_id: str):
    return post_manager.remove_post(post_id)

@app.get("/posts/author/{author_id}")
def posts_by_author(author_id: str):
    return post_manager.posts_by_author(author_id)

# Comments
@app.post("/comments")
def create_comment(comment: CommentCreate):
    result = comment_manager.add_comment(comment.post_id, comment.user_id, comment.content)
    if not result.get("success"):
        raise HTTPException(status_code=400, detail=result.get("Message"))
    return result

@app.put("/comments/{comment_id}")
def update_comment(comment_id: str, comment: CommentUpdate):
    result = comment_manager.edit_comment(comment_id, comment.content)
    if not result.get("success"):
        raise HTTPException(status_code=400, detail=result.get("Message"))
    return result

@app.delete("/comments/{comment_id}")
def delete_comment(comment_id: str):
    return comment_manager.remove_comment(comment_id)

@app.get("/comments/post/{post_id}")
def get_comments(post_id: str):
    return comment_manager.comments_for_post(post_id)

# Likes
@app.post("/likes/{post_id}/{user_id}")
def like_post(post_id: str, user_id: str):
    return like_manager.like_a_post(post_id, user_id)

@app.delete("/likes/{post_id}/{user_id}")
def unlike_post(post_id: str, user_id: str):
    return like_manager.unlike_a_post(post_id, user_id)

@app.get("/likes/{post_id}")
def get_likes(post_id: str):
    return like_manager.likes_for_post(post_id)

# --- Run ---
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api.main:app", host="0.0.0.0", port=8000, reload=True)

# src/db.py
import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)

# --- User functions ---
def create_user(email, password):
    auth_res = supabase.auth.sign_up({"email": email, "password": password})
    if getattr(auth_res, "user", None):
        supabase.table("users").insert({
            "id": auth_res.user.id,
            "email": email
        }).execute()
    return auth_res

def get_all_users():
    return supabase.table("users").select("*").execute()

def update_user(user_id, email=None):
    if email:
        supabase.auth.update_user({"email": email})
        return supabase.table("users").update({"email": email}).eq("id", user_id).execute()
    return None

def delete_user(user_id):
    return supabase.table("users").delete().eq("id", user_id).execute()

# --- Post functions ---
def create_post(title, content, author_id):
    return supabase.table("posts").insert({
        "title": title,
        "content": content,
        "author_id": author_id
    }).execute()

def get_all_posts():
    return supabase.table("posts").select("*").execute()

def get_posts_by_author(author_id):
    return supabase.table("posts").select("*").eq("author_id", author_id).execute()

def update_post(post_id, title=None, content=None):
    updates = {}
    if title:
        updates["title"] = title
    if content:
        updates["content"] = content
    return supabase.table("posts").update(updates).eq("id", post_id).execute()

def delete_post(post_id):
    return supabase.table("posts").delete().eq("id", post_id).execute()

# --- Comment functions ---
def create_comment(post_id, user_id, content):
    return supabase.table("comments").insert({
        "post_id": post_id,
        "user_id": user_id,
        "content": content
    }).execute()

def get_comments_by_post(post_id):
    return supabase.table("comments").select("*").eq("post_id", post_id).execute()

def update_comment(comment_id, content=None):
    updates = {}
    if content:
        updates["content"] = content
    return supabase.table("comments").update(updates).eq("id", comment_id).execute()

def delete_comment(comment_id):
    return supabase.table("comments").delete().eq("id", comment_id).execute()

# --- Like functions ---
def like_post(post_id, user_id):
    return supabase.table("likes").insert({
        "post_id": post_id,
        "user_id": user_id
    }).execute()

def unlike_post(post_id, user_id):
    return supabase.table("likes").delete().eq("post_id", post_id).eq("user_id", user_id).execute()

def get_likes_by_post(post_id):
    return supabase.table("likes").select("*").eq("post_id", post_id).execute()

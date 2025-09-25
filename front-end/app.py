# front-end/app.py

import streamlit as st
import requests
from datetime import datetime

API_URL = "http://127.0.0.1:8000"  # your FastAPI backend

st.set_page_config(
    page_title="Blog App",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📝 My Blog Application")
st.markdown("A simple, beautiful blog frontend using Streamlit")

# ----------------- Sidebar -----------------
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Users", "Posts", "Create Post", "Create User"])

# ----------------- Helper Functions -----------------
def fetch_users():
    return requests.get(f"{API_URL}/users").json().get("data", [])

def fetch_posts():
    return requests.get(f"{API_URL}/posts").json().get("data", [])

def fetch_comments(post_id):
    return requests.get(f"{API_URL}/comments/post/{post_id}").json().get("data", [])

def fetch_likes(post_id):
    return requests.get(f"{API_URL}/likes/{post_id}").json().get("data", [])

def add_like(post_id, user_id):
    return requests.post(f"{API_URL}/likes/{post_id}/{user_id}")

def add_user(email, password):
    return requests.post(f"{API_URL}/users", json={"email": email, "password": password})

def add_post(title, content, author_id):
    return requests.post(f"{API_URL}/posts", json={"title": title, "content": content, "author_id": author_id})

def add_comment(post_id, user_id, content):
    return requests.post(f"{API_URL}/comments", json={"post_id": post_id, "user_id": user_id, "content": content})

# ----------------- Pages -----------------
if page == "Home":
    st.subheader("Welcome to the Blog App!")
    st.markdown("Use the sidebar to navigate between users, posts, and create content.")

elif page == "Users":
    st.subheader("Users")
    users = fetch_users()
    if users:
        for user in users:
            st.info(f"👤 {user['email']} | ID: {user['id']}")
    else:
        st.warning("No users found!")

elif page == "Create User":
    st.subheader("Add New User")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Create User"):
        if email and password:
            result = add_user(email, password).json()
            if result.get("success"):
                st.success("User created successfully!")
            else:
                st.error(result.get("Message", "Error creating user"))
        else:
            st.warning("Email and password are required.")

elif page == "Posts":
    st.subheader("All Posts")
    posts = fetch_posts()
    if posts:
        for post in posts[::-1]:  # latest first
            st.markdown("---")
            st.markdown(f"### {post['title']}")
            st.write(post['content'])
            st.caption(f"Author ID: {post['author_id']} | Created at: {post['created_at']}")
            
            # Likes
            likes = fetch_likes(post['id'])
            col1, col2 = st.columns([1,3])
            with col1:
                if st.button(f"❤️ {len(likes)} Like", key=f"like_{post['id']}"):
                    add_like(post['id'], post['author_id'])  # simple demo, author likes own post

            # Comments
            comments = fetch_comments(post['id'])
            with col2:
                st.markdown("**Comments:**")
                for c in comments:
                    st.write(f"💬 {c['content']} (by {c['user_id']})")
                comment_text = st.text_input("Add comment", key=f"comment_{post['id']}")
                if st.button("Comment", key=f"btn_comment_{post['id']}") and comment_text:
                    add_comment(post['id'], post['author_id'], comment_text)
                    st.success("Comment added!")

elif page == "Create Post":
    st.subheader("Create New Post")
    users = fetch_users()
    if not users:
        st.warning("No users found! Please add a user first.")
    else:
        title = st.text_input("Post Title")
        content = st.text_area("Post Content")
        author = st.selectbox("Select Author", options=[u['id'] for u in users], format_func=lambda x: next(u['email'] for u in users if u['id']==x))
        if st.button("Add Post"):
            if title and content:
                result = add_post(title, content, author).json()
                if result.get("success"):
                    st.success("Post added successfully!")
                else:
                    st.error(result.get("Message", "Error adding post"))
            else:
                st.warning("Title and content are required.")

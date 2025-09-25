#src/logic.py
from src.db import *

class UserManager:
    """Manage user-related operations."""

    def __init__(self, db):
        self.db = db

    def add_user(self, email, password):
        """Add a new user to the database."""
        if not email or not password:
            return {"success": False, "Message": "Email and password are required"}
        result = self.db.create_user(email, password)
        if hasattr(result, "user") and result.user:
            return {"success": True, "Message": "User added successfully"}
        else:
            return {"success": False, "Message": "Error creating user"}

    def edit_user(self, user_id, email=None):
        """Update user's email."""
        if not email:
            return {"success": False, "Message": "Email is required for update"}
        self.db.update_user(user_id, email=email)
        return {"success": True, "Message": "User updated successfully"}

    def remove_user(self, user_id):
        """Delete a user by ID."""
        self.db.delete_user(user_id)
        return {"success": True, "Message": "User deleted successfully"}

    def list_users(self):
        """Fetch all users."""
        result = self.db.get_all_users()
        return {"success": True, "Message": "Users fetched successfully", "data": result}

class PostManager:
    """Manage post-related operations."""

    def __init__(self, db):
        self.db = db

    def add_post(self, title, content, author_id):
        """Add a new post."""
        if not title or not content:
            return {"success": False, "Message": "Title and content are required"}
        self.db.create_post(title, content, author_id)
        return {"success": True, "Message": "Post added successfully"}

    def edit_post(self, post_id, title=None, content=None):
        """Update a post's title or content."""
        if not title and not content:
            return {"success": False, "Message": "Title or content required for update"}
        self.db.update_post(post_id, title=title, content=content)
        return {"success": True, "Message": "Post updated successfully"}

    def remove_post(self, post_id):
        """Delete a post by ID."""
        self.db.delete_post(post_id)
        return {"success": True, "Message": "Post deleted successfully"}

    def list_posts(self):
        """Fetch all posts."""
        result = self.db.get_all_posts()
        return {"success": True, "Message": "Posts fetched successfully", "data": result}

    def posts_by_author(self, author_id):
        """Fetch all posts by a specific author."""
        result = self.db.get_posts_by_author(author_id)
        return {"success": True, "Message": "Posts by author fetched successfully", "data": result}

class CommentManager:
    """Manage comment-related operations."""

    def __init__(self, db):
        self.db = db

    def add_comment(self, post_id, user_id, content):
        """Add a comment to a post."""
        if not content:
            return {"success": False, "Message": "Comment content is required"}
        self.db.create_comment(post_id, user_id, content)
        return {"success": True, "Message": "Comment added successfully"}

    def edit_comment(self, comment_id, content):
        """Update a comment's content."""
        if not content:
            return {"success": False, "Message": "Content is required to update comment"}
        self.db.update_comment(comment_id, content)
        return {"success": True, "Message": "Comment updated successfully"}

    def remove_comment(self, comment_id):
        """Delete a comment by ID."""
        self.db.delete_comment(comment_id)
        return {"success": True, "Message": "Comment deleted successfully"}

    def comments_for_post(self, post_id):
        """Fetch all comments for a post."""
        result = self.db.get_comments_by_post(post_id)
        return {"success": True, "Message": "Comments fetched successfully", "data": result}

class LikeManager:
    """Manage like-related operations."""

    def __init__(self, db):
        self.db = db

    def like_a_post(self, post_id, user_id):
        """Like a post."""
        self.db.like_post(post_id, user_id)
        return {"success": True, "Message": "Post liked successfully"}

    def unlike_a_post(self, post_id, user_id):
        """Remove like from a post."""
        self.db.unlike_post(post_id, user_id)
        return {"success": True, "Message": "Like removed successfully"}

    def likes_for_post(self, post_id):
        """Fetch all likes for a post."""
        result = self.db.get_likes_by_post(post_id)
        return {"success": True, "Message": "Likes fetched successfully", "data": result}

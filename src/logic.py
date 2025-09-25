# src/logic.py
import src.db as db

class UserManager:
    def add_user(self, email, password):
        if not email or not password:
            return {"success": False, "Message": "Email and password are required"}
        result = db.create_user(email, password)
        if getattr(result, "user", None):
            return {"success": True, "Message": "User added successfully"}
        else:
            return {"success": False, "Message": "Error creating user"}

    def edit_user(self, user_id, email=None):
        if not email:
            return {"success": False, "Message": "Email is required for update"}
        db.update_user(user_id, email=email)
        return {"success": True, "Message": "User updated successfully"}

    def remove_user(self, user_id):
        db.delete_user(user_id)
        return {"success": True, "Message": "User deleted successfully"}

    def list_users(self):
        result = db.get_all_users()
        return {"success": True, "Message": "Users fetched successfully", "data": result.data}

class PostManager:
    def add_post(self, title, content, author_id):
        if not title or not content:
            return {"success": False, "Message": "Title and content are required"}
        db.create_post(title, content, author_id)
        return {"success": True, "Message": "Post added successfully"}

    def edit_post(self, post_id, title=None, content=None):
        if not title and not content:
            return {"success": False, "Message": "Title or content required for update"}
        db.update_post(post_id, title=title, content=content)
        return {"success": True, "Message": "Post updated successfully"}

    def remove_post(self, post_id):
        db.delete_post(post_id)
        return {"success": True, "Message": "Post deleted successfully"}

    def list_posts(self):
        result = db.get_all_posts()
        return {"success": True, "Message": "Posts fetched successfully", "data": result.data}

    def posts_by_author(self, author_id):
        result = db.get_posts_by_author(author_id)
        return {"success": True, "Message": "Posts by author fetched successfully", "data": result.data}

class CommentManager:
    def add_comment(self, post_id, user_id, content):
        if not content:
            return {"success": False, "Message": "Comment content is required"}
        db.create_comment(post_id, user_id, content)
        return {"success": True, "Message": "Comment added successfully"}

    def edit_comment(self, comment_id, content):
        if not content:
            return {"success": False, "Message": "Content is required to update comment"}
        db.update_comment(comment_id, content)
        return {"success": True, "Message": "Comment updated successfully"}

    def remove_comment(self, comment_id):
        db.delete_comment(comment_id)
        return {"success": True, "Message": "Comment deleted successfully"}

    def comments_for_post(self, post_id):
        result = db.get_comments_by_post(post_id)
        return {"success": True, "Message": "Comments fetched successfully", "data": result.data}

class LikeManager:
    def like_a_post(self, post_id, user_id):
        db.like_post(post_id, user_id)
        return {"success": True, "Message": "Post liked successfully"}

    def unlike_a_post(self, post_id, user_id):
        db.unlike_post(post_id, user_id)
        return {"success": True, "Message": "Like removed successfully"}

    def likes_for_post(self, post_id):
        result = db.get_likes_by_post(post_id)
        return {"success": True, "Message": "Likes fetched successfully", "data": result.data}

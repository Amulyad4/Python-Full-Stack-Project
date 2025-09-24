### Blog Application

A backend-driven blog system that manages users, posts, comments, and likes. Handles user authentication, data storage, retrieval, and CRUD operations for posts. Built with Python and Supabase for a scalable, cloud-based backend.

### Features 

## User Management 
Sign up and log in securely, Passwords stored as hashed values
## Posts
Create, edit, and delete blog posts, View posts by all users, View posts by a particular author
## Comments & Likes (Optional Enhancements)
Users can comment on posts, Users can like posts, Each like is unique per user per post
## Backend-First Design
Fully functional Python backend connected to Supabase, Supports future frontend integration (React, HTML/Bootstrap, etc.)
## Timestamps & Auditing
Track when users, posts, comments, and likes are created or updated

### project structure

BLOG APPLICATION/
|
|___ src/                   # Core application logic 
|   |___db.py              # database operations
|   |___logic.py           # business logic and task
|
|___ api/                   # backend API 
|   |___main.py            # FastAPI endpoints
|
|___ front-end/             # Frontend application
|   |___app.py             # streamlit web interface
|
|___ README.md              # Project documentation
|___ requirements.txt       # Python dependencies 
|
|___ .env                   # python variables


## Quick start

### prerequisites

- python 3.8 or higher
- A supabase account
- Git (push, cloning)

### 1. clone or doenload the project

# option 1 : clone with git 
git clone <repository-url>

# option 2 : Download and extract the zip file

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Set-up Supabase Database
1. create a supabase project
2. create the tasks table
- Go to sql editor in your supabase dashboard
- run the SQL command :
    ```sql
    CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
    );
    ```
3. get your credentials :

### 4. configure environment variables 

1. create a `.env` file in the project root.
2. add your supabase credentials to `.env` :
    SUPABASE_URL=your_project_url_here
    SUPABASE_KEY=your_anon_key_here

### 5.Run the Application

## streamlit frontend
streamlit run front-end/app.py
The app will open in thee browser at `http://localhost:8080`

## FastApi backend
cd api
python main.py

The API will open in thee browser at `http://localhost:8080`

## how to use
## Technical Details

## Technologies used
    - frontend -> streamlit (python web framework)
    - backend  -> FastApi (python rest API framework)
    - database -> supabase (PostgreSQL - based backend-as-a-service)
    - Language -> python 3.8+

### key components

1. **`src/db.py`** : database operation - handles all crud operations with supabase
2. **`src/logic.py`** : buisness logic - task validation and procesing
3. **`api/main.py`** : FastAPI endpoints - backend api
4. **`front-end/app.py`** : streamlit web interface - frontend application

### Trouble Shooting

## Common Issues

1. **"Module not found" error**:
    - Make sure you've installed all dependencies: pip install -r requirements.txt*
    - Check that you're running commands from the correct directory

## Future Enhancements 

Ideas for extending this Project :

- **User Authentication**: Add user accounts and login
- **Task Categories**: Organize tasks by subject or category
- **Notifications**: Email or push notifications for due dates
- **File Attachments**: Attach files to tasks
- **Collaboration**; Share tasks with classmates
- **Mobile App**; React Native or Flutter mobile version
- **Data Export**: Export tasks to CSV or PDF
- **Task Templates**: Create reusable task templates

## support 
If you encounter any issues or have questions : 
contact ->
ph no : +91 7207824196
email : amulya260106@gmail.com
Simple Blog API

A simple and modular blog backend built with Django and Django REST Framework. It provides core blogging features such as user accounts, posts, comments, and categories. This project is suitable for learning REST API development or using as a base for a full-stack blog application.

Features

User Management
Register, manage authentication.

Posts
Create, read, update, and delete blog posts. Each post belongs to a user and a category.

Comments
Add and manage comments on posts. Supports nested relationships with posts and users.

Categories
Organize posts by category for better filtering and structure.

Permissions & Auth
Only authenticated users can create posts or comments. Permissions ensure users can edit only their own content.

Clean, RESTful Endpoints
Built using DRF best practices with serializers, views, and routers.

Tech Stack

Python

Django

Django REST Framework

SQLite (default) 

Project Structure
├── blog/                # Blog app: posts, comments, categories
├── accounts/            # User registration and auth
├── blogapi/             # Main project settings and URLs
├── requirements.txt     
└── README.md

Installation
1. Clone the repository
git clone https://github.com/Mayurgokhale01/Simple-Blog-Api-Using-DRF.git
cd server/blogwebapp

2. Create a virtual environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt

4. Apply migrations
python manage.py migrate

5. Run the server
python manage.py runserver

API Endpoints (Sample)
Users

POST /api/register/

Posts

GET /api/posts/

POST /api/posts/

GET /api/posts/<id>/

PUT /api/posts/<id>/

DELETE /api/posts/<id>/

Comments

GET /api/posts/<id>/comments/

POST /api/posts/<id>/comments/

Categories

GET /api/categories/

POST /api/categories/

How It Works

Users authenticate with tokens or sessions.

Posts and comments are tied to their creators.

Categories help in grouping posts.

DRF serializers handle validations and clean output formatting.

Future Improvements

JWT authentication

Search and filtering

Pagination

Image uploads for posts

Swagger or Redoc documentation

License

Feel free to use or modify this project for learning or personal use.

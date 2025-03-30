# Social Media API

## Overview
The **Social Media API** is a RESTful API built with Django and Django REST Framework (DRF). It allows users to register, authenticate, create posts, comment on posts, and interact with the platform securely.

## Features
- User registration, authentication, and profile management
- CRUD operations for posts and comments
- User permissions and access control
- Pagination and filtering for posts
- API documentation

## Technologies Used
- **Python** (Django, Django REST Framework)
- **SQLite** (default, can be replaced with PostgreSQL or MySQL)
- **JWT Authentication** (via DRF)

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.x
- pip
- Virtualenv (optional but recommended)

### Setup
```bash
# Clone the repository
git clone https://github.com/Amen-Zelealem/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab/social_media_api

# Create and activate virtual environment
python -m venv djenv
source djenv/bin/activate  # On Windows use: djenv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py makemigrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Run the server
python manage.py runserver
```

## API Endpoints

### Authentication
| Method | Endpoint               | Description                 |
|--------|------------------------|-----------------------------|
| POST   | `/api/accounts/register/` | Register a new user        |
| POST   | `/api/accounts/login/`    | Authenticate a user        |
| GET    | `/api/accounts/profile/`  | View user profile         |

### Posts
| Method | Endpoint          | Description                  |
|--------|-------------------|------------------------------|
| GET    | `/api/posts/`      | List all posts               |
| POST   | `/api/posts/`      | Create a new post            |
| GET    | `/api/posts/{id}/` | Retrieve a specific post     |
| PUT    | `/api/posts/{id}/` | Update a post (owner only)   |
| DELETE | `/api/posts/{id}/` | Delete a post (owner only)   |

### Comments
| Method | Endpoint                | Description                        |
|--------|-------------------------|------------------------------------|
| GET    | `/api/comments/`        | List all comments                 |
| POST   | `/api/comments/`        | Add a comment to a post           |
| PUT    | `/api/comments/{id}/`   | Update a comment (owner only)     |
| DELETE | `/api/comments/{id}/`   | Delete a comment (owner only)     |

## Pagination and Filtering
- Posts can be paginated using `?page=1` in the URL.
- Posts can be filtered using `?search=<keyword>`.

## Testing
Use **Postman** or **cURL** to test the API:
# Register a user
```
curl --location 'http://localhost:8000/api/accounts/register/' \
--form 'username="Amen"' \
--form 'password="password123"' \
--form 'bio="Hello, I am a new user."' \
--form 'profile_picture=@"/C:/Users/amenz/Downloads/profile_pictures.jpg"'
```

## Contributing
1. Fork the repository
2. Create a new branch (`feature-branch`)
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## License
This project is licensed under the MIT License.


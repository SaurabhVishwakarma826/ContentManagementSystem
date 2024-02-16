# Django Rest Framework Content Management System

This project is a Django Rest Framework (DRF) implementation of a Content Management System (CMS) with support for multiple user roles, content creation, and search functionality.

## Setup

### Prerequisites

- Python 3.x
- Django
- Django Rest Framework

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/SaurabhVishwakarma826/ContentManagementSystem
    cd ContentManagementSystem
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply database migrations:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Create a superuser for the admin panel:

    ```bash
    python manage.py createsuperuser
    ```

6. Start the development server:

    ```bash
    python manage.py runserver
    ```

## Usage

### Django Admin Panel

1. Access the Django admin panel at `http://127.0.0.1:8000/admin/`.
2. Log in using the superuser credentials created during setup.
3. Use the admin panel to manage users, content, and categories.

### API Endpoints

#### User Registration

- Endpoint: `/api/register/`
- Method: `POST`
- Request Body:

    ```json
    {
        "email": "user@example.com",
        "password": "YourSecurePassword",
        "full_name": "John Doe",
        "phone": "1234567890",
        "address": "123 Main St",
        "city": "City",
        "state": "State",
        "country": "Country",
        "pincode": "123456"
    }
    ```

#### User Login

- Endpoint: `/api/login/`
- Method: `POST`
- Request Body:

    ```json
    {
        "username": "user@example.com",
        "password": "YourSecurePassword"
    }
    ```

#### Create Content

- Endpoint: `/api/content/create/`
- Method: `POST`
- Request Body:

    ```json
    {
        "title": "Sample Title",
        "body": "This is the content body.",
        "summary": "A brief summary",
        "document": null,
        "categories": [1] # spacify the category id
    }
    ```

#### List All Content

- Endpoint: `/api/content/list/`
- Method: `GET`

#### Content Detail

- Endpoint: `/api/content/detail/<int:pk>/`
- Methods: `GET`, `PUT`, `DELETE`

#### Search Content

- Endpoint: `/api/content/search/`
- Method: `GET`
- Query Parameter: `search_param`

    Example: `/api/content/search/?search_param=Django`

#### Admin View All Content

- Endpoint: `/api/admin/content/all/`
- Method: `GET`
- Permission: Admin user

#### Admin Edit or Delete Content

- Endpoint: `/api/admin/content/edit/<int:pk>/`
- Methods: `PUT`, `DELETE`
- Permission: Admin user

## Customization

Feel free to customize this project based on your specific requirements. Explore Django Rest Framework's capabilities for additional features and extensions.


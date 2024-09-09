# DRF CRUD Project

This project is built using **Django REST Framework (DRF)** to perform basic CRUD (Create, Read, Update, Delete) operations along with user authentication using tokens. It provides a RESTful API for managing resources such as creating new data, retrieving it, updating it, and deleting it. Token-based authentication is implemented to ensure that users must be authenticated to perform certain actions like creating and modifying data.

## Features

- **CRUD Operations**:
  - Create: Add new records via POST requests.
  - Read: Fetch records using GET requests.
  - Update: Modify existing records with PUT or PATCH requests.
  - Delete: Remove records via DELETE requests.
  
- **Token-based Authentication**:
  - Users can login by sending their credentials and receive a token.
  - Only authenticated users can create, update, or delete data.
  
- **Endpoints**:
  - `POST /login/`: Authenticate user and return token.
  - `POST /resources/`: Create a new resource.
  - `GET /resources/`: Retrieve a list of resources.
  - `GET /resources/<id>/`: Retrieve a single resource.
  - `PATCH /resources/<id>/`: Partially update a resource.
  - `PUT /resources/<id>/`: Fully update a resource.
  - `DELETE /resources/<id>/`: Delete a resource.

## Technologies Used

- **Django**: Web framework for the backend.
- **Django REST Framework**: Toolkit for building Web APIs in Django.
- **SQLite (or your choice of DB)**: Database for storing data.
- **Token Authentication**: For securing endpoints using DRF’s TokenAuthentication.

## Setup and Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/DRF_CRUD.git
    cd DRF_CRUD
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:
        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Apply database migrations:
    ```bash
    python manage.py migrate
    ```

6. Create a superuser (admin):
    ```bash
    python manage.py createsuperuser
    ```

7. Run the development server:
    ```bash
    python manage.py runserver
    ```

8. Access the application:

    Open `http://127.0.0.1:8000/` in your browser.

## Contributing

Contributions are welcome. Please:

1. Fork the repository.
2. Create a new branch.
3. Make changes.
4. Commit changes.
5. Push to your fork.
6. Create a pull request.

<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>

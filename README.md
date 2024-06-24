# **Select Language:** 🌍
- [Español (Spanish)](README-es.md)
- [English](README.md)

# Flask User, Post, and Category Management

This Flask project provides an API for managing users, posts, and categories, following a layered architecture approach.

## RESULTS
## REST CONSUMER
### Insomia Flask
![Alt text](api_docs/docs.PNG)
![Alt text](api_docs/insomia_flask.PNG)

## Features

- **Users**: Create, retrieve, update, and delete user profiles.
- **Posts**: Create, retrieve, update, and delete posts.
- **Categories**: Create, retrieve, update, and delete categories.

## Requirements

- Python 3.8+
- Flask
- Flask-CORS

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Anyel-ec/Flask-Py-RestAPI-RedSocial-One
    cd Flask-Py-RestAPI-RedSocial-One
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up and initialize the database:
    ```sh
    # Add instructions for database initialization if applicable
    ```

5. Run the development server:
    ```sh
    python app.py
    ```

## Architecture

This project follows a layered architecture:

1. **Controllers**: Handle HTTP requests and responses.
2. **Services**: Implement business logic and application rules.
3. **Repositories**: Manage data access and persistence.

## Main Endpoints

### Users

- `POST /api/users/`: Create a new user.
- `GET /api/users/<user_id>`: Retrieve a specific user.
- `GET /api/users/`: Retrieve all users.
- `PUT /api/users/<user_id>`: Update a specific user.
- `DELETE /api/users/<user_id>`: Delete a specific user.
- `POST /api/users/<user_id>/verify`: Verify user password.
- `POST /api/users/verify`: Verify login credentials.

### Posts

- `POST /api/posts/`: Create a new post.
- `GET /api/posts/<post_id>`: Retrieve a specific post.
- `GET /api/posts/`: Retrieve all posts.
- `PUT /api/posts/<post_id>`: Update a specific post.
- `DELETE /api/posts/<post_id>`: Delete a specific post.
- `GET /api/posts/by_user/<user_id>`: Retrieve posts by user.
- `GET /api/posts/by_email/<email>`: Retrieve posts by user email.

### Categories

- `POST /api/categories/`: Create a new category.
- `GET /api/categories/<category_id>`: Retrieve a specific category.
- `GET /api/categories/`: Retrieve all categories.
- `PUT /api/categories/<category_id>`: Update a specific category.
- `DELETE /api/categories/<category_id>`: Delete a specific category.

## Usage

To test the API, use tools like Postman or `curl` to make HTTP requests to the endpoints mentioned above.

## Insomnia JSON

For easier testing, import the provided Insomnia JSON file `insomnia_export.json` into Insomnia. This file contains pre-configured requests for all endpoints mentioned above.

## Contributions

Contributions are welcome! Follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes and commit (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
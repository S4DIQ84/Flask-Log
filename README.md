# Flask Login and Signup Application

This Flask application provides basic user authentication functionalities such as login, signup, and logout. User data is stored temporarily in a JSON file named `db.json`.

## Features

- **Login:** Users can log in with their username and password.
- **Signup:** New users can sign up by providing their email, username, and password.
- **Logout:** Users can log out of their session.

## Usage

1. Clone the repository:

    ```bash
    git clone <repository-url>
    ```

2. Navigate to the project directory:

    ```bash
    cd <project-directory>
    ```

3. Install dependencies:

    ```bash
    pip install Flask
    ```

4. Run the application:

    ```bash
    python app.py
    ```

5. Access the application in your web browser at `http://localhost:5000`.

## Files

- **app.py:** Contains the Flask application code.
- **template/login.html:** HTML template for the login page.
- **template/signup.html:** HTML template for the signup page.
- **template/index.html:** HTML template for the index page.
- **db.json:** JSON file used as a temporary database to store user information.

## Notes

- This application is intended for educational and demonstration purposes and should not be used in production without implementing proper security measures.
- The `db.json` file serves as a temporary database. For production use, consider using a more robust database solution.
- Ensure to handle sensitive user information securely and implement additional security measures such as password hashing and session management before deploying to a production environment.


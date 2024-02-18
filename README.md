# Django Notes API

A simple API for managing notes built with Django and Django REST framework.

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/django-notes-api.git
   cd django-notes-api
Create a virtual environment:

bash
Copy code
python -m venv venv
Activate the virtual environment:

On Windows:

bash

.\venv\Scripts\activate
On Unix or MacOS:

bash
Copy code
source venv/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Apply migrations:

bash
Copy code
python manage.py migrate
Run the development server:

bash
Copy code
python manage.py runserver
The API should be accessible at http://127.0.0.1:8000/

API Endpoints
User Registration
Endpoint: POST /api/signup
Functionality: Allows users to create an account by providing necessary information such as username, email, and password.
Output: If the registration is successful, return a success message or status code. If there are validation errors or the username/email is already taken, return appropriate error messages or status codes.
User Login
Endpoint: POST /api/login
Functionality: Allows users to log in to their account by providing their credentials (username/email and password).
Output: If the login is successful, return an authentication token or a success message with the user details. If the credentials are invalid, return an error message or status code.
Create New Note
Endpoint: POST /api/notes/create
Functionality: Create a new note, only authenticated users can create a new note.
Note: note owner needs to be stored in the db. Because notes are shareable.
Output: If the request is valid, return a success message with status code. If the request is invalid, return an error message or status code.
Get a Note
Endpoint: GET /api/notes/{id}
Functionality: GET a note by its id. Only authenticated users. A note is viewable by its owner and the shared users only.
Output: If the request is valid, return a success message with the note content. If the request is invalid, return an error message with status code.
Share a Note
Endpoint: POST /api/notes/share
Functionality: Share a note with other users. You can parse multiple users in this request. Once the note admin executes this POST api, the users embedded in the request body will be able to view and edit the note.
Output: If the request is valid, return a success message with the appropriate status code. If the request is invalid, return an error message or status code.
Update a Note
Endpoint: PUT /api/notes/{id}
Functionality: The note will be editable by admin, and all the shared users. All the users who have access to the note will be able to perform an edit anywhere on the note. For the sake of simplicity, let’s assume no existing sentences can be edited. But new sentences can be added in between existing lines of the note. All the updates to the notes need to be tracked with a timestamp, and stored somewhere.
Output: If the request is valid, return a success message with the appropriate status code. If the request is invalid, return an error message or status code.
Get Note Version History
Endpoint: GET /api/notes/version-history/{id}
Functionality: Accessible by users having access only. GET the version history of the note. This includes all the changes made to the note, since it has been created. The response will contain a list of timestamp, user who made the change, and the changes made to the note since its creation. If possible you can track the line number of change as well.
Output: If the request is valid, return the response with the appropriate status code. If the request is invalid, return an error message or status code.
Contributing
Feel free to contribute to this project by opening issues or pull requests.

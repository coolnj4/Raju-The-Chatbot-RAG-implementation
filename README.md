# Raju - THE CHATBOT (based on RAG implementation)
An LLM based python app that let you upload your own pdf documents and then ask questions related to it. Along with Working authencation System.

## Dependencies and Installation
----------------------------
To install this on your system please follow these steps:

1. Clone the repository to your local machine.

2. Make a virtual environment using and activate it by running actvate.exe under testenv/scripts
   ```
   python -m venv myenv
   ```

3. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

4. Go to settings.py file and change your database credentials to your database.
    
    NOTE:

        You need to create a online database which is online before your start django server.

        Pro tip : Use Databases from websites like Render.com for quick view

    You need to change following :

    ```
    DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",      #your database engine
        "NAME": "minor_project",        #your database name
        "USER": "",   #your database user
        "PASSWORD": "",     #your database password
        "HOST": "",     #your database host
        "PORT": "",     #your database port
    }
    ```

5. Apply migrations to django using following command
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Obtain an API key from OpenAI and add it to the `.env` file in the project directory.

5. Before Starting django server make sure that Database is up and running

6. Navigate to djangobackend folder and run django server using following command

   ```
   python manage.py runserver
   ```

7. Navigate to streamlit folder and run streamlit app on new terminal using following command
   ```
   streamlit run main.py
   ```

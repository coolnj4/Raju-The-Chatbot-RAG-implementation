# MINER - THE CHATBOT
An LLM based python app that let you upload your own pdf documents and then ask questions related to it. Along with Working authencation System.

## Dependencies and Installation
----------------------------
To install this on your system please follow these steps:

1. Clone the repository to your local machine.

2. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

3. Obtain an API key from OpenAI and add it to the `.env` file in the project directory.
```commandline
OPENAI_API_KEY=your_secrit_api_key
```

4. Start your database server and configure it in settings.py file in Database Section

5. Before Starting django server make sure that Database is up and running

6. run django server using following command

   ```
   phython manage.py runserver
   ```

7. run streamlit app on new terminal using following command
 ```
   streamlit run main.py
   ```

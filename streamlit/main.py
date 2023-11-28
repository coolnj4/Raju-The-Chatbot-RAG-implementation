import streamlit as st 
import requests 
import time 
from dotenv import load_dotenv
from htmltemplates import css, bot_template, user_template , foot , footer_fix

from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.llms import HuggingFaceHub
from content import file_content


def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
            #text streaming
            full_response = ""
            message_placeholder = st.empty()
            for chunk in message.content.split():
                full_response += chunk + " "
                time.sleep(0.05)
                # Add a blinking cursor to simulate typing
                message_placeholder.markdown(bot_template.replace("{{MSG}}", full_response + "▌"), unsafe_allow_html=True)
            message_placeholder.markdown(bot_template.replace("{{MSG}}", full_response), unsafe_allow_html=True)

def final():

            st.write(css, unsafe_allow_html=True)

            if "conversation" not in st.session_state:
                st.session_state.conversation = None
            if "chat_history" not in st.session_state:
                st.session_state.chat_history = None
            
            st.header("Noticed! you have a query? Ask me")
            user_question = st.text_input("Ask a question about your documents:")
            if user_question:
                handle_userinput(user_question)
                text = file_content

                text_chunks = text_to_chunk(text)

                vectorstore = get_vectorstore(text_chunks)

                st.session_state.conversation = conversation_chain(vectorstore)

            
            pdf_docs = st.file_uploader(
                "Upload your PDFs here and click on 'Process'", accept_multiple_files=True)
            if st.button("Process"):
                with st.spinner("Processing"):

                    # get pdf text
                    raw_text = pdf_to_text(pdf_docs)

                    # get the text chunks
                    text_chunks = text_to_chunk(raw_text)

                    # create vector store
                    vectorstore = get_vectorstore(text_chunks)

                    # create conversation chain
                    st.session_state.conversation = conversation_chain(vectorstore)



def pdf_to_text(pdf_docs):


    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()

            
    return text


def text_to_chunk(text):
    if text == "":
        text =text + file_content
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks


def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    # embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore


def conversation_chain(vectorstore):
    llm = ChatOpenAI()
    # llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.5, "max_length":512})

    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain




def login_page(applicant_token):
    st.markdown(foot, unsafe_allow_html=True)
    
    # Add custom CSS for footer
    st.markdown(footer_fix, unsafe_allow_html=True,)

    if(applicant_token):
        st.warning('Login Successful', icon="🥳")
        
        final()

    else:
        with st.form("my_form" , clear_on_submit=True): 
            st.header('Please Login')           
            email = st.text_input(label ='Email')
            password = st.text_input(label ='Password', type="password")
            submit_res = st.form_submit_button(label='Login')

            if submit_res:
                headers = {"Content-Type": "application/json; charset=utf-8"}
                response = requests.post('http://127.0.0.1:8000/api/accounts/api_auth/',
                  headers=headers, json={"email":email,"password":password})

                response_json = response.json()

                if response.status_code == 200:
                    applicant_token = response_json["token"]
                    

                    if applicant_token:
                       st.session_state.key = 'applicant-token'
                       st.session_state['applicant-token'] = applicant_token
                       st.experimental_rerun()

def register(applicant_token):
    st.markdown(foot, unsafe_allow_html=True)
    
    # Add custom CSS for footer
    st.markdown(footer_fix, unsafe_allow_html=True,)

    if applicant_token:
        with st.form("my_form" , clear_on_submit=True):
                    st.header('Please Register')  
                    st.write("You need to first logout before registering!")
                    submit_res = st.form_submit_button(label='Logout here') 
            
                    if submit_res:
                        st.write("You are now logged out!")
                        del st.session_state['applicant-token']
                        time.sleep(3)
                        st.experimental_rerun()

    else:
        with st.form("my_form"):
            st.header('Are you sure you want to Logout')  
            email = st.text_input(label ='email')
            username = st.text_input(label='username')
            password = st.text_input(label ='password', type="password")
            submit_res = st.form_submit_button(label='Register')

            if submit_res:    
                st.write("registered clicked!")
                headers = {"Content-Type": "application/json; charset=utf-8"}
                response = requests.post('http://127.0.0.1:8000/api/accounts/api_register/',
                  headers=headers, json={"email":email, "username": username,"password":password})

                if response.status_code == 200:
                    st.experimental_rerun()


def log_out(applicant_token):    
    st.markdown(foot, unsafe_allow_html=True)
    
    # Add custom CSS for footer
    st.markdown(footer_fix, unsafe_allow_html=True,)

    if applicant_token:        
            with st.form("my_form",clear_on_submit=True):
                st.write("Do you want to log out?")
                submit_res = st.form_submit_button(label='Logout here') 
        
                if submit_res:
                    if 'applicant-token' in st.session_state:
                        del st.session_state['applicant-token']
                    st.warning('LogOut Successful', icon="🥳")
                    st.experimental_rerun()

    else:
        st.warning('LogOut Successful', icon="🥳")

               

def load_view():
    
    st.sidebar.header("How would you like to be contacted?")
    add_selectbox = st.sidebar.selectbox('*',
    ("Login", "Register","Log out")
    )

    applicant_token =''


    if 'applicant-token' in st.session_state:
        
        applicant_token = st.session_state['applicant-token']


    if add_selectbox == 'Login':
        
        login_page(applicant_token=applicant_token) 
        

    elif add_selectbox == 'Register':

        register(applicant_token=applicant_token)

    elif add_selectbox == 'Log out':

        log_out(applicant_token=applicant_token)



if __name__ == '__main__':
    load_view()
    load_dotenv()




   
        

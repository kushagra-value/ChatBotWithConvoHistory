# import streamlit as st
# from langchain_openai import ChatOpenAI
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.prompts import ChatPromptTemplate

# # Prompt Template
# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", "You are a helpful assistant. Please respond to the user queries."),
#         ("user", "Question:{question}")
#     ]
# )

# def generate_response(question, api_key, engine, temperature, max_tokens):
#     try:
#         # Create a new instance of ChatOpenAI for each request
#         llm = ChatOpenAI(model=engine, temperature=temperature, max_tokens=max_tokens, openai_api_key=api_key)
#         output_parser = StrOutputParser()
#         chain = prompt | llm | output_parser
#         answer = chain.invoke({'question': question})
#         return answer
#     except Exception as e:
#         error_message = str(e)
#         if "Error code: 401" in error_message and "invalid_api_key" in error_message:
#             return "Invalid API Key. Please check your API Key and try again."
#         else:
#             return f"An error occurred: {error_message}"

# # Title of the app
# st.title("Enhanced Q&A Chatbot With OpenAI")

# # Sidebar for settings
# st.sidebar.title("Settings")
# api_key = st.sidebar.text_input("Enter your OpenAI API Key:", type="password")

# # Select the OpenAI model
# engine = st.sidebar.selectbox("Select OpenAI model", ["gpt-3.5-turbo"])

# # Adjust response parameters
# temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
# max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

# # Main interface for user input
# st.write("Go ahead and ask any question")
# user_input = st.text_input("You:")

# if user_input and api_key:
#     response = generate_response(user_input, api_key, engine, temperature, max_tokens)
#     st.write(response)
# elif user_input:
#     st.warning("Please enter the OpenAI API Key in the sidebar.")
# else:
#     st.write("Please provide the user input.")

import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries."),
        ("user", "Question:{question}")
    ]
)

def generate_response(question, api_key, engine, temperature, max_tokens):
    try:
        # Create a new instance of ChatOpenAI for each request
        llm = ChatOpenAI(model=engine, temperature=temperature, max_tokens=max_tokens, openai_api_key=api_key)
        output_parser = StrOutputParser()
        chain = prompt | llm | output_parser
        answer = chain.invoke({'question': question})
        return answer
    except Exception as e:
        error_message = str(e)
        if "Error code: 401" in error_message and "invalid_api_key" in error_message:
            return "Invalid API Key. Please check your API Key and try again."
        else:
            return f"An error occurred: {error_message}"

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Title of the app
st.title("Open AI chatbot with Conversational History")

# Sidebar for settings
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your OpenAI API Key:", type="password")

# Select the OpenAI model
engine = st.sidebar.selectbox("Select OpenAI model", ["gpt-3.5-turbo"])

# Adjust response parameters
# temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
temperature = 1.0
max_tokens = 200
# max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

# Main interface for user input
st.write("Go ahead and ask any question")
user_input = st.text_input("You:")

if user_input and api_key:
    response = generate_response(user_input, api_key, engine, temperature, max_tokens)
    
    # Update chat history
    st.session_state.chat_history.append({"user": user_input, "bot": response})
    
    # Display the response
    st.write(response)
elif user_input:
    st.warning("Please enter the OpenAI API Key in the sidebar.")
else:
    st.write("Please provide the user input.")

# Display chat history in a separate sidebar
st.sidebar.title("Chat History")
for i, chat in enumerate(st.session_state.chat_history):
    st.sidebar.write(f"**Q{i+1}:** {chat['user']}")
    st.sidebar.write(f"**A{i+1}:** {chat['bot']}")
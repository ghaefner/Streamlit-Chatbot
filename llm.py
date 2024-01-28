# Importing necessary modules
from langchain.llms import OpenAI, HuggingFaceHub  # Importing LLM classes from langchain.llms module
from langchain.memory import StreamlitChatMessageHistory, ConversationBufferMemory  # Importing memory-related classes
from langchain.chains import ConversationChain, LLMChain, ConversationalRetrievalChain  # Importing chain-related classes
from langchain.prompts import PromptTemplate  # Importing PromptTemplate class
from prompt import create_template  # Importing create_template function

# Initializing chat message history using StreamlitChatMessageHistory class
history = StreamlitChatMessageHistory(key='messages')
# Creating conversation memory using ConversationBufferMemory class
memory = ConversationBufferMemory(chat_memory=history)

# Function to get LLM (Language Model) instance based on the provided parameters
def get_llm(model_type, temperature, max_length=64):
    # Constructing model arguments dictionary
    model_arguments = {"temperature": temperature, "max_length": max_length}

    # Instantiating different LLM based on the provided model_type
    if model_type == 'gpt-3.5':
        llm = OpenAI(temperature=temperature, max_tokens=max_length)
    elif model_type == 'flan-t5-xxl':
        llm = HuggingFaceHub(repo_id='google/flan-t5-xxl', model_kwargs=model_arguments)
    elif model_type == 'flan-t5-base':
        llm = HuggingFaceHub(repo_id='google/flan-t5-base', model_kwargs=model_arguments)
    elif model_type == 'Llama-2-7b':
        llm = HuggingFaceHub(repo_id='meta-llama/Llama-2-7b', model_kwargs=model_arguments)
    elif model_type == 'gte-large':
        llm = HuggingFaceHub(repo_id="thenlper/gte-large", model_kwargs=model_arguments)

    # Creating an LLMChain instance with the generated LLM and a prompt template
    chain = LLMChain(llm=llm, prompt=create_template())

    return chain  # Returning the constructed chain

# Function to create a ConversationalRetrievalChain
def get_chain(retriever, chat_history):
    # Creating memory using ConversationBufferMemory with the provided chat_history
    memory = ConversationBufferMemory(chat_memory=chat_history, memory_key="chat_history", return_messages=True)
    # Instantiating OpenAI LLM
    llm = OpenAI()
    # Creating a ConversationalRetrievalChain instance using the OpenAI LLM, provided retriever, and memory
    chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=retriever, memory=memory)
    
    return chain  # Returning the constructed chain

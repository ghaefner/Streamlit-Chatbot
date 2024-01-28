import streamlit as st
from llm import get_llm, memory, history
from dotenv import load_dotenv
from prompt import get_prompt, get_roles
from langchain.tools import DuckDuckGoSearchRun
from langchain.agents import initialize_agent, AgentType
from langchain.callbacks import StreamlitCallbackHandler

load_dotenv()

"""
# Chat with AI
"""

# Sidebar selection
with st.sidebar:
    model_select = st.selectbox("Model Selection:", ['flan-t5-xxl', 'gpt-3.5','flan-t5-base', 'Llama-2-7b', 'gte-large'])
    temperature_slider = st.slider("Select Temperature:", min_value=0.1, max_value=1.5, value=0.7, step=0.1)
    max_length_slider = st.select_slider("Slect Max Number of Tokens:", options=[4,8,16,32,64,128], value=64)
    role_select = st.selectbox("Role Selection:", options=get_roles() )

    files_select = st.file_uploader(
        label = 'Upload files'
    )

# My Comment
for message in history.messages:
    msgtype = 'user' if message.type == 'human' else 'assistant'
    st.chat_message(msgtype).write(message.content)

if user_input := st.chat_input():

    # Handle user input
    st.chat_message('user').write(user_input)

    # Handle AI response
    llm = get_llm(model_select,temperature=temperature_slider,max_length=max_length_slider)
    role_val = get_prompt(role_val=role_select)
    
    # Define Search agent
    search = DuckDuckGoSearchRun(name="Search")
    search_agent = initialize_agent([search], llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, handle_parsing_errors=True)
    
    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        response = search_agent.run(st.session_state.messages, callbacks=[st_cb])
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.write(response)
    
    #response = llm.run({
     #   'query': user_input,
      #  'role':role_val,
        #'chat_history': memory
       # })
    #st.chat_message('assistant').write(response)
# Streamlit AI Chat Application

This Streamlit application allows users to engage in conversations with AI models. It provides a user-friendly interface for selecting different AI models, adjusting parameters such as temperature and max length, and specifying a role for generating prompts.

## Features

- **Model Selection**: Users can choose from various AI models, including 'flan-t5-xxl', 'gpt-3.5', 'flan-t5-base', 'Llama-2-7b', and 'gte-large'.
- **Temperature Control**: Users can adjust the temperature parameter of the selected AI model using a slider.
- **Max Length Setting**: Users can specify the maximum number of tokens for AI responses using a slider.
- **Role Selection**: Users can select a role from predefined options to customize prompts for the AI model.
- **File Uploader**: Users can upload files, although the functionality is not directly used in the current version of the application.

## Components

- **User Interface**: The main interface is constructed using Streamlit, providing a sidebar for model selection and parameter adjustment.
- **Message History Display**: The application displays chat messages from the chat history, distinguishing between user and assistant messages.
- **User Input Handling**: User input is collected using a chat input component and displayed in the chat interface.
- **AI Response Handling**: The application interacts with AI models to generate responses based on user input and selected parameters.
- **Search Agent Integration**: It includes a search agent (DuckDuckGoSearchRun) for providing relevant information based on user queries.
- **Callback Handling**: StreamlitCallbackHandler is used to manage callbacks for updating the UI with AI responses.

## Usage

To run the application, ensure you have the required dependencies installed, then execute the script. Users can interact with the application through the Streamlit interface, selecting models, adjusting parameters, and engaging in conversations with the AI model.

## Dependencies

- Streamlit: For creating interactive web applications in Python.
- Dotenv: For loading environment variables from a .env file.
- Langchain (Custom library): Provides modules for language model interactions, tools, agents, and callbacks.
- Prompt2: Contains functions for generating prompts based on roles.
- Langchain.tools: Includes tools for performing specific tasks like searching.

## File Structure

- `app.py`: Main script containing the Streamlit application code.
- `llm.py`: Contains functions for initializing LLM (Language Model) instances.
- `prompt2.py`: Provides functions for retrieving prompts based on roles.
- `langchain/tools.py`: Implements various tools used in the application.
- `langchain/agents.py`: Defines agents for interacting with AI models.
- `langchain/callbacks.py`: Handles callbacks for UI updates.

## Note

- This application serves as a demonstration of integrating AI models into a Streamlit interface. It can be further extended with additional features and improvements.
- Ensure that appropriate environment variables are set up for accessing AI models and other resources.

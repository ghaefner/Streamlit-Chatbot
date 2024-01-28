# Importing necessary modules
from langchain.prompts import PromptTemplate 
import pandas as pd 

# Function to retrieve the prompt based on the provided role value
def get_prompt(role_val=None):
    # Reading the CSV file containing prompts and storing it in a DataFrame
    df_roles = pd.read_csv("./Input/prompts_business.csv", delimiter=";")

    try:
        # Filtering the DataFrame based on the provided role value and extracting the prompt values
        prompt_val_list = df_roles[df_roles['Role'] == role_val]['Prompt'].tolist()
        # Joining the prompt values into a single string
        prompt_val = '\n'.join(prompt_val_list)
        return prompt_val  # Returning the combined prompt string
    except TypeError:
        return ""  # Returning an empty string if an error occurs

# Function to retrieve the list of roles from the specified CSV file
def get_roles(path_to_file="./Input/prompts_business.csv"):
    # Reading the CSV file containing roles and storing it in a DataFrame
    df_roles = pd.read_csv(path_to_file, delimiter=";")
    # Extracting the 'Role' column values and converting them to a list
    return df_roles['Role'].tolist()  # Returning the list of roles

# Function to create a prompt template for generating prompts
def create_template():
    # Template string containing placeholders for 'role' and 'query'
    template = """ 
    {role}. 
    
    Answer the question based on the role mentioned above. If you cannot answer the question with the 
    information available to you, simply reply "I do not know." instead of coming up with an answer.

    Question: {query}
    """
    
    # Creating a PromptTemplate object with input variables 'query' and 'role', using the template string
    prompt_template = PromptTemplate(
        input_variables=["query", "role"],
        template=template
    )

    return prompt_template  # Returning the created prompt template object

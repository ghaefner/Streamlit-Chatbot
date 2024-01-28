from langchain.prompts import PromptTemplate
import pandas as pd

def get_prompt(role_val=None):
    df_roles = pd.read_csv("./Input/prompts_business.csv", delimiter=";")

    try:
        prompt_val_list = df_roles[df_roles['Role'] == role_val]['Prompt'].tolist()
        prompt_val = '\n'.join(prompt_val_list)
        return prompt_val
    except TypeError:
        return ""

def get_roles(path_to_file = "./Input/prompts_business.csv"):
    df_roles = pd.read_csv(path_to_file, delimiter=";")
    return df_roles['Role'].tolist()
        
def create_template():
    template = """ 
    You are a chatbot having a conversation with a human.

    {chat_history}

    Human: {role} 
    
    Answer the question based on the role mentioned above. If you cannot answer the question with the 
    information available to you, simply reply "I do not know." instead of coming up with an answer.

    Question: {query}

    Chatbot: 
    """

    prompt_template = PromptTemplate(
        input_variables=["query", "role", "chat_history"],
        template=template
    )

    return prompt_template
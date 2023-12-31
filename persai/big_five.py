"""
1. define prompt
2. call data cleaner file and get returned new prompt
3. call openai model 
4. do response extracting step if necessary and return dict in right format
"""
import x_data_cleaner
import open_ai
import json

#todo find out level needed here 
def big_five(data_path):
    prompt_content = get_prompt_content(data_path)

    result = get_result()
    extracted_result = extract_result()
    return extracted_result

def get_prompt(text):
    return f"""
    Analyze the person-generated text from [Specified Level], determine the person’s levels of Openness, Conscientiousness, Extraversion, Agreeableness, and Neuroticism. Only return Low or High.

    Text:
    {text}

    Level: Let’s think step by step:
    """

def get_prompt_content():
    """
    returns content which can be inserted into prompt
    """
    get_prompt_content = x_data_cleaner("path to data")
    return get_prompt_content

def get_result():
    """
    sends request to openai and gets the result of personality analysis
    """
    pass

def extract_result():
    """
    extracts result and returns dictionary
    """
    pass
"""
1. define prompt
2. call data cleaner file and get returned new prompt
3. call openai model 
4. do response extracting step if necessary and return dict in right format
"""
import logging
from . import x_data_cleaner
from . import open_ai

# Set up logging
logging.basicConfig(level=logging.INFO)

def main_big_five(data_path):
    print(data_path)
    logging.info("Starting main_big_five function.")
    logging.info("Getting prompt content.")
    prompt_content = get_prompt_content(data_path)
    logging.info("Generating prompt.")
    prompt = get_prompt(prompt_content)
    logging.info("Creating messages.")
    messages = get_messages(prompt)
    logging.info("Getting result from LLM.")
    result = get_result(messages)
    logging.info("Extracting result.")
    extracted_result = extract_result(result)    
    logging.info("Finished main_big_five function.")
    return extracted_result

def get_prompt(text):
    return f"""
    Analyze the person-generated text from sentence level, determine the person’s levels of Openness, Conscientiousness, Extraversion, Agreeableness, and Neuroticism. Only return Low or High.

    Text:
    {text}

    Level: Let’s think step by step:
    """

def get_messages(prompt):
    """
    creates the messages which is than used for the request to openai 
    """
    messages=[
        {"role": "system", "content": "You are a psychologist who is given some tweets, and based on those tweets, you make a Big Five personality analysis."},
        {"role": "user", "content": prompt}
    ]
    return messages

def get_prompt_content(data_path):
    """
    returns content which can be inserted into prompt
    """
    get_prompt_content = x_data_cleaner.main_x_data_cleaner(data_path)
    return get_prompt_content

def get_result(prompt):
    """
    sends request to openai and gets the result of personality analysis
    """
    result = open_ai.main_openai(prompt)
    return result

def extract_result(result):
    """
    extracts result and returns dictionary
    """
    prompt ="""You are receiving a text as input that contains a personality analysis of an individual. The analysis is based on the Big Five personality traits, which include openness, conscientiousness, extraversion, agreeableness, and neuroticism. Please extract the analysis results in the following format: {"openness": "low", "conscientiousness": "high", "extraversion": "low", "agreeableness": "high", "neuroticism": "low"}."""
    messages = [{"role": "user", "content": prompt}, {"role": "user", "content": result}]
    result = open_ai.main_openai(messages)
    return result

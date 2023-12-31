import json

def main_x_data_cleaner(path_to_data, prompt):
    """
    main
    """
    valid_json_objects = load_json_objects(path_to_data)
    filtered_json_objects = filter_entities(valid_json_objects)
    full_prompt = generate_full_prompt(filtered_json_objects, prompt)
    return filtered_json_objects

# load all json objects which are not broken into a list
def load_json_objects(filename):
    """
    takes the path to the js file containing the twitter data and returns a list of json objects
    """
    valid_objects = []
    decoder = json.JSONDecoder()
    with open(filename, 'r') as f:
        text = f.read()
        pos = 0
        while pos < len(text):
            try:
                obj, pos = decoder.raw_decode(text, pos)
                valid_objects.append(obj)
            except json.JSONDecodeError:
                # Find the next position where { starts
                next_pos = text.find('{', pos)
                if next_pos == -1:
                    break
                pos = next_pos
    return valid_objects

#get all posts with no entities
def filter_entities(json_objects):
    return [obj for obj in json_objects if all(not obj['tweet']['entities'][key] for key in obj['tweet']['entities'])]

def generate_full_prompt(filtered_json_objects, prompt):
    """
    generates full prompt with which request can be send than to openai

    




    Analyze the person-generated text from [Specified Level], determine the person’s levels of Openness, Conscientiousness, Extraversion, Agreeableness, and Neuroticism. Only return Low or High.

Text:
{---
tweet
---

---
tweet
---

---
tweet
---}

Level: Let’s think step by step:
    """
    full_prompt = prompt
    for obj in filtered_json_objects:
        full_prompt += f"""
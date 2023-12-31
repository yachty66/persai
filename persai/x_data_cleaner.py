import json

def main_x_data_cleaner(path_to_data):
    """
    The main function returns 20 posts in a formatted prompt.
    """
    valid_json_objects = load_json_objects(path_to_data)
    filtered_json_objects = filter_entities(valid_json_objects)
    full_text_objects = get_full_text_objects(filtered_json_objects)
    full_prompt_content = generate_full_prompt(full_text_objects)
    return full_prompt_content

def load_json_objects(filename):
    """
    Takes the path to the JavaScript file containing the Twitter data and returns a list of JSON objects.
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

def filter_entities(json_objects):
    """
    Get all posts with no entities, i.e. only posts that are purely from users.
    """
    return [obj for obj in json_objects if all(not obj['tweet']['entities'][key] for key in obj['tweet']['entities'])]

def get_full_text_objects(filtered_json_objects):
    """
    gets the full text of the tweets
    """
    full_text = []
    for i in range(len(filtered_json_objects)):
        full_text.append(filtered_json_objects[i]['tweet']['full_text'])
    return full_text

def generate_full_prompt(full_text_objects):
    """
    Generates a full prompt with which a request can be sent to OpenAI.
    """
    big_string = ""
    for i in range(20):
        big_string += "---\n" + full_text_objects[i] + "\n---\n"
    return big_string
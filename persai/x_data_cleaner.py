import json

def main_x_data_cleaner(path_to_data):
    """
    main which returns 20 posts in prompt format
    """
    print("Starting main_x_data_cleaner function.")
    valid_json_objects = load_json_objects(path_to_data)
    print("Loaded valid JSON objects.")
    filtered_json_objects = filter_entities(valid_json_objects)
    print("Filtered JSON objects.")
    full_text_objects = get_full_text_objects(filtered_json_objects)
    print("Got full text objects.")
    full_prompt_content = generate_full_prompt(full_text_objects)
    print("Generated full prompt content.")
    print("Finished main_x_data_cleaner function.")
    return full_prompt_content

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

def get_full_text_objects(filtered_json_objects):
    """
    gets the full text of the tweets
    """
    # Assuming `data` is your dictionary
    full_text = []
    for i in range(len(filtered_json_objects)):
        full_text.append(filtered_json_objects[i]['tweet']['full_text'])
    return full_text

def generate_full_prompt(full_text_objects):
    """
    generates full prompt with which request can be send than to openai
    """
    big_string = ""
    for i in range(20):
        big_string += "---\n" + full_text_objects[i] + "\n---\n"
    return big_string


main_x_data_cleaner("tweets.js")
"""
1. load json and see that it not fails
2. get all raw tweets from the user which do not have this dots at the end
3. 

once i have the json loaded i can try to extract all raw tweets from it. following how an raw tweet looks like:

---
  {
    "tweet" : {
      "edit_info" : {
        "initial" : {
          "editTweetIds" : [
            "1730148412438511703"
          ],
          "editableUntil" : "2023-11-30T09:55:00.000Z",
          "editsRemaining" : "5",
          "isEditEligible" : true
        }
      },
      "retweeted" : false,
      "source" : "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>",
      "entities" : {
        "hashtags" : [ ],
        "symbols" : [ ],
        "user_mentions" : [ ],
        "urls" : [ ]
      },
      "display_text_range" : [
        "0",
        "22"
      ],
      "favorite_count" : "2",
      "id_str" : "1730148412438511703",
      "truncated" : false,
      "retweet_count" : "0",
      "id" : "1730148412438511703",
      "created_at" : "Thu Nov 30 08:55:00 +0000 2023",
      "favorited" : false,
      "full_text" : "happy one year chatgpt",
      "lang" : "en"
    }
  }
---

how can i load them if i get anno
"""
import json

# load all json objects which are not broken into a list
def load_json_objects(filename):
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

valid_json_objects = load_json_objects('tweets.js')


def filter_entities(json_objects):
    return [obj for obj in json_objects if all(not obj['tweet']['entities'][key] for key in obj['tweet']['entities'])]

filtered_json_objects = filter_entities(valid_json_objects)
print(filtered_json_objects[100])
#print(valid_json_objects[1])
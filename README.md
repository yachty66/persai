# persai

## usage

```python
from persai import big_five

data = "path to file with chatgpt data"

"""
will return dict like:

big_five_traits = {
    "Openness": 70,          # Sample value indicating a relatively high level of openness
    "Conscientiousness": 55, # Sample value indicating a moderate level of conscientiousness
    "Extraversion": 40,      # Sample value indicating a slightly lower level of extraversion
    "Agreeableness": 65,     # Sample value indicating a fairly high level of agreeableness
    "Neuroticism": 30        # Sample value indicating a lower level of neuroticism
}
"""

big_five(data)
```

## notes

uses gpt-4 and the prompting techniques provided in https://arxiv.org/pdf/2307.03952.pdf extended by a bit to predict big five values of an person based on chatgpt data. 

- [x] watch a video on how to build a GPT 
- [x] check if you get chatgpt data instantly
- [ ] python package
    - [x] add to readme how pypi should work, i.e. how a user would use the package 
    - [x] create structure for python package
    - [ ] file for appropriate dealing with big five data prediction
        - [x] make a plan based on how the paper does predictions, i.e. how i can do this but with more data and test if this is really valid 
        - [x] get all raw tweets
        - [x] generate a appropriate file for dealing with the x data
        - [x] figure out which model to use 
        - [ ] get last number of tweets so that prompt still fits in token window
        - [ ] create a sample prompt with Zero-Shot Level-Oriented CoT prompting
        - [ ] what are the best possible prompts i can extract from my the kind of files i have access to like whatsapp, chatgpt
        - its just a question of how the ideal prompt looks like and than i am asking myself from where i get this prompt from
            - whats the best place to look for? i am absolutely not sure 

- [x] find out if its possible to upload chatgpt data in GPT interface
    - [ ] make tool for trimming file in a way that it can be uploaded to chatgpt

- [ ] find out how i can extend the method from the paper in a way to deal with all the chatgpt data to make personality prediction not only based on one sentence

- [ ] generate an endpoint for the package
- [ ] GPT
    - gpt should work in a way that user additional to inputting his data is also able to have a conversation about his results and the meaning of personality tests 

i also could just do a python package which does this things like taking data as input and than returning the big five values. later when building the GPT i can use this package in the backend. basically i would go ahead and build an api which i than can use in my GPT. 

data --> persai pypi --> returns scores

in a later stage i can use this package for my GPT in the backend. 




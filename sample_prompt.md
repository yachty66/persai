(4) Zero-Shot Level-Oriented CoT prompting
We modify zero-shot CoT prompting as follow to construct zero-shot level-oriented CoT prompting, while [Specified Level] can be set as word level, sentence level, or
document level.
Analyze the person-generated text from [Specified Level],
determine the person’s levels of Openness, Conscientiousness, Extraversion, Agreeableness, and Neuroticism. Only
return Low or High.
Text: "[Text]"
Level: Let’s think step by step:

q:

- which level (word, sentence or document) achieves the best results? 
- whats the system prompt? 
- what is one example i can take here as text to think about
    - probably i should just take some kind of test pieces from my chat

Analyze the person-generated text from [Specified Level], determine the person’s levels of Openness, Conscientiousness, Extraversion, Agreeableness, and Neuroticism. Only return Low or High.

Text: """
---
tweet
---

---
tweet
---

---
tweet
---
"""

Level: Let’s think step by step:

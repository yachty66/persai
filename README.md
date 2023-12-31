# Persai

![Persai Logo](images/logo.png)

## Introduction 🔎

Persai is a Python package designed to analyze Twitter (X) posts and provide insights into the Big Five personality traits (Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism). This tool leverages data from your Twitter archive to offer a unique perspective on your social media presence. 🐦

![Diagram](images/diagram.png)

[Visit our website for more information and documentation](https://www.persai.org/)

## Installation 🛠️

Install Persai easily using pip:

```bash
pip install persai
```

## How to Use 💡

Follow these steps to analyze your Twitter (X) data using Persai:

1. **Export Your Twitter Data**:
   - Follow Twitter's guidelines to [download your Twitter (X) archive](https://help.twitter.com/en/managing-your-account/how-to-download-your-twitter-archive).

2. **Prepare Your Data**:
   - Locate the `twitter.js` file in your downloaded Twitter (X) data.
   - Save this file in the directory where you plan to run the Persai package.

3. **Set Your OpenAI Key**:
   - Assign your OpenAI key to a variable. For security reasons, avoid hardcoding the key in your script. Instead, consider using environment variables or other secure methods.

3. **Run Persai**:
   - Use the following Python code to perform the Big Five analysis:

   ```python
    from persai import big_five

    openai_key = "your_openai_key_here"
    data = "twitter.js"
    result = big_five(data, openai_key)
    print(result)
   ```

## Sample Output 📈

After running the script, you'll receive a dictionary with the analysis results. It will look something like this:

```json
{
  "openness": "high",
  "conscientiousness": "low",
  "extraversion": "low",
  "agreeableness": "low",
  "neuroticism": "low"
}
```

These results provide a snapshot of the personality traits expressed in your Twitter (X) posts.

## Contributing

Feel free to contribute to the project or suggest improvements! 🌟

## Acknowledgments :clap:

This project is a reimplementation of the ideas and methodologies presented in the paper [Is ChatGPT a Good Personality Recognizer? A Preliminary Study](https://arxiv.org/pdf/2307.03952.pdf). Thank you for providing this research.

## License

This project is licensed under the [MIT License](LICENSE).

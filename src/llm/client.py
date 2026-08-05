"""
LLM Client Module

Responsible for:
- Connecting to LLM APIs
- Sending prompts
- Receiving responses
"""


import os
from openai import OpenAI


class LLMClient:


    def __init__(
        self,
        api_key,
        base_url,
        model_name
    ):

        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url
        )

        self.model_name = model_name



    def generate(
        self,
        prompt,
        temperature=0.2,
        max_tokens=4096
    ):
        """
        Send prompt to LLM and return response.
        """


        response = self.client.chat.completions.create(

            model=self.model_name,

            messages=[

                {
                    "role": "user",
                    "content": prompt
                }

            ],

            temperature=temperature,

            max_tokens=max_tokens

        )


        return response.choices[0].message.content



    def extract_code(
        self,
        response
    ):
        """
        Extract Python code from LLM response.
        """

        if "```python" in response:

            code = response.split(
                "```python"
            )[1].split(
                "```"
            )[0]

            return code.strip()


        return response.strip()

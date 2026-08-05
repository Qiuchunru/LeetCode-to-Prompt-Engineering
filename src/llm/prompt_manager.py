"""
Prompt Manager Module

Responsible for:
- Loading prompt templates
- Managing different prompt strategies
- Generating final prompts for LLM requests
"""


import os


class PromptManager:


    def __init__(self, prompt_directory):

        self.prompt_directory = prompt_directory


        self.prompt_files = {

            "baseline": "baseline_prompt.txt",

            "optimized": "optimized_prompt.txt",

            "ai_assisted": "ai_assisted_workflow.txt"

        }



    def load_prompt_template(self, prompt_type):
        """
        Load prompt template from file.
        """

        if prompt_type not in self.prompt_files:

            raise ValueError(
                f"Unsupported prompt type: {prompt_type}"
            )


        file_path = os.path.join(
            self.prompt_directory,
            self.prompt_files[prompt_type]
        )


        if not os.path.exists(file_path):

            raise FileNotFoundError(
                f"Prompt file not found: {file_path}"
            )


        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            return file.read()



    def generate_prompt(
        self,
        prompt_type,
        problem
    ):
        """
        Generate final prompt by inserting problem information.
        """

        template = self.load_prompt_template(
            prompt_type
        )


        problem_description = self.format_problem(
            problem
        )


        final_prompt = template.replace(
            "{problem_description}",
            problem_description
        )


        return final_prompt



    def format_problem(self, problem):
        """
        Convert problem object into text format.
        """

        return f"""
Problem Title:
{problem['title']}


Difficulty:
{problem['difficulty']}


Category:
{problem['category']}


Description:
{problem['description']}


Expected Algorithm:
{problem.get('expected_algorithm', 'Unknown')}


Constraints:
{problem.get('constraints', [])}
"""

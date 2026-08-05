"""
Experiment Runner Module

Responsible for:
- Running benchmark experiments
- Connecting dataset, prompts, LLM, and evaluator
- Collecting experiment results
"""


from llm.client import LLMClient
from llm.prompt_manager import PromptManager
from evaluation.evaluator import Evaluator



class ExperimentRunner:


    def __init__(
        self,
        dataset,
        llm_client,
        prompt_manager,
        evaluator
    ):

        self.dataset = dataset

        self.llm_client = llm_client

        self.prompt_manager = prompt_manager

        self.evaluator = evaluator



    def run_single_problem(
        self,
        problem,
        prompt_type
    ):
        """
        Run one problem with one prompt strategy.
        """


        # Generate prompt

        prompt = self.prompt_manager.generate_prompt(
            prompt_type,
            problem
        )


        # Ask LLM

        response = self.llm_client.generate(
            prompt
        )


        # Extract code

        code = self.llm_client.extract_code(
            response
        )


        # Evaluate solution

        evaluation = self.evaluator.evaluate(
            code,
            problem["test_cases"]
        )


        return {

            "problem_id":
                problem["problem_id"],


            "title":
                problem["title"],


            "prompt_type":
                prompt_type,


            "generated_code":
                code,


            "evaluation":
                evaluation

        }



    def run_all(
        self,
        prompt_types
    ):
        """
        Run complete benchmark experiment.
        """


        results = []


        for problem in self.dataset:


            for prompt_type in prompt_types:


                print(
                    f"Running {problem['title']} "
                    f"with {prompt_type}"
                )


                result = self.run_single_problem(

                    problem,

                    prompt_type

                )


                results.append(result)



        return results

"""
Dataset Loader Module

Responsible for:
- Loading benchmark problems
- Validating dataset format
- Providing problems for experiments
"""


import json
import os


class DatasetLoader:

    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        self.problems = []


    def load(self):
        """
        Load benchmark dataset from JSON file.
        """

        if not os.path.exists(self.dataset_path):
            raise FileNotFoundError(
                f"Dataset not found: {self.dataset_path}"
            )


        with open(
            self.dataset_path,
            "r",
            encoding="utf-8"
        ) as file:

            self.problems = json.load(file)


        return self.problems



    def get_problem_by_id(self, problem_id):
        """
        Return a specific problem by ID.
        """

        for problem in self.problems:

            if problem["problem_id"] == problem_id:
                return problem


        return None



    def get_problems_by_category(self, category):
        """
        Filter problems by algorithm category.
        """

        return [
            problem
            for problem in self.problems
            if problem["category"] == category
        ]



    def get_problems_by_difficulty(self, difficulty):
        """
        Filter problems by difficulty.
        """

        return [
            problem
            for problem in self.problems
            if problem["difficulty"] == difficulty
        ]



    def count(self):
        """
        Return dataset size.
        """

        return len(self.problems)

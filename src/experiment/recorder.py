"""
Experiment Recorder Module

Responsible for:
- Saving experiment results
- Exporting JSON and CSV files
"""


import json
import csv
import os
from datetime import datetime



class ResultRecorder:


    def __init__(
        self,
        output_directory
    ):

        self.output_directory = output_directory


        os.makedirs(
            output_directory,
            exist_ok=True
        )



    def save_json(
        self,
        results,
        filename="experiment_results.json"
    ):
        """
        Save results as JSON.
        """


        path = os.path.join(

            self.output_directory,

            filename

        )


        with open(
            path,
            "w",
            encoding="utf-8"
        ) as file:


            json.dump(

                results,

                file,

                indent=4,

                ensure_ascii=False

            )


        return path



    def save_csv(
        self,
        results,
        filename="experiment_results.csv"
    ):
        """
        Save summarized results as CSV.
        """


        path = os.path.join(

            self.output_directory,

            filename

        )


        with open(
            path,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:


            writer = csv.writer(file)


            writer.writerow([

                "problem_id",

                "title",

                "prompt_type",

                "pass_rate",

                "runtime"

            ])



            for result in results:


                evaluation = result["evaluation"]


                avg_runtime = sum(

                    item["runtime"]

                    for item in evaluation["details"]

                ) / len(
                    evaluation["details"]
                )


                writer.writerow([

                    result["problem_id"],

                    result["title"],

                    result["prompt_type"],

                    evaluation["pass_rate"],

                    avg_runtime

                ])



        return path

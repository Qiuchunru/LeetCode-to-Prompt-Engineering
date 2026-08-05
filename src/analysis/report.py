"""
Analysis Report Module

Responsible for:
- Loading experiment results
- Calculating statistics
- Generating research summaries
"""


import pandas as pd
import os



class ExperimentAnalyzer:


    def __init__(
        self,
        result_file
    ):

        self.result_file = result_file

        self.data = None



    def load_results(self):
        """
        Load experiment CSV results.
        """

        self.data = pd.read_csv(
            self.result_file
        )

        return self.data



    def prompt_summary(self):
        """
        Calculate performance by prompt strategy.
        """


        summary = self.data.groupby(
            "prompt_type"
        ).agg(

            {

                "pass_rate":"mean",

                "runtime":"mean"

            }

        ).reset_index()



        return summary



    def save_summary(
        self,
        output_path
    ):
        """
        Save summary report.
        """


        summary = self.prompt_summary()


        summary.to_csv(

            output_path,

            index=False

        )


        return output_path

"""
Evaluator Module

Responsible for:
- Evaluating generated solutions
- Comparing outputs with expected answers
- Calculating performance metrics
"""


from evaluation.code_runner import CodeRunner



class Evaluator:


    def __init__(
        self,
        timeout=10
    ):

        self.runner = CodeRunner(
            timeout
        )



    def evaluate(
        self,
        code,
        test_cases
    ):
        """
        Evaluate generated code on multiple test cases.

        Returns:
            evaluation report
        """


        results = []

        passed = 0


        total = len(test_cases)



        for case in test_cases:


            execution = self.runner.execute(

                code,

                case["input"]

            )


            expected = case["output"]


            actual = execution["output"].strip()



            success = (

                execution["success"]

                and

                actual == expected

            )


            if success:

                passed += 1



            results.append({

                "input":
                    case["input"],

                "expected":
                    expected,

                "actual":
                    actual,

                "passed":
                    success,

                "runtime":
                    execution["runtime"]

            })



        return {


            "total_tests":
                total,


            "passed_tests":
                passed,


            "pass_rate":
                passed / total
                if total > 0
                else 0,


            "details":
                results

        }

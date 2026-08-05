"""
Code Runner Module

Responsible for:
- Executing generated Python code
- Running test cases
- Measuring execution result
"""


import subprocess
import tempfile
import os
import time



class CodeRunner:


    def __init__(
        self,
        timeout=10
    ):

        self.timeout = timeout



    def execute(
        self,
        code,
        test_input
    ):
        """
        Execute generated Python code.

        Returns:
            success
            output
            runtime
        """


        temp_file = None


        try:

            with tempfile.NamedTemporaryFile(
                mode="w",
                suffix=".py",
                delete=False,
                encoding="utf-8"
            ) as file:


                file.write(code)

                temp_file = file.name



            start_time = time.time()


            result = subprocess.run(

                [
                    "python",
                    temp_file
                ],

                input=test_input,

                text=True,

                capture_output=True,

                timeout=self.timeout
            )


            runtime = time.time() - start_time



            return {

                "success":
                    result.returncode == 0,

                "output":
                    result.stdout,

                "error":
                    result.stderr,

                "runtime":
                    runtime
            }



        except subprocess.TimeoutExpired:


            return {

                "success": False,

                "output": "",

                "error": "Timeout",

                "runtime": self.timeout
            }



        finally:

            if temp_file and os.path.exists(temp_file):

                os.remove(temp_file)

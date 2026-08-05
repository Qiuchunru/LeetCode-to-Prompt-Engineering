"""
Main Entry Point

Runs the complete LLM algorithm benchmark experiment.
"""


from config import (
    DATASET_PATH,
    PROMPT_DIR,
    RESULT_DIR,
    API_KEY,
    API_BASE_URL,
    MODEL_NAME,
    PROMPT_TYPES,
    TEMPERATURE,
    MAX_TOKENS
)


from dataset.loader import DatasetLoader


from llm.client import LLMClient


from llm.prompt_manager import PromptManager


from evaluation.evaluator import Evaluator


from experiment.runner import ExperimentRunner


from experiment.recorder import ResultRecorder



def main():


    print(
        "Starting LeetCode-to-Prompt-Engineering Experiment"
    )


    # ==========================
    # Load Dataset
    # ==========================


    loader = DatasetLoader(
        DATASET_PATH
    )


    problems = loader.load()


    print(
        f"Loaded {len(problems)} problems"
    )



    # ==========================
    # Initialize LLM
    # ==========================


    llm_client = LLMClient(

        API_KEY,

        API_BASE_URL,

        MODEL_NAME

    )


    print(
        "LLM client initialized"
    )



    # ==========================
    # Initialize Components
    # ==========================


    prompt_manager = PromptManager(

        PROMPT_DIR

    )


    evaluator = Evaluator()



    # ==========================
    # Run Experiment
    # ==========================


    runner = ExperimentRunner(

        problems,

        llm_client,

        prompt_manager,

        evaluator

    )


    results = runner.run_all(

        PROMPT_TYPES

    )



    print(
        "Experiment completed"
    )



    # ==========================
    # Save Results
    # ==========================


    recorder = ResultRecorder(

        RESULT_DIR

    )


    json_file = recorder.save_json(

        results

    )


    csv_file = recorder.save_csv(

        results

    )


    print(
        f"JSON saved: {json_file}"
    )


    print(
        f"CSV saved: {csv_file}"
    )




if __name__ == "__main__":

    main()

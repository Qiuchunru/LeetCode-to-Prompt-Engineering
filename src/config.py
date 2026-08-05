"""
Configuration settings for
LeetCode-to-Prompt-Engineering project.

This file stores:
- LLM configuration
- Dataset paths
- Prompt paths
- Experiment settings
"""


import os


# ==============================
# Project Paths
# ==============================

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)


DATASET_PATH = os.path.join(
    BASE_DIR,
    "dataset",
    "leetcode_problems.json"
)


PROMPT_DIR = os.path.join(
    BASE_DIR,
    "prompts"
)


RESULT_DIR = os.path.join(
    BASE_DIR,
    "results"
)


# ==============================
# LLM Configuration
# ==============================


LLM_PROVIDER = "Kimi"


MODEL_NAME = "kimi-k2.6"


API_BASE_URL = os.getenv(
    "LLM_API_BASE_URL"
)


API_KEY = os.getenv(
    "LLM_API_KEY"
)


# ==============================
# Experiment Settings
# ==============================


PROMPT_TYPES = [

    "baseline",

    "optimized",

    "ai_assisted"

]


SUPPORTED_LANGUAGE = "python"


TEMPERATURE = 0.2


MAX_TOKENS = 4096


# ==============================
# Evaluation Settings
# ==============================


TIMEOUT_SECONDS = 10


SAVE_GENERATED_CODE = True


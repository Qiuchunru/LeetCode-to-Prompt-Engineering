# Source Code Implementation

This directory contains the implementation of the LLM-based algorithm
evaluation framework.

The goal of this system is to automatically evaluate how different prompt
engineering strategies influence algorithmic problem solving.


# System Workflow


```
Benchmark Dataset

        |

        v

Dataset Loader

        |

        v

Prompt Manager

        |

        v

LLM Client

        |

        v

Generated Solution

        |

        v

Code Evaluator

        |

        v

Experiment Recorder

        |

        v

Result Analysis
```


# Directory Structure


```
src/

├── main.py

├── config.py

│
├── dataset/

│   ├── loader.py

│   └── schema.py

│
├── llm/

│   ├── client.py

│   └── prompt_manager.py

│
├── evaluation/

│   ├── evaluator.py

│   └── code_runner.py

│
├── experiment/

│   ├── runner.py

│   └── recorder.py

│
└── analysis/

    └── report.py
```


# Module Description


## Dataset Module

Responsible for loading and managing benchmark problems.

Functions:

- Load JSON dataset.
- Validate problem format.
- Provide problem information.


---

## LLM Module

Responsible for communication with Large Language Models.

Functions:

- Manage API requests.
- Load prompt templates.
- Generate solutions.
- Store model responses.


---

## Evaluation Module

Responsible for evaluating generated code.

Evaluation metrics:

- Correctness.
- Runtime.
- Memory usage.
- Complexity.


---

## Experiment Module

Responsible for running automated experiments.

Functions:

- Execute multiple problems.
- Compare prompt strategies.
- Save experiment results.


---

## Analysis Module

Responsible for analyzing experiment results.

Functions:

- Generate statistics.
- Compare strategies.
- Create research figures.


# Implementation Status

Current status:

Architecture design completed.


Future implementation:

- LLM API integration.
- Dataset loader.
- Automated evaluator.
- Experiment pipeline.
- Result visualization.

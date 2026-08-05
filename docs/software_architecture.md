# Software Architecture

## Overview

This project implements an automated evaluation framework for studying the
impact of prompt engineering on algorithmic problem solving.

The system evaluates different prompting strategies by generating solutions
from Large Language Models and automatically measuring solution quality.


---

# System Architecture


The complete workflow:


```
Benchmark Dataset

        |

        v

Prompt Manager

        |

        v

LLM Interface

        |

        v

Generated Solution

        |

        v

Code Evaluator

        |

        v

Result Analyzer

        |

        v

Experiment Report
```


---

# Project Structure


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

│   ├── code_runner.py

│   ├── correctness.py

│   └── complexity.py

│

├── experiment/

│   ├── runner.py

│   └── recorder.py

│

└── analysis/

    └── report.py
```


---

# Module Description


## 1. Dataset Module


Purpose:

Manage benchmark problems.


Responsibilities:

- Load LeetCode problems.
- Parse problem metadata.
- Provide test cases.
- Store expected solutions.


Input:

```
leetcode_problems.json
```


Output:

```
Problem Object
```


---

# 2. LLM Module


Purpose:

Communicate with Large Language Models.


Responsibilities:

- Load API configuration.
- Send prompts.
- Receive generated responses.
- Extract code solutions.


Supported models:

- OpenAI-compatible APIs.
- Kimi.
- Other LLM providers.


Workflow:

```
Problem

+

Prompt Template

        |

        v

LLM Response

        |

        v

Generated Code
```


---

# 3. Prompt Manager


Purpose:

Manage different prompt strategies.


Prompt types:


## Baseline Prompt

Simple problem solving instruction.


Example:

```
Solve this problem.
```


## Optimized Prompt

Includes:

- Constraint analysis.
- Algorithm selection.
- Complexity reasoning.


## AI Workflow Prompt

Includes:

- Multiple approaches.
- Verification.
- Optimization.


---

# 4. Evaluation Module


Purpose:

Automatically evaluate generated solutions.


Evaluation pipeline:


```
Generated Code

        |

        v

Execution Environment

        |

        v

Test Cases

        |

        v

Evaluation Result
```


Metrics:

- Correctness.
- Runtime.
- Memory usage.
- Complexity.


---

# 5. Experiment Module


Purpose:

Automate experiments.


Responsibilities:

- Run multiple problems.
- Test multiple prompts.
- Save results.
- Generate experiment records.


Example:


```
Problem 1

Baseline Prompt

        |

Evaluation


Problem 1

Optimized Prompt

        |

Evaluation

```


---

# 6. Analysis Module


Purpose:

Generate research statistics.


Functions:

- Compare prompt strategies.
- Calculate improvement.
- Generate charts.
- Export tables for paper.


---

# Reproducibility


The project will provide:


- Dataset.
- Prompt templates.
- Source code.
- Experiment configurations.
- Generated results.


This allows researchers to reproduce and extend the experiments.

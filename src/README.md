# Source Code Structure

This directory contains the implementation of the LLM-based algorithm evaluation framework for the research project:

**From LeetCode to Prompt Engineering**

The source code will implement an automated pipeline to evaluate how different prompt strategies influence LLM-based algorithm problem solving.

---

# Architecture Overview

The complete system workflow:

```
LeetCode Dataset

        ↓

Prompt Strategy Selection

        ↓

LLM API Request

        ↓

Generated Algorithm Solution

        ↓

Automated Evaluation

        ↓

Experiment Results

        ↓

Research Analysis
```

---

# Module Design

## 1. LLM Runner

File:

```
llm_runner.py
```

Purpose:

Responsible for interacting with Large Language Models and generating algorithm solutions.

Main responsibilities:

- Load different prompt templates.
- Send LeetCode problems to LLM APIs.
- Generate Python solutions.
- Store model responses.
- Support multiple LLM models.

Expected input:

```
Problem Description
+
Prompt Template
+
LLM Model
```

Expected output:

```
Generated Code Solution
+
Algorithm Explanation
+
Complexity Analysis
```

---

## 2. Solution Evaluator

File:

```
evaluator.py
```

Purpose:

Automatically evaluate generated solutions produced by LLMs.


Evaluation includes:

### Correctness Evaluation

- Execute generated code.
- Run predefined test cases.
- Check accepted or failed results.


### Efficiency Evaluation

- Measure runtime performance.
- Analyze memory usage.
- Compare algorithm complexity.


### Quality Evaluation

- Data structure selection.
- Algorithm pattern recognition.
- Explanation quality.


Expected workflow:

```
Generated Code

        ↓

Test Cases

        ↓

Execution Environment

        ↓

Evaluation Results
```

---

## 3. Experiment Runner

File:

```
experiment_runner.py
```

Purpose:

Automate large-scale benchmark experiments.


Responsibilities:

- Load LeetCode benchmark dataset.
- Select different prompt strategies.
- Query LLM models.
- Evaluate generated solutions.
- Save experiment results.


Workflow:

```
Dataset

↓

Prompt A / Prompt B / Prompt C

↓

LLM Generation

↓

Automatic Evaluation

↓

Results CSV
```

---

## 4. Result Analysis Module

File:

```
analysis.py
```

Purpose:

Analyze experimental results and generate research insights.


Responsibilities:

- Calculate success rate.
- Compare prompt strategies.
- Generate statistical summaries.
- Create visualization figures.
- Prepare data for research publication.


---

# Planned Project Structure

```
src/

├── llm_runner.py

├── evaluator.py

├── experiment_runner.py

└── analysis.py
```

---

# Implementation Technology

Programming Language:

- Python


Libraries:

- OpenAI API compatible clients
- Pandas
- NumPy
- Matplotlib
- JSON
- Subprocess


---

# Development Roadmap

## Phase 1: Framework Design

Status:

Completed


Tasks:

- Define research question.
- Design experiment methodology.
- Create benchmark structure.


## Phase 2: LLM Integration

Status:

Planned


Tasks:

- Connect LLM API.
- Implement prompt loading.
- Generate algorithm solutions.


## Phase 3: Automated Evaluation

Status:

Planned


Tasks:

- Execute generated code.
- Validate test cases.
- Measure performance.


## Phase 4: Research Analysis

Status:

Planned


Tasks:

- Compare prompt strategies.
- Generate experimental results.
- Prepare research paper.


---

# Current Status

Research framework design completed.

Future work:

- Implement the LLM evaluation pipeline.
- Run benchmark experiments.
- Analyze the impact of prompt engineering on algorithmic problem solving.

# From LeetCode to Prompt Engineering

## Overview

The rapid development of Large Language Models (LLMs) and Prompt Engineering is changing how software engineers write, debug, and optimize code.

Traditionally, Computer Science students spend hundreds of hours practicing algorithmic problems on platforms such as LeetCode to develop skills in:

- Data structure selection
- Algorithm design
- Complexity analysis
- Problem-solving strategies

This project investigates whether AI-assisted programming through optimized prompt engineering can transform the traditional algorithm learning and interview preparation process.

---

# Research Question

## Main Question

**Can optimized prompt engineering improve algorithmic problem-solving performance and reduce the reliance on traditional LeetCode-style algorithm practice?**

This research explores whether future software engineers may need to shift from primarily practicing algorithm implementation toward developing skills in:

- Prompt Engineering
- AI-assisted problem solving
- Solution verification
- Algorithm evaluation

---

# Motivation

## Traditional Software Engineering Preparation

For many years, software engineering candidates have followed a conventional learning path:

```
Learn Data Structures
        ↓
Understand Algorithms
        ↓
Practice Hundreds of LeetCode Problems
        ↓
Improve Algorithmic Problem Solving
        ↓
Technical Interview Preparation
```

This approach emphasizes human ability to independently:

- Recognize algorithm patterns
- Select appropriate data structures
- Optimize time and space complexity
- Implement efficient solutions

---

## Emerging AI-Assisted Workflow

The introduction of LLMs creates a new programming workflow:

```
Problem Description
        ↓
Prompt Engineering
        ↓
LLM-Assisted Algorithm Design
        ↓
Generated Solution
        ↓
Human Verification and Optimization
```

Instead of manually deriving every solution, developers may increasingly focus on:

- Asking effective questions
- Guiding AI reasoning
- Evaluating generated solutions
- Making engineering decisions

This project investigates whether prompt engineering could become an important complementary skill, or potentially an alternative pathway, to traditional algorithm training.

---

# Research Objectives

This project aims to answer three main questions:

### 1. Algorithmic Performance

Can optimized prompts improve LLM performance on algorithmic problems?

Evaluation includes:

- Solution correctness
- Acceptance rate
- Runtime performance
- Memory usage


### 2. Algorithm Design Ability

Can prompt engineering improve:

- Data structure selection
- Algorithm pattern recognition
- Time complexity optimization
- Space complexity optimization


### 3. Future Software Engineering Skills

How might LLM-assisted programming change the skills required for future software engineers?

This project explores whether future developers will rely more on:

Traditional Skills:

```
Algorithm Memorization
        +
Coding Practice
```

or a combination of:

```
Algorithm Understanding
        +
Prompt Engineering
        +
AI Verification Skills
```

---

# Experimental Methodology

The project evaluates different approaches for solving LeetCode-style algorithm problems.

## Experimental Groups

| Approach | Description |
|----------|-------------|
| Baseline Prompt | Directly asking an LLM to solve a problem |
| Optimized Prompt | Using structured prompts to guide algorithm reasoning |
| AI-Assisted Workflow | Multi-step reasoning, verification, and optimization process |


---

# Evaluation Metrics

Generated solutions will be evaluated using:

## Correctness

- Test case success rate
- Accepted solutions
- Runtime errors


## Algorithm Efficiency

- Time complexity
- Space complexity
- Data structure selection


## Code Quality

- Readability
- Explanation quality
- Maintainability


---

# Research Dataset

The initial benchmark will include LeetCode problems covering:

- Arrays
- Hash Tables
- Linked Lists
- Stacks and Queues
- Trees
- Graphs
- Dynamic Programming
- Searching Algorithms


The dataset will gradually expand as experiments progress.

---

# Project Structure

```
LeetCode-to-Prompt-Engineering/

│
├── dataset/
│   └── leetcode_problems.json
│
├── prompts/
│   ├── baseline_prompt.txt
│   ├── optimized_prompt.txt
│
├── src/
│   ├── llm_runner.py
│   ├── evaluator.py
│   └── analysis.py
│
├── experiments/
│   └── experiment_results.csv
│
├── results/
│   └── figures/
│
├── paper/
│   └── research_report.pdf
│
└── README.md
```

---

# Project Status

🚧 Research in Progress


Current Phase:

- [x] Research question definition
- [ ] Dataset collection
- [ ] Prompt design
- [ ] LLM evaluation framework
- [ ] Experimental analysis
- [ ] Research paper preparation
- [ ] arXiv publication


---

# Expected Contributions

This project aims to provide:

1. A benchmark for evaluating LLM-assisted algorithm problem solving.

2. An analysis of how prompt engineering influences algorithm selection and optimization.

3. Insights into how software engineering education may evolve in the LLM era.


---

# Future Work

Future improvements include:

- Testing multiple LLM models
- Expanding the benchmark dataset
- Comparing human and AI-assisted workflows
- Developing automated algorithm evaluation pipelines
- Publishing research findings as an open technical report


---

# Author

Chunru Qiu

Computer Science Undergraduate  
Concordia University

Research Interest:

- Large Language Models
- Prompt Engineering
- Software Engineering
- AI-Assisted Programming

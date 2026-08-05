# Benchmark Dataset Selection Strategy


## Overview

This benchmark evaluates the ability of Large Language Models to solve
algorithmic programming problems under different prompt engineering strategies.

The dataset is designed to represent common algorithm patterns used in
computer science education and software engineering interviews.


---

# Dataset Size

The initial benchmark contains:

- 50 LeetCode-style problems.

The dataset may be expanded to:

- 100+ problems in future experiments.


---

# Difficulty Distribution


The benchmark follows this distribution:


| Difficulty | Number of Problems | Percentage |
|------------|-------------------|------------|
| Easy | 15 | 30% |
| Medium | 25 | 50% |
| Hard | 10 | 20% |


This distribution reflects the typical difficulty distribution encountered
during technical interview preparation.


---

# Algorithm Category Distribution


The benchmark covers:


| Category | Number |
|----------|--------|
| Array | 5 |
| String | 5 |
| Hash Table | 5 |
| Two Pointers | 5 |
| Sliding Window | 5 |
| Linked List | 5 |
| Stack / Queue | 4 |
| Binary Search | 4 |
| Tree | 5 |
| Graph | 3 |
| Dynamic Programming | 4 |


---

# Selection Criteria


Problems are selected according to the following criteria:


## 1. Algorithm Representation

Each problem should represent a recognizable algorithmic pattern.


Examples:

- Hash Table
- Sliding Window
- Binary Search
- Dynamic Programming


---

## 2. Known Optimal Solution

Each problem should have:

- Well-established optimal algorithm.
- Known time complexity.
- Known space complexity.


This allows comparison between generated solutions and expected solutions.


---

## 3. Testability

Each problem should provide:

- Clear input format.
- Deterministic output.
- Automated test cases.


---

## 4. Complexity Diversity

The dataset includes:

- Simple implementation problems.
- Multi-step reasoning problems.
- Optimization problems.


This allows evaluation across different reasoning difficulties.


---

# Dataset Metadata


Each problem record contains:


- Problem ID
- Title
- Difficulty
- Category
- Description
- Constraints
- Expected algorithm
- Optimal complexity
- Test cases


---

# Research Purpose


The goal of this dataset is not to measure whether LLMs can memorize
solutions.

Instead, it evaluates whether prompt engineering can improve:

- Algorithm selection.
- Data structure selection.
- Solution correctness.
- Computational efficiency.

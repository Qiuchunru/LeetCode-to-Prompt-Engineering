# Benchmark Dataset

## Purpose

This dataset contains LeetCode-style programming problems used to evaluate
LLM-assisted algorithm problem solving.

---

## Dataset Format

Each problem contains:

- Problem ID
- Problem title
- Difficulty
- Algorithm category
- Problem description
- Constraints
- Expected optimal algorithm
- Complexity information
- Test cases

---

## Example

```json
{
    "problem_id": 1,
    "title": "Two Sum",
    "difficulty": "Easy",
    "category": "Hash Table",
    "expected_algorithm": "Hash Table",
    "optimal_time_complexity": "O(n)",
    "optimal_space_complexity": "O(n)"
}
```

---

## Dataset Organization

The dataset is organized to support automated experiments.

Each problem record contains:

- Metadata
- Problem description
- Algorithm category
- Difficulty level
- Expected solution information
- Test cases

The dataset format allows the evaluation framework to:

1. Load programming problems.
2. Apply different prompt strategies.
3. Generate LLM solutions.
4. Evaluate generated code.
5. Store experiment results.

---

## Future Expansion

The initial benchmark will contain approximately:

- 50 problems for pilot experiments.
- 100+ problems for extended evaluation.

---

## Algorithm Categories

Problems will cover:

- Array
- String
- Hash Table
- Linked List
- Stack and Queue
- Binary Search
- Tree
- Graph
- Dynamic Programming
- Greedy Algorithms
- Backtracking

---

## Dataset Goal

The goal of this benchmark is not only to measure code generation accuracy,
but also to evaluate:

- Algorithm selection ability.
- Data structure selection.
- Complexity optimization.
- AI-assisted problem-solving performance.

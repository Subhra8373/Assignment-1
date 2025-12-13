# Willans' Formula with Optimized Prime Detector

## Project Overview
This repository contains a solution for **Programming Assignment 1 (Cryptography)**. The goal was to implement a mathematical formula that acts as a "Prime Computer" (generating the $n^{th}$ prime) by transforming a "Prime Detector" (a function that checks primality).

While the original **Willans' Formula** relies on **Wilson's Theorem** (which uses factorials and is computationally infeasible), this project implements a modified version using a **Divisor-Counting Detector** (Trial Division).

## Mathematical Formulation

### 1. The Prime Detector ($F(j)$)
We define a detector function $F(j)$ such that $F(j)=1$ if $j$ is prime, and $0$ otherwise.
Using the trial division method:
$$F(j) = \begin{cases} 1 & \text{if } \forall k \in [2, \sqrt{j}], j \not\equiv 0 \pmod k \\ 0 & \text{otherwise} \end{cases}$$

### 2. The Prime Counting Function ($\pi(m)$)
$$\pi(m) = \sum_{j=1}^{m} F(j)$$

### 3. The Prime Computer ($p_n$)
We use the summation formula to find the $n^{th}$ prime:
$$p_n = 1 + \sum_{m=1}^{2^n} \left\lfloor \left( \frac{n}{1 + \pi(m)} \right)^{1/n} \right\rfloor$$

## Time Complexity Comparison

| Algorithm | Detector Method | Time Complexity | Feasibility |
| :--- | :--- | :--- | :--- |
| **Original Willans'** | Wilson's Theorem ($(j-1)! \equiv -1$) | $O(p_n!)$ (Factorial) | $n < 6$ |
| **This Implementation** | Divisor Counting (Trial Division) | $O(p_n^{2.5})$ (Polynomial) | $n \approx 500+$ |

## How to Run
1. Clone the repository.
2. Run the script using Python 3:
   ```bash
   python prime_computer.py
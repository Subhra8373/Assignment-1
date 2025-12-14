
### 1. The Core Detector: Wilson's Theorem

Wilson's Theorem provides an elegant way to detect primes using only arithmetic:

$$
(j-1)! \equiv -1 \pmod j \quad \text{if and only if } j \text{ is a prime number.}
$$

The theorem is used to construct a prime detector function $F(j)$ that returns 1 if $j$ is prime, and 0 otherwise.

### 2. The Prime Counting Function ($\pi(m)$)

The prime counting function is built by summing the detector:
$$
\pi(m) = \sum_{j=1}^{m} F(j)
$$

### 3. The Prime Computer: Willans' Formula

The final formula for the $n^{th}$ prime number $p_n$ is:
$$
p_n = 1 + \sum_{m=1}^{2^n} \left\lfloor \left( \frac{n}{1 + \pi(m)} \right)^{1/n} \right\rfloor
$$
s

### Prerequisites
- Python 3.x
- Sufficient patience, as even the 7th prime (17) will take noticeable time.

### Running the Code
The code must be run with a small value for `n`.

```python
# Example Code Snippet:
def factorial(x):
    # ... implementation here ...
    
def wilson_detector(j):
    # ... implementation of (j-1)! mod j here ...

# ... rest of the pi_function and nth_prime_formula ...

# Only run for very small n (e.g., n=5)
n = 5 
# The 5th prime is 11
print(f"The {n}th prime is: {nth_prime_formula(n)}")
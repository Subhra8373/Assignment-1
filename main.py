import math
import sys

# --- 1. The Detector ---
def divisor_counting_detector(j):
    """
    The Prime Detector F(j).
    Instead of Wilson's Theorem (j-1)! which is O(j!), 
    we use Trial Division which is O(sqrt(j)).
    
    Returns:
        1 if j is prime
        0 if j is composite
    """
    if j < 2: 
        return 0
    
    # We check divisibility from 2 up to sqrt(j)
    # This represents the summation of divisor checks mathematically.
    limit = int(math.isqrt(j))
    for k in range(2, limit + 1):
        if j % k == 0:
            return 0 # Composite
    return 1 # Prime

# --- 2. The Prime Counting Function ---
def pi_function(m):
    """
    Counts primes <= m by summing the detector output.
    pi(m) = sum(F(j) for j in 1..m)
    """
    count = 0
    for j in range(1, m + 1):
        count += divisor_counting_detector(j)
    return count

# --- 3. The Prime Computer (Willans' Formula Logic) ---
def nth_prime_computer(n):
    """
    Computes the n-th prime number.
    Formula: p_n = 1 + sum_{m=1}^{2^n} floor( (n / (1 + pi(m)))^(1/n) )
    """
    print(f"--- Computing the {n}-th Prime ---")
    
    summation = 0
    # Theoretical upper bound is 2^n. 
    # For n=10, 2^10 = 1024. For n=20, this becomes large but feasible with this detector.
    limit = 2**n 
    
    for m in range(1, limit + 1):
        pi_m = pi_function(m)
        
        # Willans' Logic:
        # If pi(m) < n, the term (n / (1+pi(m))) is >= 1.
        # The nth root and floor function turn this into 1.
        # If pi(m) >= n, the term becomes < 1, and floor turns it to 0.
        
        # Optimization: If we have found n primes (pi(m) == n), 
        # the formula will output 0 for all future m. We can stop early.
        if pi_m >= n:
            break
            
        term_inner = n / (1 + pi_m)
        
        # Note: We use a small epsilon to handle floating point precision issues
        # though strictly integer math is preferred for formal proofs.
        term_root = term_inner ** (1/n)
        term_floor = math.floor(term_root + 1e-9)
        
        summation += term_floor
        
    result = 1 + summation
    return result

if __name__ == "__main__":
    test_inputs = [1, 5, 10, 50] 
    
    print(f"{'n':<5} | {'Computed Prime':<15} | {'Verification'}")
    print("-" * 40)
    
    for n in test_inputs:
        try:
            p_n = nth_prime_computer(n)
            print(f"{n:<5} | {p_n:<15} | {'Correct' if divisor_counting_detector(p_n) else 'Incorrect'}")
        except OverflowError:
            print(f"{n:<5} | {'Too Large'}")
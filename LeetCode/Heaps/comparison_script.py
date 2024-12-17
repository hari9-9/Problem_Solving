import heapq
import random
import time
import tracemalloc
from typing import List

# Configurable variables
INPUT_SIZE = 1000000  # Change this to adjust the size of the input list
K = 50000  # Number of iterations for modifying elements
MULTIPLIER = 2  # Multiplier value for the operations

# Generate random input list
def generate_random_list(size: int, start: int = 1, end: int = 1000) -> List[int]:
    return [random.randint(start, end) for _ in range(size)]

# First Solution: Simple Array Operations
class SolutionArray:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            n = min(nums)
            x = nums.index(n)
            nums[x] = nums[x] * multiplier
        return nums

# Second Solution: Heap-based Approach
class SolutionHeap:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i], i))
        for _ in range(k):
            ele, idx = heapq.heappop(heap)
            nums[idx] = ele * multiplier
            heapq.heappush(heap, (ele * multiplier, idx))
        return nums

# Function to measure time and memory usage
def measure_performance(solution_class, nums: List[int], k: int, multiplier: int):
    nums_copy = nums.copy()  # Work on a copy to keep input consistent
    solution = solution_class()
    
    # Start memory and time tracking
    tracemalloc.start()
    start_time = time.time()
    result = solution.getFinalState(nums_copy, k, multiplier)
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    time_taken = end_time - start_time
    space_used = peak / 1024  # Convert bytes to KB

    return result, time_taken, space_used

def main():
    print("--- Performance Comparison ---")
    
    # Generate random input list
    nums = generate_random_list(INPUT_SIZE)
    print(f"Input List Size: {INPUT_SIZE}, K: {K}, Multiplier: {MULTIPLIER}\n")

    # Measure performance for SolutionArray
    print("Running Solution 1 (Simple Array Operations)...")
    _, time_array, space_array = measure_performance(SolutionArray, nums, K, MULTIPLIER)
    print(f"Time Taken: {time_array:.6f} seconds")
    print(f"Peak Memory Used: {space_array:.2f} KB\n")

    # Measure performance for SolutionHeap
    print("Running Solution 2 (Heap-based Approach)...")
    _, time_heap, space_heap = measure_performance(SolutionHeap, nums, K, MULTIPLIER)
    print(f"Time Taken: {time_heap:.6f} seconds")
    print(f"Peak Memory Used: {space_heap:.2f} KB\n")

    # Comparison Summary
    print("--- Summary ---")
    print(f"Solution 1 (Array Operations) - Time: {time_array:.6f}s, Memory: {space_array:.2f} KB")
    print(f"Solution 2 (Heap-Based) - Time: {time_heap:.6f}s, Memory: {space_heap:.2f} KB")

if __name__ == "__main__":
    main()

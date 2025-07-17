#!/usr/bin/env python3
"""
Performance comparison script to demonstrate the fix for Bug #2
"""
import time
import random

# Original buggy O(n²) algorithm
def find_duplicates_buggy(numbers):
    duplicates = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j and numbers[i] == numbers[j]:
                if numbers[i] not in duplicates:
                    duplicates.append(numbers[i])
    return duplicates

# Fixed O(n) algorithm
def find_duplicates_fixed(numbers):
    seen = set()
    duplicates = set()
    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)

def run_performance_test():
    # Test with different data sizes
    test_sizes = [100, 500, 1000, 2000]
    
    print("Performance Comparison: Bug Fix #2 - Algorithm Optimization")
    print("=" * 60)
    print(f"{'Size':<10} {'Buggy (O(n²))':<15} {'Fixed (O(n))':<15} {'Improvement':<15}")
    print("-" * 60)
    
    for size in test_sizes:
        # Create test data with some duplicates
        numbers = list(range(size)) + random.choices(range(size // 2), k=size // 10)
        random.shuffle(numbers)
        
        # Test buggy algorithm
        start_time = time.time()
        result_buggy = find_duplicates_buggy(numbers)
        buggy_time = time.time() - start_time
        
        # Test fixed algorithm
        start_time = time.time()
        result_fixed = find_duplicates_fixed(numbers)
        fixed_time = time.time() - start_time
        
        # Calculate improvement
        improvement = buggy_time / fixed_time if fixed_time > 0 else float('inf')
        
        print(f"{size:<10} {buggy_time:<15.6f} {fixed_time:<15.6f} {improvement:<15.2f}x")
        
        # Verify both algorithms produce the same results (when sorted)
        assert sorted(result_buggy) == sorted(result_fixed), "Algorithms should produce same results"

if __name__ == "__main__":
    run_performance_test()
    print("\n✅ Performance test completed successfully!")
    print("The fixed algorithm shows significant performance improvements, especially with larger datasets.")
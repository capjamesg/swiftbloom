import mmh3
from typing import Union
import math

def estimate_error_rate(n: int, m: int, k: int):
    # k = hash functions
    # m = # of bits
    # n = # of elements
    return math.pow(1 - math.exp(-k * n / m), k)

class SwiftBloom:
    def __init__(self, size: int, k_hash_functions: int = 3):
        self.bits = [False] * size
        self.size = size
        self.k_hash_functions = k_hash_functions

    def add(self, item: Union[str, int]):
        hash_function_results = []

        for i in range(0, self.k_hash_functions):
            hash_function_results.append(mmh3.hash(item, i) % self.size)

        for hash_function_result in hash_function_results:
            self.bits[hash_function_result] = True

    def query(self, item: Union[str, int]):
        hash_function_results = []

        for i in range(0, self.k_hash_functions):
            hash_function_results.append(mmh3.hash(item, i) % self.size)

        contains_zero_bit = [self.bits[hash_function_result] for hash_function_result in hash_function_results]

        if False in contains_zero_bit:
            return False
        
        return True
    
names = ["James", "Taylor", "TayTay"]

bloom = SwiftBloom(1000)

for name in names:
    bloom.add(name)

print(bloom.query("x"))
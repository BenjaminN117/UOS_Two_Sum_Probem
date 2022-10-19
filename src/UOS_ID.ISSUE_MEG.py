# Creates empty dictionary to store value and index of elements as key-pairs.
# Iterates through list values and indices containing the random numbers. 
# If difference between target and current value in list is included already as dictonary key, this means it's the solution. 
# If it's not solution, it just adds value and index as key-value pair in dictonary and continues iteration.

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for idx, value in enumerate(nums):
            if target - value in values:
                return [values[target - value], idx]
            else:
                values[value] = idx

# This solution iterates over the list of numbers just once so time complexity of the algorithm is O(n)
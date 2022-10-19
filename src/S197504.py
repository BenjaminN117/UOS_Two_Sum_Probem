'''
Product:
Description:
Author:
'''
import random
import itertools as it
from generator import listClass

class Solution():
    def __init__(self):
        inst = listClass()
        self.listOfNumbers = inst.number_generator()
    
    def your_solution(self):
        randomTarget = random.randint(3, 20)
        list_combinations = (list(it.combinations(self.listOfNumbers, 2)))
        print("Target number is: " + str(randomTarget))
        print("\nCombinations found: ")
        for i in list_combinations:
            target_check = sum(i)
            if target_check == randomTarget:
                print("\n" + str(i))
        if target_check != randomTarget:
            print("\nNo further combinations found.")
        
        pass

if __name__ == "__main__":
    inst = Solution()
    inst.your_solution()
'''
Product: Two_Sum
Description: Two sum generator
Author: Edvin papakul
'''
from generator import listClass

class Solution():
    def __init__(self):
        inst = listClass()
        self.listOfNumbers = inst.number_generator()
    
    def your_solution(self):
        '''
        Write you solution in here!
        '''
        target = 9
        list1 = []
        for i in range(len(self.listOfNumbers)):
            for j in self.listOfNumbers:
                if j != self.listOfNumbers[i] and j + self.listOfNumbers[i] == target:
                    list1.append((self.listOfNumbers[i], j))
        print(list1)
        
        pass

if __name__ == "__main__":
    inst = Solution()
    inst.your_solution()
    
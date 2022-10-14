'''
Product: Two Sum Problem Number Generator
Description: Creates a list of random numbers
Author: Benjamin Norman 2022
'''

import random

class listClass():
    
    def __init__(self):
        # Creates an empty list
        self.listOfNumbers = []
    
    def number_generator(self):
        # Picks random number for the length of the list to be
        highestListNumber = random.randint(4, 10)
        
        for i in range(0,highestListNumber):
            # Picks a random number and adds it to the list
            randomNumber = random.randint(1,20)
            self.listOfNumbers.append(randomNumber)
            
        return self.listOfNumbers
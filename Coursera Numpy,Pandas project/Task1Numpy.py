#Task 1
#Write a code that takes in a positive int x from user and creates an array with random numbers from 0 to x in 1x10
import numpy as np
x=int(input("Please enter a positive int:"))
my_matrix= np.random.randint(0,x,10)
print(my_matrix)
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Question 1
numbers = np.empty([4,4], dtype='int64')

for row in range(4):
    for col in range(4):
        numbers[row][col] = row + col
print("Question 1:\n")        
print(numbers)
#-------------------------------------------

#Question 2
print("\nQuestion 2:\n")
some_variable = numbers
#Part A.
print(type(some_variable)) #<class 'numpy.ndarray'>

#Part B.
print(some_variable.dtype) #int64

#Part C.
print("\n")
#number = int(input("Enter an integer: "))
number = 3
numbers = np.arange(number * number).reshape(number, number)
print(numbers)

#Part D.
print("\n")
tictactoe = np.array([["x", "x", "o"], ["o", "o", "x"], ["x", "x", "o"]])
print(tictactoe[1:2])
#-------------------------------------------

#Question 3
print("\nQuestion 3:\n(Referance Graph)")
wins = pd.read_csv('warriors.csv')

wins["Percentage"] = (wins["Wins"] / 82 *100)

plt.figure("NBA Analysis")
plt.title("Golden State Warriors")
plt.xlabel("Year")
plt.ylabel("Winning Percent")
plt.plot(wins["Year"], wins["Percentage"], "b--")
plt.plot(wins["Year"], wins["Percentage"], "rd")

plt.show()

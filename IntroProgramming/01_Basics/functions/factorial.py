"""
Docstring for practice_problem
"""

# factorial - create a program which allows the user to enter a nunmber and then outputs the factorial of a number
# 4! = 4 *3 *2 *1 = 24

def factorial(n):
  result = 1
  for i in range(1, n+1):
      result *= i
  return result

user_input = int(input("Please enter a number for the factorial: "))
print(f"{user_input}! factorial is {factorial(user_input)}")
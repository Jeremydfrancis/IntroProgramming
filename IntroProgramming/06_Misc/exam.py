"""
Jeremy Francis
2026_02_11
FizzBuzz
"""

# create a program which counts from 1 to 100
# if the current is divisible by 3 print fizz
# if divisble by 5 print buzz
# if both print fizz buzz

# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("fizz")
#     elif i % 5 == 0:
#         print("buzz")
#     else:
#         print(i)

# for i in range(1, 101):
#       print(i, end=" ")
#       if i % 3 == 0:
#             print("FIZZ", end="")
#       if i % 5 == 0:
#             print("BUZZ", end="")

for i in range(1,101):
      output_string = ""
      if i % 3 == 0:
            output_string += " FIZZ"
      if i % 5 == 0:
            output_string += " BUZZ"
      print(str(i) + output_string)
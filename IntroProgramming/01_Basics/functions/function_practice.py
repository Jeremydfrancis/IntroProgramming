"""
Docstring for functions
"""
#Create a function which accepts a name as a parameter
#Inside function ask if male or female
# If male, append Mr. before the name if female return Mrs.
# return adjusted name at the end
# COMPOUND INTEREST FORMULA EXTRA CREDIT A = P(1 + r/n)nt

def hello_person(name):
      user_input = input("Are you a (M)ale or (F)emale? ").upper()
      if user_input == "M":
            return "Mr." + name
      elif user_input == "F":
            return"Mrs." + name
      return name


def area_of_triangle(base,height):
      area = (base*height)/2
      return area


def main():
      print(area_of_triangle(50,100))
main()


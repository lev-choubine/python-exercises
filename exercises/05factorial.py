# Write a method to compute the `factorial` of a number.
# Given a whole number n, a factorial is the product of all
# whole numbers from 1 to n.
# 5! = 5 * 4 * 3 * 2 * 1
#
# Example method call
#
# factorial(5)
#
# > 120
#

def factorial(num):
    fact = 1
    for i in range(num):
        fact = fact * (i+1)
    print(fact)

factorial(5)

class Chef:
  def __init__(self, name, lastname):
    self.name = name
    self.age = age

Chef 1 = Person("Gordon", "Ramsay")
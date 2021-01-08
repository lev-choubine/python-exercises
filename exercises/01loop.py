# Write a method called `p_times` that takes a `statement` and
# a `num` as inputs, and outputs the `statement` some `num` of times
# to the console.
#
# Example method call:
#
# p_times('Hello there', 1)
#
# > Hello there
#
# p_times('Hello there', 3)
#
# > Hello there
# > Hello there
# > Hello there



def p_times():
    num = int(input("enter a number "))
    data = str(input("enter a sentense "))
    for line in range(num):
        result = data 
        print(result)

p_times()
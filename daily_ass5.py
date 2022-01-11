# 1. write a python function to find the max of 3 numbers.
def max_num(a, b, c):
    return max(a, b, c)

print(max_num(2, 5, 8))
#2. Write a python function to sum all the numbers in a list.
def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((8, 2, 3, 0, 7)))

#3. Write a python function to multiply all numbers in a list
def multiply(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total  
print(multiply((8, 2, 3, -1, 7)))

#4. Write a python function to reverse a given string.
def my_function(x):
  return x[::-1]
myword = my_function("I am beautifully made by God")

print(myword)
#5. Write a python function that takes a string and displays the number of upper case letters and the number of lower case letters.
def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test('The quick Brown Fox')

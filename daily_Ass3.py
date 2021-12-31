1. What is the output of the following range() function
for num in range(2,-5,-1):
    print(num, end=", ")
2. Given the nested if-else below, what will be the value x when the code executed successfully
x = 0
a = 5
b = 5
if a > 0:
    if b < 0:
        x = x + 5
    elif a > 5:
        x = x + 4
    else:
        x = x + 3
else:
    x = x + 2
print(x)
3
3. What is the output of the following nested loop?
for num in range(10, 14):
   for i in range(2, num):
       if num%i == 1:
          print(num)
          break
10
11
12
13         
4. What is the output of the following if statement
a, b = 12, 5
if a + b:
    print('True')
else:
  print('False')
True 
5. What is the value of the var after the for loop completes its execution
var = 10
for i in range(10):
    for j in range(2, 10, 1):
        if var % 2 == 0:
            continue
            var += 1
    var+=1
else:
    var+=1
print(var)

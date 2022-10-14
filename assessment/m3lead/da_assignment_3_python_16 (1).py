
## Exercises

Answer the questions or complete the tasks outlined in bold below, use the specific method described if applicable.

** What is 7 to the power of 4?**
"""

pow(7,4)

"""** Split this string:**

    s = "Hi there Sam!"
    
**into a list. **
"""

s = "Hi there dad!"

output = s.split()
print(output)

"""** Given the variables:**

    planet = "Earth"
    diameter = 12742

** Use .format() to print the following string: **

    The diameter of Earth is 12742 kilometers.
"""

res = "The diameter of the {planet} is {diameter} kilometers."

print(res.format(planet = "Earth",diameter = 12742))

"""** Given this nested list, use indexing to grab the word "hello" **"""

lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]

lst[3][1][2]

"""** Given this nest dictionary grab the word "hello". Be prepared, this will be annoying/tricky **"""

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}

d['k1'][3]['tricky'][3]['target'][3]

"""** What is the main difference between a tuple and a list? **"""

print("list can be modified where as tuple can not be modified")

"""** Create a function that grabs the email website domain from a string in the form: **

    user@domain.com
    
**So for example, passing "user@domain.com" would return: domain.com**
"""

def domain(inp):
  temp = inp.split('@')
  print(temp[1])

inp = input()
domain(inp)

"""** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **"""

from logging import fatal
def contain(inp):
  temp = inp.split(" ")
  com = ['d','o','g']
  flag = -1
  for i in temp:
    if(len(i)==3 or len(i)==4):
      for j in range(len(i)):
        if(i[j] != com[j]):
          break
        elif(j == len(com)-1):
          return True
  return False

inp = input()
print(contain(inp))

"""** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **"""

def contain(inp):
  com=['d','o','g']
  temp = inp.split(" ")
  count = 0
  for i in temp:
    if(len(i) == 3 or len(i)== 4):
      for j in range(len(i)):
        if(i[j] != com[j]):
          break
        elif(j == len(com)-1):
          count +=1
  return count

inp = input()
print(contain(inp))

"""### Problem
**You are driving a little too fast, and a police officer stops you. Write a function
  to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
  If your speed is 60 or less, the result is "No Ticket". If speed is between 61 
  and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all 
  cases. **
"""

def caught_speeding(speed, is_birthday):
    
    if is_birthday:
        speeding = speed - 5
    else:
        speeding = speed
    
    if speeding > 80:
        return 'Big Ticket'
    elif speeding > 60:
        return 'Small Ticket'
    else:
        return 'No Ticket'

print(caught_speeding(85,False))

caught_speeding(85,True)

"""Create an employee list with basic salary values(at least 5 values for 5 employees)  and using a for loop retreive each employee salary and calculate total salary expenditure. """

salary = [12000,13000,14000,15000,20000]
total_exp = 0
for i in salary:
  total_exp+=i
print("the total salary expenditure is {value}".format(value=total_exp))

"""Create two dictionaries in Python:

First one to contain fields as Empid,  Empname,  Basicpay

Second dictionary to contain fields as DeptName,  DeptId.

Combine both dictionaries. 
"""

from collections import Counter

dic_1 = Counter({'employ' : ['Empid','Empname','Basicpay']})
dic_2 = Counter({'employ' : ['DeptName','DeptId']})


print(str(dic_1))
print(str(dic_2))

final_dic = dic_1 + dic_2
print(str(final_dic))

['Empid','Empname','Basicpay']
['DeptName','DeptId']
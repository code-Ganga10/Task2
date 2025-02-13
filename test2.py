# Data types 
list=[1,2,3]
print(list)

list.append(7)
print(list)

list.extend([4,5,9])
print(list)

list.remove(3)
print(list)

list.pop()
print(list)

print(list[1])
print(list[-2])


t=(10,)
print(type(t))
t1=(19,32)
print(t)
print(t1)
print(t1[1])
print([-1])


set={}   #it is empty dictionary
print(type(set))
set={10,22,33}
print(type(set))

set.add(4)
print(set)

set.remove(22)
print(set)

set.discard(10)
print(set)

# dictionary

dict={"a":10,"b":22}
print(dict)
print(dict['a'])

dict['c']=33
print(dict)

dict.pop('a')
print(dict)

del dict['b']
print(dict)

# type casting 
int = 10
float = 10.5
result = int+float  
print(result)  #implicit conversion means automatic conersion 

f=2.0
i=int(2.0)
print(i)  #ecplicit conversion 


# Try and Exception 
class CustomError(Exception):
    pass
try:
    raise CustomError("custom error")
except CustomError as e:
    print(e)
finally:
    print("I am always print")


# function and build in function

def ganga(name):
    return f"hello,{name}"

print(ganga("diksha"))

def square(number):
    return number * number
print(square(6))  

# built in function in python 
b= int(input("enter a integer number"))  #input is also a built in function in python #
print(b,"Is a integer number")

a=[19,29,11,22,89]
print(min(a),max(a))
print(len(a))
print(abs(22.54))
print(pow(2,3))
print(round(7,2))

# User Defined Function 
a=(10,11,3,3,4,4,5,5)
print(type(10))
print(id(10))
print(len(a))



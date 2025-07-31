# a python code for a simple calculator
print("welcome to my smart calculator")

#accepting number and operators
first_number=int(input("please enter the first number: "))

operator= input ("please enter your operator sign (+, -, *, /): ")

second_number= int(input("please enter the second number: "))

#printing out the results

if operator == "+":
    result= first_number + second_number

elif operator == "-":
    result= first_number - second_number
elif operator == "+":
    result= first_number * second_number
elif operator == "/":
    if second_number !=0:
        result= first_number / second_number
else :
    result = "invalid operator !"


#printing result
print ( F"{first_number} {operator} {second_number} = {result}")






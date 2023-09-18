#Calculator in Python
from art import logo
from replit import clear

def Add (n1, n2):
  return n1 + n2
  
def Subtract (n1, n2):
  return n1 - n2
  
def Multiply (n1, n2):
  return n1 * n2
  
def Divide (n1, n2):
  return n1 / n2
  
def Modulus (n1, n2):
  return n1 % n2

operations = {"+" : Add, "-" : Subtract, "*" : Multiply, "/" : Divide, "%" : Modulus,}

def calculator():
  print(logo)
  num1 = float(input("Enter the first number: "))
    # print (operations.keys())
  
  for operator in operations:
    print(operator)
  
  flag = True
  while flag == True:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("Enter the next number: "))
  
    operation_function = operations[operation_symbol]
    answer = operation_function(num1, num2)
    to_continue = (input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation : "))
  
    if to_continue == "y":
      num1 = answer
    else:
      flag = False
      clear()
      calculator()

calculator()



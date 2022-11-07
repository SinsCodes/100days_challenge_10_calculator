from art import logo

def add(n1,n2):
  return n1+n2

def subtract(n1,n2):
  return n1-n2
  
def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2

operations={
  
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)
  
  num1=float(input("what is the first number? "))
    
  for symbol in operations:
    print(symbol)
  calculator_end=True
  while calculator_end:
    
    operation_symbol=input("pick an operation : ")
    num2=float(input("what is your next number? "))
   
    calculator_function=operations[operation_symbol]
    first_answer=calculator_function(num1,num2)
    
    print(f"{num1}{operation_symbol}{num2}={first_answer}")
    
    if input(f"Type'y'to continue calculating with {first_answer} or type 'n'to exit: ")=="y":
      num1=first_answer
    else:
      calculator_end=False
      calculator()
    
calculator()  
  
    
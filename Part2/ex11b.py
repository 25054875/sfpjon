def calculate(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator" 
    
print(calculate(10, "+", 10))
print(calculate(10, "-" , 10))      
print( calculate (10, "*", 10) ) 
print ( calculate (10 , "/" , 10 )) 
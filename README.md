# Calculator
Basic Calculator to perform the operations
This is a simple command-line calculator implemented in Python. It allows users to perform basic arithmetic operations such as addition, subtraction, multiplication, division, and floor division. It also demonstrates a more advanced approach using `eval` for dynamic expression evaluation.

# Features
Basic Arithmetic Operations:
    * Addition
    * Subtraction
    * Multiplication
    * Division (with zero division check)
    * Floor Division
# How to Use
Follow the Prompts:
    * Enter the first number.
    * Enter the second number.
    * Choose the operation you want to perform by entering the corresponding number.
    * For the advanced version, you will be asked to enter the number of variables, variable names and values, and then the expression.
    
#Code Explanation
It takes two floating-point numbers as input.
It presents a menu of operations and prompts the user to choose one.
The match statement then directs the program flow to the corresponding case.
Each case performs the selected operation and prints the result.
It includes a check for division by zero.
The _ case acts as a default, handling invalid input.
Advantages: This approach is structured, readable, and handles different operations cleanly.
Disadvantages: It requires Python 3.10 or later for the match statement.

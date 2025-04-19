# 📘 Gentle Programming Language Documentation

## 🚀 Introduction

Gentle is a lightweight, interpreted programming language designed for simplicity and readability. With its clean syntax and intuitive structure, Gentle offers an accessible entry point for beginners while still providing powerful features for experienced developers.

## 🔤 Basic Syntax

### Comments
```
# This is a comment
```

### Variables and Assignment
```
var x = 42        # Integer
var pi = 3.14159  # Float
var name = "Bob"  # String
var is_active = TRUE  # Boolean
```

## 🧮 Data Types

### Primitive Types
- **Integers**: `42`, `-7`, `0`
- **Floats**: `3.14`, `-0.01`, `5.0`
- **Strings**: `"Hello, world!"`, `"Gentle is fun!"`
- **Booleans**: `TRUE`, `FALSE`

### Collections
- **Lists**: `[1, 2, 3]`, `["apple", "orange"]`, `[]`

## 🧠 Operators

### Arithmetic Operators
- Addition: `+`
- Subtraction: `-`
- Multiplication: `*`
- Division: `/`
- Power: `^`

### Comparison Operators
- Equal to: `==`
- Not equal to: `!=`
- Less than: `<`
- Greater than: `>`
- Less than or equal: `<=`
- Greater than or equal: `>=`

### Logical Operators
- AND: `and`
- OR: `or`
- NOT: `not`

## 🔄 Control Flow

### If Statements
```
if condition -> 
    expression
else if another_condition ->
    expression
else
    expression
```

### For Loops
```
for i = 0 to 10 ->
    expression

# With step
for i = 0 to 10 step 2 ->
    expression
```

### While Loops
```
while condition ->
    expression
```

## 🧩 Functions

### Function Definition
```
function add(a, b) -> a + b

# Anonymous function
var multiply = function(a, b) -> a * b
```

### Function Calls
```
add(5, 3)        # Returns 8
multiply(4, 2)   # Returns 8
```

## 📚 Lists

### Creating Lists
```
var fruits = ["apple", "banana", "cherry"]
```

### List Operations
```
fruits[0]        # Access element (returns "apple")
fruits + "orange"  # Add element (returns ["apple", "banana", "cherry", "orange"])
fruits - 0       # Remove element at index (returns ["banana", "cherry"])
fruits * [1, 2]  # Concatenate lists
```

## 🔍 Examples

### Calculate Factorial
```
function factorial(n) ->
    if n == 0 ->
        1
    else
        n * factorial(n - 1)

var result = factorial(5)  # Returns 120
```

### Print First 10 Fibonacci Numbers
```
function fibonacci(n) ->
    if n <= 1 ->
        n
    else
        fibonacci(n - 1) + fibonacci(n - 2)

for i = 0 to 9 ->
    fibonacci(i)  # Returns [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

### Simple Calculator
```
function calculator(a, op, b) ->
    if op == "+" ->
        a + b
    else if op == "-" ->
        a - b
    else if op == "*" ->
        a * b
    else if op == "/" ->
        a / b
    else
        "Unknown operation"

var result = calculator(10, "*", 5)  # Returns 50
```

## 🏃 How To Run ? 

### 1) Firstly you need:
python *(3.12 RECOMMENDED)*

### 2) After Downloading:
run in terminal:
cd <directory_to_file>
python run.py

## 💡 Tips and Best Practices

- Use descriptive variable names for better code readability
- Break complex operations into smaller functions
- Comment your code to explain complex logic
- Use lists to group related values
- Use indentation to improve code structure (though not required by the language)


Happy coding with Gentle! 🎉

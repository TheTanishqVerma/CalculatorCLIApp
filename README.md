# Python Command-Line Calculator

A simple interactive calculator built in Python that supports basic arithmetic operations like addition, subtraction, multiplication, and division. This calculator runs in the command-line interface (CLI).

## Features

- Addition, Subtraction, Multiplication, and Division  
- Decimal precision support  
- Graceful handling of division by zero  
- Easy-to-navigate CLI menu  
- Looping until the user chooses to exit  

## File Structure

```
calculator.py     # Main calculator script  
README.md         # Project documentation (you are here)  
```

## Requirements

- Python 3.6 or higher  
- No third-party libraries required (uses built-in `re` module)

## How to Run

1. Open a terminal or command prompt.  
2. Navigate to the folder containing `calculator.py`.  
3. Run the script:

```bash
python calculator.py
```

## Sample Output

```
***** Welcome To Python Calculator *****
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
Choose an option (1-5): 1
Enter the first number: 12.5
Enter the second number: 3.2
Result: 15.7
```

## Input Validation

The calculator ensures only valid numeric inputs using regular expressions:

- Accepts integers and decimal numbers (e.g., `42`, `-3.14`)  
- Division by zero is caught and returns an error message instead of crashing
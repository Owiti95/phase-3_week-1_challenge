# Python Coding Assessment

## Overview

This repository contains my solutions for the Python Coding Assessment. The assessment is designed to evaluate my understanding of fundamental Python concepts. It includes tasks covering basic data structures, functions, decorators, sequences, sets, dictionaries, and object-oriented programming.

## Instructions

1. **Complete the Tasks**: Follow the tasks outlined below.
2. **Adhere to Best Practices**: Ensure that my code follows Python best practices.
3. **Comment Your Code**: Add comments to explain the logic and approach where necessary.
4. **Run the Code**: Instructions on how to set up and run the code are provided below.

## Setup Instructions

To set up and run the code, follow these steps:

### Prerequisites

- Python 3.x installed on your machine
- Git installed on your machine

### Steps to Set Up and Run

1. **Clone the Repository**
   Clone the repository to your local machine using the following command:
   ```bash
   git clone https://github.com/your-username/your-repository.git
   ```

2. **Navigate to the Project Directory**
   ```bash
   cd your-repository
   ```

3. **Create a Virtual Environment (Optional but recommended)**
   ```bash
   python3 -m venv venv
   ```

4. **Activate the Virtual Environment**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. **Run the Python Code**
   To test each function, you can run the individual Python files or import them into a Python interactive shell. Use the following command to execute a file:
   ```bash
   python filename.py
   ```

## Tasks

### 1. Function: `add_numbers` (2 points)
   Implement a function that takes two numbers as input and returns their sum.
   ```python
   def add_numbers(num1, num2):
       return num1 + num2
   ```

### 2. Function: `is_even` (2 points)
   Implement a function that checks whether a given number is even.
   ```python
   def is_even(number):
       return number % 2 == 0
   ```

### 3. Function: `reverse_string` (2 points)
   Implement a function that reverses a given string.
   ```python
   def reverse_string(text):
       return text[::-1]
   ```

### 4. Function: `count_vowels` (2 points)
   Implement a function that counts the vowels in a given string, ignoring case.
   ```python
   def count_vowels(text):
       vowels = "aeiou"
       return sum(1 for char in text.lower() if char in vowels)
   ```

### 5. Function: `calculate_factorial` (2 points)
   Implement a function that calculates the factorial of a non-negative integer.
   ```python
   def calculate_factorial(n):
       result = 1
       for i in range(1, n + 1):
           result *= i
       return result
   ```

### 6. Function: `apply_decorator` (1 point)
   Implement a decorator that prints "Decorator Applied" before calling the original function.
   ```python
   def decorator_func(func):
       def wrapper():
           print("Decorator Applied")
           return func()
       return wrapper

   def apply_decorator(func):
       return decorator_func(func)
   ```

### 7. Sequences: Sort List of Tuples (1 point)
   Implement a function to sort a list of tuples (name, age) by age.
   ```python
   def sort_by_age(lst):
       return sorted(lst, key=lambda x: x[1])
   ```

### 8. Sets and Dictionaries: Merge Dictionaries (1 point)
   Implement a function that merges two dictionaries, summing values of common keys.
   ```python
   def merge_dicts(dict1, dict2):
       merged_dict = dict1.copy()
       for key, value in dict2.items():
           merged_dict[key] = merged_dict.get(key, 0) + value
       return merged_dict
   ```

### 9. Object-Oriented Programming: Class Creation (2 points)
   Define a `Car` class with attributes `make`, `model`, and `year`, and implement a method to display the car’s information.
   ```python
   class Car:
       def __init__(self, make, model, year):
           self.make = make
           self.model = model
           self.year = year

       def display_info(self):
           print(f"Car Info: {self.year} {self.make} {self.model}")
   ```

## Testing

To test each function, run the respective Python files or import the functions into an interactive Python shell. Verify that the functions work as expected with various test cases.

## Submission

1. **Push the Code**: Ensure that my solutions are pushed to my private GitHub repository.
2. **Include this README**: Make sure this `README.md` file is in the root directory of the repository.
3. **Provide the Repository Link**: Share the repository link with the assessment coordinator or submit it as required.

## Contact

If you have any questions or need assistance, please feel free to reach out to me at [hanningtonowiti@gmail.com].
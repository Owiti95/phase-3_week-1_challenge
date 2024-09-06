def decorator_func(func):
    def wrapper():
        print("Decorator Applied")
        return func()  # Calling the original function
    return wrapper

# Using the @ syntax for applying the decorator
@decorator_func
def sample_function():
    print("Calling the original function ")

# Calling the decorated function
sample_function()

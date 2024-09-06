def calculate_factorial(n):

    result = 1#this initializes the result to 1 because factorial of 0 is 1

    for i in range(1, n + 1):# loop from a range of 1 to 4. we add 1 to n so that the loop actually stops at n and not b4 n

        result = result * i # in every loop, we multiply the result(1) by every

    return result

user_int = int(input("Enter a number to get its factorial: "))

print(f"The factorial of {user_int} is {calculate_factorial(user_int)}")
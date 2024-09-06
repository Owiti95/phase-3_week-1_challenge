def reverse_string(text):# This function takes the text and returns it reversed.
    return text[::-1]

user_text = input("Enter a string to reverse: ")# Prompt the user to enter a text and store it in the variable 'user_text'

print(reverse_string(user_text))# Call the reverse_string function with the user_text as the argument

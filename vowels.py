def count_vowels(text):
    
    vowels = "aeiou"  # Defining a string containing all the vowels

    count = 0  # Initializing the counter to track the number of vowels

    for char in text.lower():  # Looping through each character in the input text

        if char in vowels:  # Checking if the character is a vowel

            count += 1  # If it is a vowel, increment the count by 1

    return count  # Return the total number of vowels found in the text

user_input = input("Enter a string to count the vowels: ")# Prompting the user to input text

print(f"Number of vowels: {count_vowels(user_input)}")#testing
















# def count_vowels():
#     vowels = "aeiou"

#     for i, thing in enumerate(vowels):
#         print(i, thing.lower())
# count_vowels()
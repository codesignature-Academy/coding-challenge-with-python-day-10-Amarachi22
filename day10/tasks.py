"""
Task 1 === Check if a String is a Pangram

Write a Python function to check whether a string is a pangram or not.

Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"

Task 2 === Print Even Numbers from a Given List

Write a Python program to print the even numbers from a given list.

Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]

"""
def is_pangram(sentence):
    sentence = sentence.lower() 
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet:
        if letter not in sentence:
            return False 
    return True  
text = "The quick brown fox jumps over the lazy dog"
print(is_pangram(text))









# def is_even():
#     numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
#     even_num = []
#     odd_num = []
#     for num in numbers:
#         if num % 2 == 0:
#             even_num.append(num)
#         else:
#             odd_num.append(num)
#     print(even_num)
#     print(odd_num)
# is_even()



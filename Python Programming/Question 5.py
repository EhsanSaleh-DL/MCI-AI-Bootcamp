# ----------------------------------------------------
# Title: Simple English Spell Checker
# Author: Ehsan Saleh
# Course: Python Programming
# Instructor: Dr. Jamal Kazazi
# Program: MCI AI Bootcamp (Generative AI with a Focus on Image Processing and Analysis)
# Date: 2026-07
# ----------------------------------------------------



import string

# Read the input text; For example: 
# The student wrote transfrd instead of transferred. Another wrong word is bcdfgh because it has six consecutive consonants.
text = input()

# Define the vowels
vowels = "aeiouyAEIOUY"

# Check each word in the text
for word in text.split():

    # Remove punctuation from the beginning and end of the word
    w = word.strip(string.punctuation)

    # Skip empty words
    if w == "":
        continue

    # Ignore words written entirely in uppercase (e.g., HTTPS)
    if w.isupper():
        continue

    # Counter for consecutive consonants
    cnt = 0

    # Flag to indicate whether the word is invalid
    wrong = False

    # Check each character in the word
    for ch in w:
        if ch.isalpha():
            if ch in vowels:
                # Reset the counter when a vowel is found
                cnt = 0
            else:
                # Increase the counter for a consonant
                cnt += 1

                # If there are 5 consecutive consonants,
                # mark the word as invalid
                if cnt >= 5:
                    wrong = True
                    break
        else:
            # Reset the counter if a non-letter is found
            cnt = 0

    # Print the invalid word
    if wrong:
        print("\n", w, end=" ")

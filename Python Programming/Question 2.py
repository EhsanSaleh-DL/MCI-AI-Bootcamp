#!/usr/bin/env python
# coding: utf-8

# In[2]:


# ----------------------------------------------------
# Title: Digit Extraction and Repetition
# Author: Ehsan Saleh
# Course: Python Programming
# Instructor: Dr. Jamal Kazazi
# Program: MCI AI Bootcamp (Generative AI with a Focus on Image Processing and Analysis)
# Date: 2026-07
# ----------------------------------------------------



m = int(input("Input a number: \n"))

digits = []

# Extract the digits from the number
while m>10:
    
    # Check if only the first two digits remain
    if m//10<10:
        r = m%10
        digits.append(r)
        digits.append(m//10)
        break
        
    # Get the last digit of the number
    r = m%10;
    
    # Add the digit to the list
    digits.append(r)
    
    # Remove the last digit from the number
    m = m//10
    
# Print the digits in their original order    
for r in reversed(digits):
    print(str(r) + ':', str(r) * r)
    


# In[ ]:





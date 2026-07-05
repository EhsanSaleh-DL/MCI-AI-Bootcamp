#!/usr/bin/env python
# coding: utf-8

# In[2]:


# ----------------------------------------------------
# Title: Finding the Next Power of Two
# Author: Ehsan Saleh
# Course: Python Programming
# Instructor: Dr. Jamal Kazazi
# Program: MCI AI Bootcamp (Generative AI with a Focus on Image Processing and Analysis)
# Date: 2026-07
# ----------------------------------------------------



num = int(input('Enter a number: \n'))

# Check powers of 2 from 2^0 to 2^108
for m in range(109):
    
    num_2 = 2**m
    
    # Check if the current power of 2 is greater than the user's number
    if num_2 > num:
        print('The first power of 2 greater than your number is:', num_2)
        break

# If no larger power of 2 was found, the number is at least 2^109        
if num_2 >= 2**109:
    print('The number you entered is greater than or equal to 2^109.')


# In[ ]:





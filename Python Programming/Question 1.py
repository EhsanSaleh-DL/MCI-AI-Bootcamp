#!/usr/bin/env python
# coding: utf-8

# In[3]:


# ----------------------------------------------------
# Title: Butterfly Pattern Using Asterisks
# Author: Ehsan Saleh
# Course: Python Programming
# Instructor: Dr. Jamal Kazazi
# Program: MCI AI Bootcamp (Generative AI with a Focus on Image Processing and Analysis)
# Date: 2026-07
# ----------------------------------------------------



# Keep asking until the user enters a valid odd number
while True:
    n = int(input("Please input an odd number between 1 and 19: "))
    if 1 <= n <= 19 and n % 2 == 1:
        break

    print("Invalid input! Please enter an odd number between 1 and 19.\n")


# Print an empty line for better output formatting
print("\n")

n = int(n)
itr = (n//2)+1
s = 1

# Print the upper half of the pattern
for i in range(itr):
    x1 = "*"*s
    print(x1.center(n)+x1.center(n))
    s = s + 2

# Print the lower half of the pattern
s = n
for i in range(itr-1):
    s = s-2
    x2 = "*"*s
    print(x2.center(n)+x2.center(n))


# In[ ]:





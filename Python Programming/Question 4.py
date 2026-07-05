# ----------------------------------------------------
# Title: Prime Factorization of an Integer
# Author: Ehsan Saleh
# Course: Python Programming
# Instructor: Dr. Jamal Kazazi
# Program: MCI AI Bootcamp (Generative AI with a Focus on Image Processing and Analysis)
# Date: 2026-07
# ----------------------------------------------------



n = int(input('Enter your number: \n'))

# Start checking from the smallest prime factor
i = 2

ans = []

while i * i <= n:
    
    # Count how many times the current factor divides n
    cnt = 0
    while n % i == 0:
        
        cnt = cnt + 1
        
        # Divide n by the current factor
        n = n // i

    # If the factor appears at least once, store it in the result list
    if cnt > 0:
        ans.append(f"{i}^{cnt}")
        
    # Move to the next possible factor
    i += 1
    
# If n is greater than 1, then it is the last prime factor
if n > 1:
    ans.append(f"{n}^1")

print("*".join(ans))

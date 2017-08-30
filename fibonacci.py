# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 17:56:16 2017

@author: LarsPetter

fibonacci
"""
# Python program to display the Fibonacci sequence up to n-th term using recursive functions

def recur_fibo(n):
   """Recursive function to
   print Fibonacci sequence"""
   if n <= 1:
       return n
   else:
       return(1/(recur_fibo(n-1) + recur_fibo(n-2)))

# Change this value for a different result
nterms = 50

# uncomment to take input from the user
#nterms = int(input("How many terms? "))

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))
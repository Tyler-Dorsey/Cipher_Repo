import numpy as np 
import math 
import pandas as pd 
import matplotlib.pyplot as plt 
from sympy import randprime 



####----------------------------------------------------------------------------####
# Title: THE OCTAVIAN CIPHER                                                       # 
# Author: Tyler Dorsey                                                             #
# Purpose: The Octavian Cipher is a poly-alphabetic cipher which has it's origins  # 
#          from the classic Caesar Cipher. Where the oringal Caesar Cipher used a  # 
#          single constant shift for each letter in the word to be encrypted, the  #
#          Octavian Cipher uses a product of prime number keys and a direcitonal   #
#          array that explains in which direction to shift per that given digit of #
#          the product key. The difficulty in breaking the original Caesar cipher  # 
#          was that of O(26) ~ O(1), while the Octavian Cipher has O(10^n/2)*2^n.  #                                                                                                                    
####----------------------------------------------------------------------------####

#------------------------------#
#--- Phrase To Be Encrypted ---#
#------------------------------# 

phrase = 'This is the phrase to be encrypted.' 
phrase = phrase.upper() 
phrase = phrase.replace(' ', '-') 
phrase_array = [char for char in phrase]
print(f'Phrase: {phrase}') 



#-------------------------#
#--- Create Master Key ---#
#-------------------------# 

def generate_random_prime(start = 0, end = 300000): 
    return randprime(start, end) 

key_1 = generate_random_prime() 

key_2 = generate_random_prime() 

master_key = key_1*key_2 
master_key_array = [int(digit) for digit in str(master_key)]


print(f'Master Key Value: {master_key}')   

# Ensure master_key_array is the same length as phrase_array
while len(master_key_array) < len(phrase_array):
    master_key_array += master_key_array  # Double the array size

# Trim excess elements if master_key_array is now longer
master_key_array = master_key_array[:len(phrase_array)]

print(f'Master Key Array: {master_key_array}')
print(f'Master Key Array Length: {len(master_key_array)}')
print(f'Phrase Array Length: {len(phrase_array)}')


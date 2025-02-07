import numpy as np 
import pandas as pd 
import math 
import matplotlib.pyplot as plt 

####----------------------------------------------------------------------------####
# Title: EXTENDED CEASAR CIPHER                                                    # 
# Author: Tyler Dorsey                                                             #
# Purpose: The ceasar cipher is one of the world's oldest ciphers. While it was a  #
#          success for it's day, it can be easily cracked. The extended Ceasar     #
#          cipher aims at taking the original cipher and making it harder to crack #
#          The product of two keys will be taken and each digit will be used to    #
#          shift each digit in the cipher.                                         #                                                           
####----------------------------------------------------------------------------#### 


# Phrase To Be Encrypted
word = 'Tyler is great. He is the best person that I know.'
word = word.upper()
word = word.replace('.','--')
word = word.replace(' ', '.')
print(f'Phrase: {word}')

#--- Establish Keys ---# 
key_1 = 22/7 
key_2 = math.e  
product_key = key_1 * key_2 
key_3 = 'fbfb'
print(f'Product of the keys: {product_key}') 

#--- Truncate Product Key ---# 
N = 13
factor = 10**N 
truncated_key = math.floor(factor * product_key) 
truncated_key = [char for char in str(truncated_key)]
print(f'Truncated Key: {truncated_key}') 

#--- Alphabet Matrix ---# 
alphabet_matrix = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# Truncated Key Check To Word Length
difference = abs(len(word)-len(truncated_key))

while len(word) != len(truncated_key):
    
    if difference > len(truncated_key):
        truncated_key += truncated_key 
        difference = abs(len(word)-len(truncated_key))
        
    elif difference < len(truncated_key): 
        truncated_key += truncated_key[:difference]
        difference = abs(len(word)-len(truncated_key))
        
    elif difference == 0: 
        break 
print(len(truncated_key))


if len(word) == len(truncated_key): 
    print('----------------------------------')
    print('SUCCESS: Word length and key length match')
    print(f'Word Length: {len(word)}')
    print(f'Key Length : {len(truncated_key)}')






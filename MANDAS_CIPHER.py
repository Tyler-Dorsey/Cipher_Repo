import numpy as np  
import pandas as pd 
import math 
import matplotlib.pyplot as plt      


####----------------------------------------------------------------------------####
# Title: THE MANDAS PARADIDDLE CIPHER                                              # 
# Author: Tyler Dorsey                                                             #
# Purpose: The Mandas Paradiddle Cipher is a poly-alphabetic cipher that arose from# 
#          the union of mathematics and music, specifically drumming patterns known# 
#          as paradiddles.                                                         #  
####----------------------------------------------------------------------------#### 

# Word or Phrase to be encrypted 
word = 'SECRET IS THE way to Go' 
word = word.upper() 
word = word.replace(" ", ".") 
word_array = [char for char in word]
print(f'This is the phrase to be encrypted: {word}')
#print(f'This is the array: {word_array}') 

# Paradiddle Key 
key = 'UDRL' 


#--- Extend Paradiddle Key ---# 
difference = abs(len(key) - len(word_array))

while len(word_array) != len(key): 
    if difference > len(key):
       key = key + key
       difference = abs(len(key) - len(word_array))
    elif difference < len(key): 
       key = key + key[:difference]
       difference = abs(len(key) - len(word_array))
    elif difference == 0: 
        break 
print(f'Key: {key}')

key_array = [char for char in key] 

# Word and Key Check 

if len(key_array) == len(word_array): 
    print('----------------------------------------')
    print(f'SUCCESS: Word and Key Length Match')
    print('----------------------------------------')
else: 
    print('----------------------------------------')
    print(f'FAILURE: Word and Key Length Do Not Match')
    print('----------------------------------------')


#--- Alphabet Matrix ---# 
A_Matrix = np.array([ 
                     ['A', 'B', 'C', 'D', 'E', 'M'],
                     ['G', 'H', 'I', 'J', 'K', 'N'],
                     ['O', 'P', 'Q', 'R', 'S', 'U'],
                     ['V', 'W', 'X', 'F', 'L', 'T'],
                     ['Z', 'Y', '#', '%', '&', '*']
                     ])  

#--------------------------------#
#----- ENCRYPTION ALGORITHM -----#
#--------------------------------# 
print(f'word array: {word_array}')
print(f'key array:  {key_array}')


cipher_array = []
n = 0 

for item in word_array: 
    if key_array[n] == 'U': 
       if item == 'A': 
           cipher_array.append('Z')
           n += 1 
       elif item == 'B': 
           cipher_array.append('Y')
           n += 1  
       elif item == 'C': 
           cipher_array.append('#') 
           n += 1
       elif item == 'D': 
           cipher_array.append('%')
           n += 1
       elif item == 'E': 
           cipher_array.append('&')
           n += 1 
       elif item == 'F': 
           cipher_array.append('R')
           n += 1
       elif item == 'G': 
           cipher_array.append('A')
           n += 1 
       elif item == 'H': 
           cipher_array.append('B')
           n += 1 
       elif item == 'I': 
           cipher_array.append('C')
           n += 1 
       elif item == 'J': 
           cipher_array.append('D')
           n += 1 
       elif item == 'K': 
           cipher_array.append('E')
           n += 1 
       elif item == 'L': 
           cipher_array.append('S')
           n += 1 
       elif item == 'M': 
           cipher_array.append('*') 
           n += 1 
       elif item == 'N': 
           cipher_array.append('M')
           n += 1 
       elif item == 'O': 
           cipher_array.append('G')
           n += 1 
       elif item == 'P': 
           cipher_array.append('H')
           n += 1 
       elif item == 'Q': 
           cipher_array.append('I')
           n += 1 
       elif item == 'R': 
           cipher_array.append('J')
           n += 1 
       elif item == 'S': 
           cipher_array.append('K')
           n += 1 
       elif item == 'T': 
           cipher_array.append('U')
           n += 1 
       elif item == 'U': 
           cipher_array.append('N')
           n += 1 
       elif item == 'V': 
           cipher_array.append('O')
           n += 1 
       elif item == 'W': 
           cipher_array.append('P')
           n += 1 
       elif item == 'X': 
           cipher_array.append('Q')
           n += 1 
       elif item == 'Y': 
           cipher_array.append('W')
           n += 1 
       elif item == 'Z': 
           cipher_array.append('V')                               
        
    else: 
        cipher_array.append('!')
        n += 1
print(cipher_array)       




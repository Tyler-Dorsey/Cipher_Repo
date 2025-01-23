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

cipher_array = []
n = 0 

for item in word_array: 
    if key_array[n] == 'U': 
       if item == 'T': 
           cipher_array.append('Z')
           n += 1 
       elif item == 'B': 
           cipher_array.append('Y')
           n += 1  
       elif item == 'S': 
           cipher_array.append('YEAHMAAAAN')
    else: 
        print('NOOOOO')
print(cipher_array)       




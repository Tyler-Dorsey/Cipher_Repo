import numpy as np  
import pandas as pd 
import math 
import matplotlib.pyplot as plt      


####----------------------------------------------------------------------------####
# Title: THE MANDAS PARADIDDLE CIPHER 2D                                              # 
# Author: Tyler Dorsey                                                             #
# Purpose: The Mandas Paradiddle Cipher is a poly-alphabetic cipher that arose from# 
#          the union of mathematics and music, specifically drumming patterns known# 
#          as paradiddles. This script is a 2-D version of the Mandas cipher.      #                                                           
####----------------------------------------------------------------------------#### 

# Word or Phrase to be encrypted 
word = 'Sherlock Holmes is the greatest detective.' 
word = word.upper() 
word = word.replace(" ", ".") 
word_array = [char for char in word]
print(f'This is the phrase to be encrypted: {word}')
#print(f'This is the array: {word_array}') 

# Paradiddle Key 
key = 'UDLR DDRL' 
key = key.upper()
key = key.replace(" ", "")

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

#----------------------------------------------------#
#--------------- ENCRYPTION ALGORITHM ---------------#
#----------------------------------------------------# 
print(f'word array: {word_array}')
print(f'key array:  {key_array}')

cipher_array = []
n = 0 

for item in word_array: 
    #-------------------------------#
    #--- Takes Care of 'UP' Case ---#
    #-------------------------------#
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
           n += 1
       elif item == '.': 
           cipher_array.append('.')
           n += 1
    #---------------------------------#
    #--- Takes Care of 'DOWN' Case ---#
    #---------------------------------#  
    elif key_array[n] == 'D': 
        if item == 'A': 
           cipher_array.append('G')
           n += 1 
        elif item == 'B': 
           cipher_array.append('H')
           n += 1  
        elif item == 'C': 
           cipher_array.append('I') 
           n += 1
        elif item == 'D': 
           cipher_array.append('J')
           n += 1
        elif item == 'E': 
           cipher_array.append('K')
           n += 1 
        elif item == 'F': 
           cipher_array.append('%')
           n += 1
        elif item == 'G': 
           cipher_array.append('O')
           n += 1 
        elif item == 'H': 
           cipher_array.append('P')
           n += 1 
        elif item == 'I': 
           cipher_array.append('Q')
           n += 1 
        elif item == 'J': 
           cipher_array.append('R')
           n += 1 
        elif item == 'K': 
           cipher_array.append('S')
           n += 1 
        elif item == 'L': 
           cipher_array.append('&')
           n += 1 
        elif item == 'M': 
           cipher_array.append('N') 
           n += 1 
        elif item == 'N': 
           cipher_array.append('U')
           n += 1 
        elif item == 'O': 
           cipher_array.append('V')
           n += 1 
        elif item == 'P': 
           cipher_array.append('W')
           n += 1 
        elif item == 'Q': 
           cipher_array.append('X')
           n += 1 
        elif item == 'R': 
           cipher_array.append('F')
           n += 1 
        elif item == 'S': 
           cipher_array.append('L')
           n += 1 
        elif item == 'T': 
           cipher_array.append('*')
           n += 1 
        elif item == 'U': 
           cipher_array.append('T')
           n += 1 
        elif item == 'V': 
           cipher_array.append('Z')
           n += 1 
        elif item == 'W': 
           cipher_array.append('Y')
           n += 1 
        elif item == 'X': 
           cipher_array.append('#')
           n += 1 
        elif item == 'Y': 
           cipher_array.append('B')
           n += 1 
        elif item == 'Z': 
           cipher_array.append('A')
           n += 1
        elif item == '.': 
           cipher_array.append('.')
           n += 1
    #----------------------------------#
    #--- Takes Care of 'RIGHT' Case ---#
    #----------------------------------#
    elif key_array[n] == 'R': 
        if item == 'A': 
           cipher_array.append('B')
           n += 1 
        elif item == 'B': 
           cipher_array.append('H')
           n += 1  
        elif item == 'C': 
           cipher_array.append('I') 
           n += 1
        elif item == 'D': 
           cipher_array.append('J')
           n += 1
        elif item == 'E': 
           cipher_array.append('K')
           n += 1 
        elif item == 'F': 
           cipher_array.append('%')
           n += 1
        elif item == 'G': 
           cipher_array.append('O')
           n += 1 
        elif item == 'H': 
           cipher_array.append('P')
           n += 1 
        elif item == 'I': 
           cipher_array.append('Q')
           n += 1 
        elif item == 'J': 
           cipher_array.append('R')
           n += 1 
        elif item == 'K': 
           cipher_array.append('S')
           n += 1 
        elif item == 'L': 
           cipher_array.append('&')
           n += 1 
        elif item == 'M': 
           cipher_array.append('N') 
           n += 1 
        elif item == 'N': 
           cipher_array.append('U')
           n += 1 
        elif item == 'O': 
           cipher_array.append('V')
           n += 1 
        elif item == 'P': 
           cipher_array.append('W')
           n += 1 
        elif item == 'Q': 
           cipher_array.append('X')
           n += 1 
        elif item == 'R': 
           cipher_array.append('F')
           n += 1 
        elif item == 'S': 
           cipher_array.append('L')
           n += 1 
        elif item == 'T': 
           cipher_array.append('*')
           n += 1 
        elif item == 'U': 
           cipher_array.append('T')
           n += 1 
        elif item == 'V': 
           cipher_array.append('Z')
           n += 1 
        elif item == 'W': 
           cipher_array.append('Y')
           n += 1 
        elif item == 'X': 
           cipher_array.append('#')
           n += 1 
        elif item == 'Y': 
           cipher_array.append('B')
           n += 1 
        elif item == 'Z': 
           cipher_array.append('A')
           n += 1
        elif item == '.': 
           cipher_array.append('.')
           n += 1
    #----------------------------------#
    #--- Takes Care of 'LEFT' Case ----#
    #----------------------------------#
    elif key_array[n] == 'L': 
        if item == 'A': 
           cipher_array.append('M')
           n += 1 
        elif item == 'B': 
           cipher_array.append('A')
           n += 1  
        elif item == 'C': 
           cipher_array.append('B') 
           n += 1
        elif item == 'D': 
           cipher_array.append('C')
           n += 1
        elif item == 'E': 
           cipher_array.append('D')
           n += 1 
        elif item == 'F': 
           cipher_array.append('X')
           n += 1
        elif item == 'G': 
           cipher_array.append('N')
           n += 1 
        elif item == 'H': 
           cipher_array.append('G')
           n += 1 
        elif item == 'I': 
           cipher_array.append('H')
           n += 1 
        elif item == 'J': 
           cipher_array.append('I')
           n += 1 
        elif item == 'K': 
           cipher_array.append('J')
           n += 1 
        elif item == 'L': 
           cipher_array.append('F')
           n += 1 
        elif item == 'M': 
           cipher_array.append('E') 
           n += 1 
        elif item == 'N': 
           cipher_array.append('K')
           n += 1 
        elif item == 'O': 
           cipher_array.append('U')
           n += 1 
        elif item == 'P': 
           cipher_array.append('O')
           n += 1 
        elif item == 'Q': 
           cipher_array.append('P')
           n += 1 
        elif item == 'R': 
           cipher_array.append('Q')
           n += 1 
        elif item == 'S': 
           cipher_array.append('R')
           n += 1 
        elif item == 'T': 
           cipher_array.append('L')
           n += 1 
        elif item == 'U': 
           cipher_array.append('S')
           n += 1 
        elif item == 'V': 
           cipher_array.append('T')
           n += 1 
        elif item == 'W': 
           cipher_array.append('V')
           n += 1 
        elif item == 'X': 
           cipher_array.append('W')
           n += 1 
        elif item == 'Y': 
           cipher_array.append('Z')
           n += 1 
        elif item == 'Z': 
           cipher_array.append('*')
           n += 1
        elif item == '.':
           cipher_array.append('&')
           n += 1 
        
    else: 
        cipher_array.append('!')
        n += 1
print(f'Encrypted Array: {cipher_array}')

encrypted_string =''.join(cipher_array)
print('-------------------------------------------------------------------------------------')
print(f'Encrypted Message: {encrypted_string}') 
print('-------------------------------------------------------------------------------------')


#print(f'{len(encrypted_string)}  {len(key_array)}')    

#--- Create Opposite Decryption Paradiddle Key ---#

new_key = []

for item in key_array: 
    if item == 'U':
        new_key.append('D')
    elif item == 'D':
        new_key.append('U')
    elif item == 'R': 
        new_key.append('L')
    elif item == 'L': 
        new_key.append('R')
        
new_key_1 = ''.join(new_key)
key_array_1 = ''.join(key_array)
if len(new_key) == len(key_array): 
    print(f'New Key Array: {new_key_1}')
    print('--------------------------------------')
    print(f'Old Key Array: {key_array_1}')
    print('SUCCESS: OLD AND NEW KEY LENGTHS MATCH')
    print('--------------------------------------')
    
    
#----------------------------------------------------#
#--------------- DECRYPTION ALGORITHM ---------------#
#----------------------------------------------------# 

decrypted_array = []
n = 0

for item in cipher_array: 
    #-------------------------------#
    #--- Takes Care of 'UP' Case ---#
    #-------------------------------#
    if key_array[n] == 'U': 
       if item == 'Z': 
           decrypted_array.append('A')
           n += 1 
       elif item == 'Y': 
           decrypted_array.append('B')
           n += 1  
       elif item == '#': 
           decrypted_array.append('C') 
           n += 1
       elif item == '%': 
           decrypted_array.append('')
           n += 1
       elif item == '&': 
           decrypted_array.append('E')
           n += 1 
       elif item == 'R': 
           decrypted_array.append('F')
           n += 1
       elif item == 'A': 
           decrypted_array.append('G')
           n += 1 
       elif item == 'B': 
           decrypted_array.append('H')
           n += 1 
       elif item == 'C': 
           decrypted_array.append('I')
           n += 1 
       elif item == 'D': 
           decrypted_array.append('J')
           n += 1 
       elif item == 'E': 
           decrypted_array.append('K')
           n += 1 
       elif item == 'S': 
           decrypted_array.append('L')
           n += 1 
       elif item == '*': 
           decrypted_array.append('M') 
           n += 1 
       elif item == 'M': 
           decrypted_array.append('N')
           n += 1 
       elif item == 'G': 
           decrypted_array.append('O')
           n += 1 
       elif item == 'H': 
           decrypted_array.append('P')
           n += 1 
       elif item == 'I': 
           decrypted_array.append('Q')
           n += 1 
       elif item == 'J': 
           decrypted_array.append('R')
           n += 1 
       elif item == 'K': 
           decrypted_array.append('S')
           n += 1 
       elif item == 'U': 
           decrypted_array.append('T')
           n += 1 
       elif item == 'N': 
           decrypted_array.append('U')
           n += 1 
       elif item == 'O': 
           decrypted_array.append('V')
           n += 1 
       elif item == 'P': 
           decrypted_array.append('W')
           n += 1 
       elif item == 'Q': 
           decrypted_array.append('X')
           n += 1 
       elif item == 'W': 
           decrypted_array.append('Y')
           n += 1 
       elif item == 'V': 
           decrypted_array.append('Z')   
           n += 1
       elif item == '.': 
           decrypted_array.append('.')
           n += 1
    
    #---------------------------------#
    #--- Takes Care of 'DOWN' Case ---#
    #---------------------------------#
    elif key_array[n] == 'D': 
        if item == 'G': 
           decrypted_array.append('A')
           n += 1 
        elif item == 'H': 
           decrypted_array.append('B')
           n += 1  
        elif item == 'I': 
           decrypted_array.append('C') 
           n += 1
        elif item == 'J': 
           decrypted_array.append('D')
           n += 1
        elif item == 'K': 
           decrypted_array.append('E')
           n += 1 
        elif item == '%': 
           decrypted_array.append('F')
           n += 1
        elif item == 'O': 
           decrypted_array.append('G')
           n += 1 
        elif item == 'P': 
           decrypted_array.append('H')
           n += 1 
        elif item == 'Q': 
           decrypted_array.append('I')
           n += 1 
        elif item == 'R': 
           decrypted_array.append('J')
           n += 1 
        elif item == 'S': 
           decrypted_array.append('K')
           n += 1 
        elif item == '&': 
           decrypted_array.append('L')
           n += 1 
        elif item == 'N': 
           decrypted_array.append('M') 
           n += 1 
        elif item == 'U': 
           decrypted_array.append('N')
           n += 1 
        elif item == 'V': 
           decrypted_array.append('O')
           n += 1 
        elif item == 'W': 
           decrypted_array.append('P')
           n += 1 
        elif item == 'X': 
           decrypted_array.append('Q')
           n += 1 
        elif item == 'F': 
           decrypted_array.append('R')
           n += 1 
        elif item == 'L': 
           decrypted_array.append('S')
           n += 1 
        elif item == '*': 
           decrypted_array.append('T')
           n += 1 
        elif item == 'T': 
           decrypted_array.append('U')
           n += 1 
        elif item == 'Z': 
           decrypted_array.append('V')
           n += 1 
        elif item == 'Y': 
           decrypted_array.append('W')
           n += 1 
        elif item == '#': 
           decrypted_array.append('X')
           n += 1 
        elif item == 'B': 
           decrypted_array.append('Y')
           n += 1 
        elif item == 'A': 
           decrypted_array.append('Z')
           n += 1
        elif item == '.': 
           decrypted_array.append('.')
           n += 1
           
    #----------------------------------#
    #--- Takes Care of 'RIGHT' Case ---#
    #----------------------------------#
    elif key_array[n] == 'R': 
        if item == 'B': 
           decrypted_array.append('A')
           n += 1 
        elif item == 'H': 
           decrypted_array.append('B')
           n += 1  
        elif item == 'I': 
           decrypted_array.append('C') 
           n += 1
        elif item == 'J': 
           decrypted_array.append('D')
           n += 1
        elif item == 'K': 
           decrypted_array.append('E')
           n += 1 
        elif item == '%': 
           decrypted_array.append('F')
           n += 1
        elif item == 'O': 
           decrypted_array.append('G')
           n += 1 
        elif item == 'P': 
           decrypted_array.append('H')
           n += 1 
        elif item == 'Q': 
           decrypted_array.append('I')
           n += 1 
        elif item == 'R': 
           decrypted_array.append('J')
           n += 1 
        elif item == 'S': 
           decrypted_array.append('K')
           n += 1 
        elif item == '&': 
           decrypted_array.append('L')
           n += 1 
        elif item == 'N': 
           decrypted_array.append('M') 
           n += 1 
        elif item == 'U': 
           decrypted_array.append('N')
           n += 1 
        elif item == 'V': 
           decrypted_array.append('O')
           n += 1 
        elif item == 'W': 
           decrypted_array.append('P')
           n += 1 
        elif item == 'X': 
           decrypted_array.append('Q')
           n += 1 
        elif item == 'F': 
           decrypted_array.append('R')
           n += 1 
        elif item == 'L': 
           decrypted_array.append('S')
           n += 1 
        elif item == '*': 
           decrypted_array.append('T')
           n += 1 
        elif item == 'T': 
           decrypted_array.append('U')
           n += 1 
        elif item == 'Z': 
           decrypted_array.append('V')
           n += 1 
        elif item == 'Y': 
           decrypted_array.append('W')
           n += 1 
        elif item == '#': 
           decrypted_array.append('X')
           n += 1 
        elif item == 'B': 
           decrypted_array.append('Y')
           n += 1 
        elif item == 'A': 
           decrypted_array.append('Z')
           n += 1
        elif item == '.': 
           decrypted_array.append('.')
           n += 1
    #----------------------------------#
    #--- Takes Care of 'LEFT' Case ----#
    #----------------------------------#
    elif key_array[n] == 'L': 
        if item == 'M': 
           decrypted_array.append('A')
           n += 1 
        elif item == 'A': 
           decrypted_array.append('B')
           n += 1  
        elif item == 'B': 
           decrypted_array.append('C') 
           n += 1
        elif item == 'C': 
           decrypted_array.append('D')
           n += 1
        elif item == 'D': 
           decrypted_array.append('E')
           n += 1 
        elif item == 'X': 
           decrypted_array.append('F')
           n += 1
        elif item == 'N': 
           decrypted_array.append('G')
           n += 1 
        elif item == 'G': 
           decrypted_array.append('H')
           n += 1 
        elif item == 'H': 
           decrypted_array.append('I')
           n += 1 
        elif item == 'I': 
           decrypted_array.append('J')
           n += 1 
        elif item == 'J': 
           decrypted_array.append('K')
           n += 1 
        elif item == 'F': 
           decrypted_array.append('L')
           n += 1 
        elif item == 'E': 
           decrypted_array.append('M') 
           n += 1 
        elif item == 'K': 
           decrypted_array.append('N')
           n += 1 
        elif item == 'U': 
           decrypted_array.append('O')
           n += 1 
        elif item == 'O': 
           decrypted_array.append('P')
           n += 1 
        elif item == 'P': 
           decrypted_array.append('Q')
           n += 1 
        elif item == 'Q': 
           decrypted_array.append('R')
           n += 1 
        elif item == 'R': 
           decrypted_array.append('S')
           n += 1 
        elif item == 'L': 
           decrypted_array.append('T')
           n += 1 
        elif item == 'S': 
           decrypted_array.append('U')
           n += 1 
        elif item == 'T': 
           decrypted_array.append('V')
           n += 1 
        elif item == 'V': 
           decrypted_array.append('W')
           n += 1 
        elif item == 'W': 
           decrypted_array.append('X')
           n += 1 
        elif item == 'Z': 
           decrypted_array.append('Y')
           n += 1 
        elif item == '*': 
           decrypted_array.append('Z')
           n += 1
        elif item == '&':
           decrypted_array.append('.')
           n += 1 
    
    else:
        decrypted_array.append('VOID') 
        n += 1

decrypted_array = ''.join(decrypted_array)
print(f'Decrypted Array: {decrypted_array}')
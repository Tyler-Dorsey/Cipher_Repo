import numpy as np  
import pandas as pd 
import math 
import matplotlib.pyplot as plt      


####----------------------------------------------------------------------------####
# Title: THE MANDAS PARADIDDLE CIPHER 3D (Tensor Version)                          # 
# Author: Tyler Dorsey                                                             #
# Purpose: The Mandas Paradiddle Cipher is a poly-alphabetic cipher that arose from# 
#          the union of mathematics and music, specifically drumming patterns known# 
#          as paradiddles. This script is a 3-D version of the Mandas cipher.      #                                                           
####----------------------------------------------------------------------------#### 

# Word or Phrase to be encrypted 
word = 'Sherlock Holmes is the greatest detective.' 
word = word.upper() 
word = word.replace(" ", ".") 
word_array = [char for char in word]
print(f'This is the phrase to be encrypted: {word}')
#print(f'This is the array: {word_array}') 

# Paradiddle Key 
key = 'UDRL DUIO'
key = key.upper()
key = key.replace(' ','')
print(f'Key: {key}')

#--- Extend Paradiddle Key ---# 
difference = abs(len(word_array) - len(key))

while len(word_array) != len(key):
    if difference > len(key): 
        key = key + key  
        difference = abs(len(word_array) - len(key))
    elif difference < len(key): 
        key = key + key[:difference]
        difference = abs(len(word_array) - len(key))
    elif difference == 0: 
        break 
print(f'Extended Key: {key}') 

extended_key = [char for char in key]
print(extended_key)
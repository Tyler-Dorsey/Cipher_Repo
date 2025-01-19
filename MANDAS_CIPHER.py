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
word = ''.join(word.split()) 

print(f'This is the phrase to be encrypted: {word}') 

# Paradiddle Key 
key = 'UDRL' 

# Extend Paradiddle Key to Match Phrase Length 

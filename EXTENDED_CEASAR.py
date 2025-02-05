import numpy as np 
import pandas as pd 
import math 
import matplotlib.pyplot as plt 

####----------------------------------------------------------------------------####
# Title: EXTENDED CEASAR CIPHER                                                    # 
# Author: Tyler Dorsey                                                             #
# Purpose: The ceasar cipher is one of the world's moldest ciphers. While it was a #
#          success for it's day, it can be easily cracked. The extended Ceasar     #
#          cipher aims at taking the original cipher and making it harder to crack #
#          The product of two keys will be taken and each digit will be used to    #
#          shift each digit in the cipher.                                         #                                                           
####----------------------------------------------------------------------------#### 


#--- Establish Keys ---# 
key_1 = 22/7 
key_2 = math.e  
product_key = key_1 * key_2 
print(f'Product of the keys: {product_key}') 

#--- Truncate Product Key ---# 
N = 13
factor = 10**N 
truncated_key = math.floor(factor * product_key) 
print(f'Truncated Key: {truncated_key}')


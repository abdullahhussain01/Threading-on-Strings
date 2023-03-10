# -*- coding: utf-8 -*-
"""200901042_Assign_04.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1r7g4X15rLRcnZTjQd_phJfOm9Lrc01GF
"""

#Abdullah Hussain
#200901042
import threading

string = ""  

def input_thread():
    global string  
    while True:
        try:
            
            string = input("Enter a string: ")
            if not string.isalpha():
                raise ValueError("Input must be a string")
        except ValueError as e:
            print(e)
        else:
            break
    
    reverse_thread.start()
    capital_thread.start()
    shift_thread.start()

def reverse_thread():
    global string  
    try:
        
        reversed_string = string[::-1]
        print("Reversed string:", reversed_string)
    except Exception as e:
        
        print("Exception occurred in reverse thread:", e)

def capital_thread():
    global string  
    try:
       
        capitalized_string = string.upper()
        print("Capitalized string:", capitalized_string)
    except Exception as e:
        
        print("Exception occurred in capital thread:", e)

def shift_thread():
    global string  
    try:
      
        shifted_string = ""
        for char in string:
            shifted_string += chr(ord(char) + 2)
        print("Shifted string:", shifted_string)
    except Exception as e:
        
        print("Exception occurred in shift thread:", e)
# Create the threads
input_thread = threading.Thread(target=input_thread)
reverse_thread = threading.Thread(target=reverse_thread)
capital_thread = threading.Thread(target=capital_thread)
shift_thread = threading.Thread(target=shift_thread)


input_thread.start()


input_thread.join()
reverse_thread.join()
capital_thread.join()
shift_thread.join()
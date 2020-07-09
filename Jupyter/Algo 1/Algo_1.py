from PIL import Image
import cv2
import numpy as np
import encryption as en


# Converts String to Characters
def str_char(string):
    l = list(string)
    return l
    
    
#Converts charcters to ASCII values    
def ascii_array(list):
    new_list = []
    bin_list = []
    for i in list:
        new_list.append(int(ord(i)))
    
    return new_list

#Converts decimal values to a string of binary charcters
def ascii_to_bin(Temp):
    Bin = []
    for i in Temp:
        Bin.append(bin(i)[2:])
    return Bin



#This Funtion performs the TMM method shown in Fig 3 of the reading
def BintoTemp(bin_array):
    temp_array = []
    temp_array.append(bin_array[0])
    for i in range(0,len(bin_array)-1):
        temp_array.append(bin_array[i+1] ^ temp_array[i])
    return temp_array


#Key Matrix generator turns list into matrix
def Matrix_Gen(Temp):
    Bin = []
    for i in Temp:
        Bin.append(bin(i)[2:])
        
    #separates last element into a string of characters in binary   
    my_list = [char for char in Bin[len(Bin)-1]]
    
   #Converts char to int
    num_list = []
    for j in range(0,5):
        num_list.append(int(my_list[j]))
    # Add zero to the front
    i = 0
    
    while len(num_list) < 9:
        num_list.insert(i,0)
        i = i + 1
        
    matrix = []    
    while num_list != []: 
        matrix.append(num_list[:3])
        num_list = num_list[3:] 
  
    return matrix
            
def encryption_algorithm(msg,n):
    
    secret_msg = str_char(msg)
    
    msg_array = ascii_array(secret_msg)
    
    
    #TMM method
    binary_array = BintoTemp(msg_array)
   
    
    Bin = []
    for i in binary_array:
        Bin.append(bin(i)[2:])
        
    #separates last element into a string of characters    
    my_list = [char for char in Bin[n-1]]
    
  
    #Converts char to int
    num_list = []
    for j in range(0,len(Bin[n-1])):
        num_list.append(int(my_list[j]))
    # Add zero to the front
    i = 0
    
    while len(num_list) < 9:
        num_list.insert(i,0)
        i = i + 1
        
    matrix = []    
    while num_list != []: 
        matrix.append(num_list[:3])
        num_list = num_list[3:]
        
    if  n%3 == 0:
        print("Encryption_1")
    if n%3 == 1:
        print("Encryption_2")
    if n%3 == 2:
        print("Encryption_3")
        
    return matrix
   
    
################################################################################################################################
# Password encryption

test_list = str_char("SECRET")

bin_array = ascii_array(test_list)

Temp = BintoTemp(bin_array)

key_matrix = Matrix_Gen(Temp)

#print(key_matrix)

# Let secret message be "HELLO"

msg = "HELLO"

encryption_algorithm(msg,1)









    





       
       
        
        

       
       
        
        
    

        

        



    













    


 






    



    









                        




                        
                     
                        
                        
            














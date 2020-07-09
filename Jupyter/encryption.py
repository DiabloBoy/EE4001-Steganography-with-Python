from PIL import Image
import cv2
import numpy as np

#This function rotates a matrix clockwise
def rotate90Clockwise(A): 
    N = len(A[0]) 
    for i in range(N // 2): 
        for j in range(i, N - i - 1): 
            temp = A[i][j] 
            A[i][j] = A[N - 1 - j][i] 
            A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j] 
            A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i] 
            A[j][N - 1 - i] = temp
    return A

#This function rotates a matric anticlockwise
def rotate_90_degree_anticlockwise(matrix):
    new_matrix = []
    for i in range(len(matrix[0]), 0, -1):
        new_matrix.append(list(map(lambda x: x[i-1], matrix)))

    return new_matrix


# This function performs the operation shown in Fig 4. of the reading
def xor_matrix(B,key_matrix):
    temp_array = []
    for i in range(0,3):
        temp_array.append(B[0][i] ^ key_matrix[0][i])
    for j in range(0,3):
        temp_array.append(B[1][j] ^ key_matrix[1][j])
    for k in range(0,3):
        temp_array.append(B[2][k] ^ key_matrix[2][k])
    eight_bit_array = temp_array[1:]
    return eight_bit_array

# This function peforms XOR operation between 2 matrices and returns a matrix
def xor_matrix_decrypt(B,key_matrix):
    temp_array = []
    for i in range(0,3):
        temp_array.append(B[0][i] ^ key_matrix[0][i])
    for j in range(0,3):
        temp_array.append(B[1][j] ^ key_matrix[1][j])
    for k in range(0,3):
        temp_array.append(B[2][k] ^ key_matrix[2][k])
    matrix = []   
    
    while temp_array != []: 
        matrix.append(temp_array [:3])
        temp_array  = temp_array [3:] 
  
    return matrix
    

# This function ads integer zeros to the front of a list
def list_appender(num_list):
    i = 0
    while len(num_list) < 8:
        num_list.insert(i,0)
        i = i + 1
    return num_list

#This function converts a binary string to decimal
def str_convert(list):
    new_list = []
    ans = ""
    value = 0
    for i in list:
        new_list.append(str(i))
    ans = ''.join(new_list)
    value = int(ans,2)
    return value


def encryption_1(im,char_n,x,y):
    value  = im.getpixel((x,y))
    
    #print(value)
    
    RED =  list(bin(value[0]))
    GREEN = list(bin(value[1]))
    BLUE = value[2]
    
    RED_1 = RED[2:]
    GREEN_1 = GREEN[2:]
    
    new_red = []
    new_green = []
    
    for i in RED_1:
        new_red.append(int(i))
    for i in GREEN_1:
        new_green.append(int(i))
    eight_bit_red  = list_appender(new_red)
    eight_bit_green = list_appender(new_green)
    
    red_unchanged = eight_bit_red[:4]
    green_unchanged = eight_bit_green[:4]

    RED_NEW = red_unchanged + char_n[:4]
    GREEN_NEW = green_unchanged + char_n[4:]
    
    PUT_RED = str_convert(RED_NEW)
    PUT_GREEN = str_convert(GREEN_NEW)
    
    im.putpixel((x,y),(PUT_RED,PUT_GREEN,BLUE))
    
    return im

def encryption_2(im,char_n,x,y):
    
    value  = im.getpixel((x,y))
    
    RED =  value[0]
    GREEN = list(bin(value[1]))
    BLUE = list(bin(value[2]))
    
    #print(value)
    
    
    GREEN_1 = GREEN[2:]
    BLUE_1 = BLUE[2:]
    
    
    new_green = []
    new_blue = []
    
    for i in GREEN_1:
        new_green.append(int(i))
    for i in BLUE_1:
        new_blue.append(int(i))
        
    eight_bit_green  = list_appender(new_green)
    eight_bit_blue = list_appender(new_blue)
    
    green_unchanged = eight_bit_green[:4]
    blue_unchanged = eight_bit_blue[:4]

    GREEN_NEW = green_unchanged + char_n[:4]
    BLUE_NEW = blue_unchanged + char_n[4:]
    
    PUT_GREEN = str_convert(GREEN_NEW)
    PUT_BLUE = str_convert(BLUE_NEW)
    
    im.putpixel((x,y),(RED,PUT_GREEN,PUT_BLUE))
    
    return im  

def encryption_3(im,char_n,x,y):
    
    value  = im.getpixel((x,y))
    
    RED =  list(bin(value[0]))
    GREEN = value[1]
    BLUE = list(bin(value[2]))
    
    #print(value)
    
    
    RED_1 = RED[2:]
    BLUE_1 = BLUE[2:]
    
    
    new_red = []
    new_blue = []
    
    for i in RED_1:
        new_red.append(int(i))
    for i in BLUE_1:
        new_blue.append(int(i))
        
    eight_bit_red  = list_appender(new_red)
    eight_bit_blue = list_appender(new_blue)
    
    red_unchanged = eight_bit_red[:4]
    blue_unchanged = eight_bit_blue[:4]

    RED_NEW = red_unchanged + char_n[:4]
    BLUE_NEW = blue_unchanged + char_n[4:]
    
    PUT_RED = str_convert(RED_NEW)
    PUT_BLUE = str_convert(BLUE_NEW)
    
    im.putpixel((x,y),(PUT_RED,GREEN,PUT_BLUE))
    
    
    return im   



def decryption_1(stego,key_matrix,x,y):
    
    new_value = stego.getpixel((x,y))
    
    print(new_value)
    
    RED =  list(bin(new_value[0]))
    GREEN = list(bin(new_value[1]))
    
    RED_1 = RED[2:]
    GREEN_1 = GREEN[2:]
    
    new_red = []
    new_green = []
    
    for i in RED_1:
        new_red.append(int(i))
    for i in GREEN_1:
        new_green.append(int(i))
        
    eight_bit_red  = list_appender(new_red)
    eight_bit_green = list_appender(new_green)
    
    red_nibble = eight_bit_red[4:]
    green_nibble = eight_bit_green[4:]
    
    new_list = red_nibble + green_nibble
    
    new_list.insert(0,0)
    
    matrix = [] 
    while new_list != []: 
        matrix.append(new_list[:3])
        new_list = new_list[3:]
        
    my_matrix = xor_matrix_decrypt(matrix,key_matrix)
    final = rotate_90_degree_anticlockwise(my_matrix)
    
    decoded_array = []
    
    for i in range(1,3):
        decoded_array.append(final[0][i])
        
    for i in range(0,3):
        decoded_array.append(final[1][i])
        
    for i in range(0,3):
        decoded_array.append(final[2][i])
        
    string_array = []
    
    for i in decoded_array:
        string_array.append(str(i))
        
    binary_string = "".join(string_array)
    letter = int(binary_string,2)
    
    return chr(letter)

def decryption_2(stego,key_matrix,x,y):
    
    new_value = stego.getpixel((x,y))
    
    print(new_value)
    
   
    GREEN = list(bin(new_value[1]))
    BLUE = list(bin(new_value[2]))
    
   
    GREEN_1 = GREEN[2:]
    BLUE_1 = BLUE[2:]
    
   
    new_green = []
    new_blue = []
    
    for i in BLUE_1:
        new_blue.append(int(i))
    for i in GREEN_1:
        new_green.append(int(i))
        
    eight_bit_blue  = list_appender(new_blue)
    eight_bit_green = list_appender(new_green)
    
    blue_nibble = eight_bit_blue[4:]
    green_nibble = eight_bit_green[4:]
    
    new_list =  green_nibble + blue_nibble
    
    new_list.insert(0,0)
    
    matrix = [] 
    while new_list != []: 
        matrix.append(new_list[:3])
        new_list = new_list[3:]
        
    my_matrix = xor_matrix_decrypt(matrix,key_matrix)
    final = rotate_90_degree_anticlockwise(my_matrix)
    
    decoded_array = []
    
    for i in range(1,3):
        decoded_array.append(final[0][i])
        
    for i in range(0,3):
        decoded_array.append(final[1][i])
        
    for i in range(0,3):
        decoded_array.append(final[2][i])
        
    string_array = []
    
    for i in decoded_array:
        string_array.append(str(i))
        
    binary_string = "".join(string_array)
    letter = int(binary_string,2)
    
    return chr(letter)

def decryption_3(stego,key_matrix,x,y):
    
    new_value = stego.getpixel((x,y))
    
    print(new_value)
    
   
    RED = list(bin(new_value[0]))
    BLUE = list(bin(new_value[2]))
    
   
    RED_1 = RED[2:]
    BLUE_1 = BLUE[2:]
    
   
    new_red = []
    new_blue = []
    
    for i in RED_1:
        new_red.append(int(i))
    for i in BLUE_1:
        new_blue.append(int(i))
        
    eight_bit_blue  = list_appender(new_blue)
    eight_bit_red = list_appender(new_red)
    
    blue_nibble = eight_bit_blue[4:]
    red_nibble = eight_bit_red[4:]
    
    new_list = red_nibble + blue_nibble
    
    new_list.insert(0,0)
    
    matrix = [] 
    while new_list != []: 
        matrix.append(new_list[:3])
        new_list = new_list[3:]
        
    my_matrix = xor_matrix_decrypt(matrix,key_matrix)
    final = rotate_90_degree_anticlockwise(my_matrix)
    
    decoded_array = []
    
    for i in range(1,3):
        decoded_array.append(final[0][i])
        
    for i in range(0,3):
        decoded_array.append(final[1][i])
        
    for i in range(0,3):
        decoded_array.append(final[2][i])
        
    string_array = []
    
    for i in decoded_array:
        string_array.append(str(i))
        
    binary_string = "".join(string_array)
    letter = int(binary_string,2)
    
    return chr(letter)










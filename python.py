# PRINTING
# print('Welcome to python')
# print('Welcome to python!!!!!')

# NAMING VARIABLES AND PRINTING ASSIGNMENTS
#item_name = 'strawberry'
#price = 2.39
#inventory = 15
#is_in_inventory = True
#print(item_name, price, inventory)

# BASIC ARITHMETIC OPERATIONS
#a=6
# b=2
# print('Addition : ', a + b)
# print('Subtraction : ', a - b)
# print('Multiplication : ', a * b)
# print('Division (float) : ', a / b)
# print('Division (floor) : ', a // b)
# print('Modulus : ', a % b)
# print('Exponent : ', a ** b)

# STRING BASICS/SLICING
msg='welcome to python'
    #0123456789 
# print(msg)
# WANT IT TO PRINT TWICE?
# print(msg+msg)
# print(msg*2)
# print(msg,msg)
#WANT TO CHANGE CASING?
# print(msg.upper())
# print(msg.lower())
# print(msg.capitalize())
# print(msg.title())
# WANT TO KNOW INFO ABOUT STRING?
# print(len(msg))
# print(msg.count('python'))
# SLICING STRINGS
    # THE WAY TO ACCESS NUMBERS IS BY USING []
# print(msg[4])
    # CAN ALSO USE NEGATIVE INDEXES(-)
# print(msg[-3])
    # WANT TO GRAB EVERYTHING AFTER THE CHOSEN NUMBER?
# print(msg[2:])
    # YOU CAN SPECIFY AN ENDPOINT
# print(msg[2:9])
    # IF YOU TAKE OUT THE FIRST NUMBER(2), PYTHON ASSUMES YOU WANT TO START AT 0
# print(msg[:8])
    # EXAMPLE
# msg='welcome to Python 101: Strings'
# msg2='ring'
# msg3='Tyler' 
# msg4='1'
# # print(msg)
# print((msg4 + ' ' + msg[:7] + ' ' + msg2 + ' ' + msg[8:10] + ' ' + msg3).title())
    # OR
msg='welcome to Python 101: Strings'
msg1=msg[18]+' '+msg[:8]+msg[25:29]+msg[7:11]+msg[13]+msg[12]+msg[2]+msg[1]+msg[-5]  
print(msg1.title())
    # WANT TO PRINT BACKWARDS?
print(msg1[::-1].title())

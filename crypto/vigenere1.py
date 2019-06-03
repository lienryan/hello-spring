import string
from helpers import alphabet_position, rotate_character

def encrypt(message, key):

    encrypted_message = ''
               
    """for char in key"""
    
    for i in range(len(message)):
        for char in range(len(key)):
            if message[i].isalpha():
            
                encrypted_message += rotate_character(message[i], alphabet_position(key[i] +1))
                
            
  
        else:
            encrypted_message += message[i]

    return encrypted_message

def main():

    user_message = input("What message would you like to encrypt?")
    user_key = input("What text is your encryption key?")
    print(encrypt(user_message, user_key))

if __name__ =="__main__":
    main()
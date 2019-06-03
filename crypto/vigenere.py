import string
from helpers import alphabet_position, rotate_character

def encrypt(message, key):
    """recieves a string, message, and a word, key, 
    and returns the encrypted text by rotating each 
    character in message by each characters in key places to the right 
    """

    encrypted_message = ''
    
    key_pos = 0
    """for key_pos in key"""
   
    for i in range(len(message)):
        
        if message[i].isalpha():
            encrypted_message += rotate_character(message[i], alphabet_position(key[key_pos % len(key)]))
            key_pos += 1
        
        else:
            encrypted_message += message[i]

    return encrypted_message

def main():

    user_message = input("What message would you like to encrypt?")
    user_key = input("What text is your encryption key?")
    print(encrypt(user_message, user_key))

if __name__ =="__main__":
    main()
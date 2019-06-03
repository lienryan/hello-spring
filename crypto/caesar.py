import string
from helpers import alphabet_position, rotate_character

"""recieves a string, text, and an integer, rot, 
and returns the encrypted text by rotating each 
character in text by rot places to the right.
"""
    
def encrypt(text,rot):  
    
    encrypted_text = ""
    
    for char in text:
        encrypted_text += rotate_character (char, rot)
        
    return encrypted_text

def main():

    user_text = input("What text would you like to encrypt?")
    user_rot = int(input("What integer is your encryption key?"))
    print(encrypt(user_text, user_rot))

if __name__ =="__main__":
    main()
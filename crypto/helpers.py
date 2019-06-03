import string

uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase

def alphabet_position(letter):
    """
    receives a letter, returns 0-based 
    numerical position of that letter within the alphabet; 
    """
    
    if letter in uppercase:
        position = uppercase.index(letter)
        
    elif letter in lowercase:
        position = lowercase.index(letter)
        
    return position


def rotate_character(char,rot):
    """
    receives a string, char, and an integer, 
    rot, and returns a new string that is the result
    of rotating char by rot number of places to the right
    """
    
    if char in uppercase:
        new_char = uppercase[(alphabet_position(char)+rot)%26]
    elif char in lowercase:
        new_char = lowercase[(alphabet_position(char)+rot)%26]
    else:
        new_char = char 
    
    return new_char
def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase) """
    # TODO your code here
    name = fullname
    full_name = name.split()
 
    initials = ""

    for name in full_name:
        initials += name[0].upper()

    return initials
def main():
    fullname = input("What is your full name?")
    print(get_initials(fullname))
    
if __name__ == "__main__":
    main()
    
    





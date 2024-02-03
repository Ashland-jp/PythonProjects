def password_checker(password):
    # set rules for password strength
    min_length = 12
    has_uppercase = False
    has_lowercasee = False
    has_digit = False
    has_special_char = False
    special_chars = "!@#$%^&*()-_=+[{]}\|:;',<.>/?"

    # check length
    if len(password) < min_length:
        print("Password is too short!")
        return False

    # check if password meets remaining requirements
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special_char = True

    # Print error for any missing requirements
    if not has_uppercase:
        print("Password must contain at least one Uppercase letter!")
        return False
    if not has_lowercase:
        print("Password must contain at least one Lowercase letter!")
        return False
    if not has_digit:
        print("Password must contain at least one Number!")
        return False
    if not has_special_char:
        print("Password must contain at least one Special Character!")
        return False

    # if requirements are fulfilled, print success message
    print("Password is skrong!")
    return True


password = input("Enter a password with a minimum of 12 characters: ")
password_checker(password)
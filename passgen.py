import random
import string
def generate_password(length):
    """ This generates a random password using a combo of upper and lowercase letters, numbers, and special characters"""

    # define a string containing all possible characters
    all_chars = string.ascii_letters + string.digits + string.punctuation

    # generate a password using a random selection of characters
    password = "".join(random.choice(all_chars) for i in range(length))

    return password

# test functionality by generating password with length of 15
password = generate_password(15)
print(password)
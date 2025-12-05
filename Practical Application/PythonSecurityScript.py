print("------------------------------------")
print("         Username Verifier          ") # Just some fancifying text
print("------------------------------------")

# Username checker function
def usernameChecker(username: str):
    if len(username) > 10: # Checks to see if the username is GREATER THAN (>) 10 characters
        print("Your username is too long!")
        return False # Prints error and returns False (meaning invalid username!)
    if ">" in username or "<" in username: # Checks to see if there are any "<" or ">" characters within the username to prevent against SQL injection attacks
        print("Your username contains > or < which has been blocked to prevent injection attacks!")
        return False # Prints error and returns False (meaning invalid username!)
    if not username.isalnum(): # Checks to see if the username is all alphanumerics (A-Z a-z 0-9) (INBUILT Python function)
        print("Your username isn't just Alphanumerics!")
        return False # Prints error and returns False (meaning invalid username!)
    
    print("Your username is valid!") # None of the checks have failed so the username must be Valid!
    return True

# Unit Tests

# Checks to see if "<" and ">" are successfully blocked
usernameChecker("=\"1\"or1<2")

# Checks to see if spaces are blocked (Non Alphanumerics)
usernameChecker("Space e")

# Checks to see if other alphanumerics are blocked
usernameChecker("!!ProGame!")

# Checks to see if long usernames are blocked
usernameChecker("ThisUsernameisToooooLong")

# Checks to see if a valid username works!
usernameChecker("Valid123")
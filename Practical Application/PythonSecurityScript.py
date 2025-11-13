print("------------------------------------")
print("         Username Verifier          ")
print("------------------------------------")


def usernameChecker(username: str):
    if len(username) > 10:
        print("Your username is too long!")
        return False
    if ">" in username or "<" in username:
        print("Your username contains > or < which has been blocked to prevent injection attacks!")
        return False
    if not username.isalnum():
        print("Your username isn't just Alphanumerics!")
        return False
    print("Your username is valid!")
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
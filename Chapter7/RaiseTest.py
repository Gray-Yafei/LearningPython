try:
    password = input("Enter your password: ")
    if len(password) < 8:
        raise Exception("Password must be at least 8 characters long")
except Exception as e:
    print(e)

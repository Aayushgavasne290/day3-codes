correct_pass ="somepassword"
not_found = True

while not_found:
    entered_password = input("enter the password:")
    if entered_password == correct_pass:
        print("Access granted")
        not_found = False
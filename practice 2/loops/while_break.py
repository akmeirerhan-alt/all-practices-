password_attempts = 0

while True:  # Creates an infinite loop
    password_attempts += 1
    print(f"Attempt {password_attempts}")
    
    if password_attempts == 3:
        print("Too many attempts. System locked.")
        break  # Forces the 'while True' loop to stop
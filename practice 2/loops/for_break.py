# Stop the loop if we find the number 7
numbers = [1, 3, 5, 7, 9]

for num in numbers:
    if num == 7:
        print("Found 7! Stopping the loop.")
        break
    print(f"Checking: {num}")
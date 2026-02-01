# Skip the number 3, but keep printing others
for i in range(1, 6):
    if i == 3:
        print("Skipping 3...")
        continue
    print(f"Number: {i}")
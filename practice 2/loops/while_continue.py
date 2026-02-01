i = 0

while i < 5:
    i += 1
    if i == 2:
        print("Wait, skipping 2...")
        continue
    print(f"Processing number: {i}")
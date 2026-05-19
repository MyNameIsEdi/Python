# --- Exercise 1: Age Boundaries and Categorization ---
print("--- Age Check ---")
age = int(input("Please enter your age: "))

# Fix out-of-bounds ages (Clamping)
if age < 0:
    age = 0
elif age > 120:
    age = 120

# Categorize based on the fixed age
if 0 <= age <= 18:
    print("teenager")
elif 19 <= age <= 120:
    print("adult")


# --- Exercise 2: Password Validation ---
print("\n--- Password Validation ---")
password = input("Please enter a password: ")

# Check validation rules one by one to provide specific feedback
if len(password) < 8:
    print("Error: Password must be at least 8 characters long.")
elif password[0] != 'C' and password[0] != 'Z':
    print("Error: Password must start with 'C' or 'Z'.")
elif password[-1] != '$':
    print("Error: Password must end with '$'.")
else:
    # If it didn't fail any of the conditions above, it's valid!
    print("STRONG PASSWORD")
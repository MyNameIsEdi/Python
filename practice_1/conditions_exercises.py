# --- Exercise 1: Positive or Negative ---
print("--- Exercise 1 ---")
num_str = input("Please enter a number: ")

# Convert input to float to handle decimals, then check conditions
try:
    num = float(num_str)
    if num > 0:
        print("The number is positive.")
    elif num < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")
except ValueError:
    print("Invalid input. That's not a number.")


# --- Exercise 2: Change first 'A' to 'a' ---
print("\n--- Exercise 2 ---")
text = input("Please enter a string: ")

# Check if the string is not empty and starts with 'A'
if len(text) > 0 and text[0] == 'A':
    # Create a new string with 'a' and the rest of the original string
    modified_text = 'a' + text[1:]
    print(f"Modified string: {modified_text}")
else:
    print(f"String unchanged: {text}")


# --- Exercise 3: Basic Email Validation ---
print("\n--- Exercise 3 ---")
email = input("Please enter an email address: ")

# Check for length and invalid '@' positions
if len(email) < 4:
    print("ERROR")
elif email[0] == '@' or email[-1] == '@':
    print("ERROR")
else:
    print("Email format is valid.")
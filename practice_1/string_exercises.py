# --- Exercise 1 ---
print("--- Exercise 1 ---")
text = input("Please enter a string (e.g., an email address): ")

first_char = text[0]
last_char = text[-1]
# Using // for integer division to avoid float index error
middle_char = text[len(text) // 2] 

print(f"First character: {first_char}")
print(f"Middle character: {middle_char}")
print(f"Last character: {last_char}")


# --- Exercise 2 ---
print("\n--- Exercise 2 ---")
email_text = input("Please enter a string of at least 5 characters: ")

# a. Slice from the 3rd character to the end (index 2)
sliced_text = email_text[2:]
print(f"a. Sliced string (3rd char to end): {sliced_text}")

# b. Print the length of the string
text_length = len(email_text)
print(f"b. String length: {text_length}")

# c. Replace all spaces with a hyphen '-'
replaced_text = email_text.replace(" ", "-")
print(f"c. String without spaces: {replaced_text}")
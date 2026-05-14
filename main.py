# ==========================================
# סעיף 1 – יצירת משתנים
# ==========================================
print("--- Section 1: Variables ---")

user_name = "Dana"
age = 28
is_connected = True
test_score = 95.5

print("User:", user_name)
print("Age:", age)
print("Connected:", is_connected)
print("Score:", test_score)

# ==========================================
# סעיף 2 – שינוי ערכים
# ==========================================
print("\n--- Section 2: Updating Variables ---")

# שינוי של שני משתנים
age = 29
is_connected = False

print("Updated Age:", age)
print("Updated Connected status:", is_connected)

# ==========================================
# סעיף 3 – הכרת input באופן עצמאי
# ==========================================
print("\n--- Section 3: User Input ---")

input_name = input("Enter your name:\n")
input_age = input("Enter your age:\n")

print("\nHello", input_name)

# ==========================================
# סעיף 4 – אתגר (לא חובה)
# ==========================================
print("\n--- Section 4: Challenge ---")

tester_name = input("Enter tester name: ")
tests_run = input("Enter number of tests you ran today: ")

# שימוש ב-f-string כדי לשלב משתנים בתוך מחרוזת בקלות
print(f"Tester {tester_name} ran {tests_run} tests today")

# ==========================================
# סעיף 5 – בונוס לבודקי תוכנה
# ==========================================
print("\n--- Section 5: Bonus (If statement) ---")

test_passed = True

if test_passed == True:
    print("TEST PASSED")
else:
    print("TEST FAILED")
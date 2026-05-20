# --- Exercise: String Length Validation ---
print("--- String Length Validation ---")

# 1. קליטת המחרוזת מהמשתמש
user_text = input("Please enter a string: ")

# 2. שמירת אורך המחרוזת בתוך משתנה חדש
text_length = len(user_text)

# 3. בדיקת התנאים והדפסה בהתאם
if text_length < 4:
    print("too short")
elif text_length > 9:
    print("too long")
else:
    # If it's not less than 4 and not greater than 9, it must be between 4 and 9
    print("OK")

# הדפסת עזר רק כדי שיהיה נוח לראות את האורך (לא חובה לתרגיל)
print(f"(The actual length was: {text_length})")

```markdown
# 🐍 מבוא לפייתון לבודקי תוכנה (QA)

ברוכים הבאים למדריך הבסיסי לפייתון, המותאם במיוחד עבור בודקי תוכנה (QA) שעושים את צעדיהם הראשונים בעולם פיתוח האוטומציה! 🚀

מאגר זה נועד לרכז את כל מושגי היסוד שצריך להכיר כדי להתחיל לכתוב סקריפטים ובדיקות אוטומטיות בשפת Python.

## 📚 תוכן עניינים
1. [משתנים וסוגי נתונים](#1-משתנים-וסוגי-נתונים)
2. [תנאים](#2-תנאים-ifelifelse)
3. [מבני נתונים: רשימות](#3-רשימות-lists)
4. [מבני נתונים: מילונים](#4-מילונים-dictionaries)
5. [לולאות](#5-לולאות-loops)
6. [פונקציות](#6-פונקציות-functions)
7. [טיפים של זהב](#7-טיפים-של-זהב-לבודק-המתחיל)

---

## 1. משתנים וסוגי נתונים
בבדיקות תוכנה, אנחנו כל הזמן שומרים נתונים: שמות משתמשים, סיסמאות, סטטוסים וכו'. משתנה הוא פשוט "קופסה" ששומרת ערך בזיכרון.

סוגי הנתונים המרכזיים:
* **String (מחרוזת):** לטקסטים וכתובות (מוקף בגרשיים).
* **Integer (מספר שלם):** לסטטוס קוד (למשל 200), כמויות.
* **Float (מספר עשרוני):** למחירים, זמני תגובה.
* **Boolean (בוליאני):** `True` או `False`. מעולה לסטטוס של טסט.

```python
env_url = "[https://qa.myapp.com](https://qa.myapp.com)"  # String
expected_status_code = 200        # Integer
response_time = 1.45              # Float
is_test_passed = True             # Boolean

```

---

## 2. תנאים (if/elif/else)

הלב של כל בדיקת אוטומציה הוא ה־**Assertion** (אימות) – אנחנו בודקים האם ה"תוצאה בפועל" (Actual) שווה ל"תוצאה המצופה" (Expected).

```python
expected_title = "Welcome"
actual_title = "Welcome"

if actual_title == expected_title:
    print("Test Passed! The titles match.")
else:
    print(f"Test Failed! Expected '{expected_title}' but got '{actual_title}'.")

```

---

## 3. רשימות (Lists)

לשמירת קבוצה של נתונים, כמו רשימת דפדפנים להרצת הבדיקה. מוגדר בעזרת `[]`.

```python
supported_browsers = ["Chrome", "Firefox", "Edge", "Safari"]

# הדפסת הדפדפן הראשון ברשימה (הספירה מתחילה מ-0)
print(supported_browsers[0])  # Output: Chrome

# הוספת דפדפן חדש לרשימה
supported_browsers.append("Opera")

```

---

## 4. מילונים (Dictionaries)

קריטיים לבדיקות API. מבנה נתונים שמזכיר JSON, בנוי מזוגות של **מפתח וערך** (Key: Value) בתוך `{}`.

```python
user_payload = {
    "id": 101,
    "username": "qa_tester_1",
    "is_admin": False
}

# גישה לנתון בתוך המילון
print(user_payload["username"])  # Output: qa_tester_1

```

---

## 5. לולאות (Loops)

מונעות חזרתיות (DRY). אם רוצים להריץ טסט על מספר דפדפנים, נשתמש בלולאת `for`.

```python
browsers = ["Chrome", "Firefox", "Edge"]

for browser in browsers:
    print(f"Starting test execution on {browser}...")
    
print("All tests completed.")

```

---

## 6. פונקציות (Functions)

אורזות קטעי קוד לשימוש חוזר כדי לשמור על סדר וקריאות. מוגדרות בעזרת המילה `def`.

```python
def login(username, password):
    print(f"Entering username: {username}")
    print(f"Entering password: {password}")
    print("Clicking the login button")
    return True

# שימוש בפונקציה פעמיים עבור משתמשים שונים
login("admin", "123456")
login("guest", "password123")

```

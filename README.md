
# 🐍 Python for QA Automation: המדריך המלא לבודקי תוכנה

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue?style=for-the-badge&logo=python)
![QA Focus](https://img.shields.io/badge/Focus-QA_%26_Automation-green?style=for-the-badge)
![Learning](https://img.shields.io/badge/Level-Beginner-orange?style=for-the-badge)

ברוכים הבאים למדריך הבסיסי לפייתון, המותאם במיוחד עבור אנשי QA שעושים את צעדיהם הראשונים בעולם פיתוח האוטומציה! 🚀

מאגר זה מרכז את כל מושגי היסוד הנדרשים לכתיבת סקריפטים, בדיקות API, ובדיקות UI אוטומטיות.

---

## 📚 תוכן עניינים
* [📦 משתנים וסוגי נתונים](#1-משתנים-וסוגי-נתונים)
* [⚖️ תנאים ואימותים (Assertions)](#2-תנאים-ואימותים-ifelifelse)
* [📂 מבני נתונים (Lists & Dictionaries)](#3-מבני-נתונים-רשימות-ומילונים)
* [🔄 לולאות (Loops)](#4-לולאות-loops)
* [⚙️ פונקציות ושימוש חוזר](#5-פונקציות-functions)
* [🏆 סיכום: תרחיש בדיקה אמיתי](#-תרחיש-בדיקה-מסכם)
* [💡 טיפים של זהב](#-טיפים-של-זהב-לבודק-המתחיל)

---

## 1. משתנים וסוגי נתונים
בבדיקות תוכנה, אנחנו שומרים נתונים כמו שמות משתמשים, סיסמאות וזמני תגובה. פייתון היא שפה "חכמה" שלא דורשת מאיתנו להגדיר את סוג המשתנה מראש.

| סוג נתון | שם באנגלית | שימוש נפוץ ב-QA | דוגמה |
| :--- | :--- | :--- | :--- |
| **מחרוזת** | String | שמות משתמשים, כתובות URL, הודעות שגיאה | `"https://api.test.com"` |
| **מספר שלם** | Integer | סטטוס קוד (200, 404), כמות פריטים בעגלה | `200` |
| **מספר עשרוני** | Float | זמני תגובה של שרת, מחירי מוצרים | `1.45` |
| **בוליאני** | Boolean | בדיקה האם אלמנט מוצג, האם טסט עבר | `True` / `False` |

```python
endpoint = "/auth/login"      # String
expected_code = 200           # Integer
latency_threshold = 0.5       # Float
is_element_visible = True     # Boolean

```

---

## 2. תנאים ואימותים (if/elif/else)

הלב של האוטומציה הוא ה-**Assertion**. אנחנו משתמשים בתנאים כדי להשוות בין התוצאה בפועל (Actual) לתוצאה המצופה (Expected).

```python
actual_status = 404
expected_status = 200

if actual_status == expected_status:
    print("✅ Test Passed: Status code is 200")
elif actual_status == 500:
    print("❌ Test Failed: Server Error (500)")
else:
    print(f"❌ Test Failed: Got status {actual_status}")

```

---

## 3. מבני נתונים: רשימות ומילונים

### 🔹 רשימות (Lists) - לניהול אוספים

מתאים לשמירת רשימת דפדפנים, רשימת יוזרים או מערך של מוצרים.

```python
browsers = ["Chrome", "Firefox", "Edge"]
browsers.append("Safari") # הוספת איבר
print(browsers[0])        # גישה לאיבר הראשון (Chrome)

```

### 🔹 מילונים (Dictionaries) - עבודה עם API

המילון הוא הבסיס לעבודה עם JSON. הוא בנוי מזוגות של **מפתח:ערך**.

```python
# ייצוג של Response מ-API
user_data = {
    "id": 55,
    "role": "admin",
    "email": "test@qa.com"
}
print(user_data["role"])  # פלט: admin

```

---

## 4. לולאות (Loops)

לולאות מאפשרות לנו להריץ את אותה בדיקה על נתונים שונים (Data Driven Testing).

```python
test_users = ["admin_user", "guest_user", "editor_user"]

for user in test_users:
    print(f"Running Login Test for: {user}")

```

---

## 5. פונקציות (Functions)

כדי לא לחזור על קוד (עקרון ה-DRY), נכניס פעולות נפוצות (כמו התחברות או ניקוי נתונים) לתוך פונקציות.

```python
def check_response_time(actual_time, limit=2.0):
    if actual_time <= limit:
        return True
    return False

# שימוש בפונקציה
result = check_response_time(1.2)
print(f"Is performance OK? {result}")

```

---

## 🏗 תרחיש בדיקה מסכם

כך נראה קוד שמשלב את כל המושגים שלמדנו לתוך "טסט" קטן:

```python
def run_api_test(endpoint, expected_status):
    response = {"status": 200, "data": "Success"} # דמיון של תגובת שרת
    
    print(f"Testing endpoint: {endpoint}")
    
    if response["status"] == expected_status:
        return "PASS"
    else:
        return "FAIL"

# הרצה על רשימת אנדפוינטים
endpoints = ["/login", "/profile", "/logout"]
for ep in endpoints:
    status = run_api_test(ep, 200)
    print(f"Result for {ep}: {status}")

```

---

## 💡 טיפים של זהב לבודק המתחיל

1. **הזחות (Indentation):** פייתון רגישה לרווחים! ודאו שכל בלוק קוד נמצא תחת אותה הזחה (Tab/4 Spaces).
2. **Clean Code:** תנו שמות משמעותיים. `is_login_successful` עדיף בהרבה על `x`.
3. **אל תפחדו משגיאות:** ה-**Traceback** (הטקסט האדום) הוא החבר הכי טוב שלכם. השורה האחרונה בדרך כלל מסבירה בדיוק מה נשבר.
4. **תיעוד:** השתמשו ב-Comments (`#`) כדי להסביר למה כתבתם שלב מסוים בטסט.

---

בעריכת אדי מ | למידה מהנה! 🐍✨

```

# 🔐 Password Strength Checker

A professional CLI-based Python application that evaluates the strength of a password using multiple validation rules.

---

## Project Overview

The **Password Strength Checker** analyzes a user-entered password and classifies it as:

- ❌ Weak  
- ⚠️ Medium  
- ✅ Strong  

It evaluates password strength based on length and character diversity (uppercase, lowercase, digits, and special characters).

This project demonstrates:
- Clean modular programming
- Input validation
- Use of built-in Python modules
- CLI user interaction design
- Basic security logic implementation

---

## Features

✔ Checks minimum length (≥ 8 characters)  
✔ Detects uppercase letters  
✔ Detects lowercase letters  
✔ Detects numeric digits  
✔ Detects special characters  
✔ Strength scoring system (0–5 scale)  
✔ Colored terminal output  
✔ Retry loop with input validation  
✔ Professional program structure using `if __name__ == "__main__"`  

---

##  Technologies Used

- Python 3
- `string` module (built-in)
- `colorama` library (for colored CLI output)

---

## 📂 Project Structure

```
password-strength-checker/
│
├── art.py
├── main.py
└── README.md
```

---

## ▶️ How to Run

```bash
python main.py
```

---

## 🧠 How the Strength Scoring Works

The password receives 1 point for each condition met:

| Condition | Points |
|-----------|--------|
| Length ≥ 8 | +1 |
| Contains Uppercase | +1 |
| Contains Lowercase | +1 |
| Contains Digit | +1 |
| Contains Special Character | +1 |

### Strength Classification

- 0–2 → Weak  
- 3–4 → Medium  
- 5 → Strong  

---

## 📷 Example Output

```
Enter your password: Hello@123
✅ Strong Password

Do you want to try again? (y/n): n
Thank you for using Password Strength Checker 🚀
```

---

## 🎯 Learning Outcomes

This project helped reinforce:

- String manipulation in Python
- Generator expressions with `any()`
- Writing reusable functions
- CLI application flow control
- Basic password validation logic

---

## 🔮 Future Improvements

- Hide password input using `getpass`
- Add password improvement suggestions
- Display strength score (e.g., 4/5)
- Convert to GUI using Tkinter
- Implement advanced entropy-based scoring

---

## Author

**Sanaa**  
Python Learner | Data Enthusiast | Building in Public 

---

⭐ If you found this project useful, consider giving it a star!
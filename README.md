# 🔐 Password Strength Analyzer

A simple Python-based **Password Strength Analyzer** that checks how strong a password is based on its length and complexity.

This project is designed for beginners to understand **password security, Python programming, regular expressions, and basic cybersecurity concepts**.

## 📌 Features

* ✅ Checks password length
* ✅ Checks for uppercase letters
* ✅ Checks for lowercase letters
* ✅ Checks for numbers
* ✅ Checks for special characters
* ✅ Calculates a password strength score
* ✅ Classifies passwords as:

  * 🔴 Weak
  * 🟡 Medium
  * 🟢 Strong
* ✅ Provides suggestions to improve weak passwords

## 🛠️ Technologies Used

* **Python 3**
* **Regular Expressions (`re`)**
* **VS Code**

No external Python libraries are required.

## 📂 Project Structure

```text
Password-Strength-Analyzer/
│
├── code.py
└── README.md
```

## ⚙️ How It Works

The program asks the user to enter a password and checks five important conditions:

| Check             | Requirement                    |
| ----------------- | ------------------------------ |
| Length            | At least 8 characters          |
| Uppercase         | At least one A-Z               |
| Lowercase         | At least one a-z               |
| Number            | At least one 0-9               |
| Special Character | At least one special character |

The program gives **1 point** for every condition satisfied.

### Strength Levels

```text
5 points  → STRONG
3-4 points → MEDIUM
0-2 points → WEAK
```

## ▶️ How to Run

### 1. Install Python

Make sure Python is installed on your computer.

Check it using:

```bash
python --version
```

### 2. Clone the Repository

```bash
git clone https://github.com/yourusername/password-strength-analyzer.git
```

### 3. Open the Project

```bash
cd password-strength-analyzer
```

### 4. Run the Program

```bash
python code.py
```

## 💻 Example

```text
================================
     PASSWORD STRENGTH CHECKER
================================

Enter your password: Password9@

------------------------------
⚠️ Password Strength: MEDIUM
------------------------------
```

## 🎯 Learning Objectives

Through this project, I learned:

* Basic Python programming
* Conditional statements
* User input handling
* Regular expressions
* Password security concepts
* Password complexity analysis
* Basic cybersecurity principles

## 🔮 Future Improvements

The project can be improved by adding:

* 🔹 Password generator
* 🔹 Common-password detection
* 🔹 Detection of repeated characters and patterns
* 🔹 GUI using Tkinter
* 🔹 Password history using SQLite
* 🔹 Secure password hashing
* 🔹 Entropy-based password strength calculation

## ⚠️ Security Note

This project is intended for **educational purposes**.

The analyzer should not be used as a replacement for professional password-security systems. Real applications should use secure password hashing algorithms such as **Argon2id** or **bcrypt** and should never store passwords in plain text.

## 👩‍💻 Author

**Pallavi Poojari**

Cybersecurity Student | Networking & Cybersecurity Enthusiast

---

⭐ If you found this project useful, consider giving the repository a star!

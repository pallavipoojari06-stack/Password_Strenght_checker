import re

print("================================")
print("     PASSWORD STRENGTH CHECKER")
print("================================")

password = input("Enter your password: ")

score = 0

# Check length
if len(password) >= 8:
    score += 1
else:
    print("❌ Password should have at least 8 characters.")

# Check uppercase
if re.search("[A-Z]", password):
    score += 1
else:
    print("❌ Add at least one uppercase letter (A-Z).")

# Check lowercase
if re.search("[a-z]", password):
    score += 1
else:
    print("❌ Add at least one lowercase letter (a-z).")

# Check number
if re.search("[0-9]", password):
    score += 1
else:
    print("❌ Add at least one number (0-9).")

# Check special character
if re.search("[!@#$%^&*]", password):
    score += 1
else:
    print("❌ Add a special character (! @ # $ % ^ & *).")

# Show result
print("\n------------------------------")

if score == 5:
    print("✅ Password Strength: STRONG")
elif score >= 3:
    print("⚠️ Password Strength: MEDIUM")
else:
    print("❌ Password Strength: WEAK")

print("------------------------------")
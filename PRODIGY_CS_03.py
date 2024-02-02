import re

def is_password_complex(password):
    # Minimum length check
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."

    # Uppercase and lowercase letter check
    if not any(c.isupper() for c in password) or not any(c.islower() for c in password):
        return False, "Password must contain both uppercase and lowercase letters."

    # Digit check
    if not any(c.isdigit() for c in password):
        return False, "Password must contain at least one digit."

    # Special character check (optional, you can customize this pattern)
    special_char_pattern = re.compile(r'[!@#$%^&*(),.?":{}|<>]')
    if not special_char_pattern.search(password):
        return False, "Password must contain at least one special character."

    # If all checks pass, the password is considered complex
    return True, "Password is complex and meets the criteria."

# Example usage
password_to_check = input("Enter a password: ")

is_complex, feedback = is_password_complex(password_to_check)

if is_complex:
    print("Password is complex and meets the criteria.")
else:
    print(f"Password is not complex. {feedback} Please follow the password criteria.")

import re


common_passwords = ["123456", "password", "123456789", "12345678", "12345", "1234567", "password1", "1234567890"]

def check_password_strength(password):
    # Initialize variables to keep track of different criteria
    length_criteria = len(password) >= 8
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    digit_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    common_password_criteria = password not in common_passwords

    # Assess the strength of the password based on the criteria
    criteria_met = sum([length_criteria, lowercase_criteria, uppercase_criteria, digit_criteria, special_char_criteria, common_password_criteria])

    # Provide feedback based on the number of criteria met
    if criteria_met == 6:
        strength = 'Very Strong'
    elif criteria_met == 5:
        strength = 'Strong'
    elif criteria_met == 4:
        strength = 'Moderate'
    elif criteria_met == 3:
        strength = 'Weak'
    else:
        strength = 'Very Weak'

    return strength, {
        'Length': length_criteria,
        'Lowercase': lowercase_criteria,
        'Uppercase': uppercase_criteria,
        'Digit': digit_criteria,
        'Special Character': special_char_criteria,
        'Not a Common Password': common_password_criteria
    }

def provide_suggestions(criteria):
    suggestions = []
    if not criteria['Length']:
        suggestions.append("Make your password at least 8 characters long.")
    if not criteria['Lowercase']:
        suggestions.append("Include at least one lowercase letter.")
    if not criteria['Uppercase']:
        suggestions.append("Include at least one uppercase letter.")
    if not criteria['Digit']:
        suggestions.append("Include at least one digit.")
    if not criteria['Special Character']:
        suggestions.append("Include at least one special character (e.g., !, @, #, $).")
    if not criteria['Not a Common Password']:
        suggestions.append("Avoid using common passwords.")
    return suggestions

def main():
    while True:
        password = input("\nEnter a password to check its strength: ")
        
        strength, criteria = check_password_strength(password)
        
        print(f"\nPassword Strength: {strength}")
        print("Criteria Met:")
        for criterion, met in criteria.items():
            print(f" - {criterion}: {'Yes' if met else 'No'}")

        suggestions = provide_suggestions(criteria)
        if suggestions:
            print("\nSuggestions to improve your password strength:")
            for suggestion in suggestions:
                print(f" - {suggestion}")

        continue_check = input("\nDo you want to check another password? (yes/no): ").strip().lower()
        if continue_check != 'yes':
            print("Thanks for using! Use a strong password and stay safe.\n")
            break

if __name__ == "__main__":
    main()

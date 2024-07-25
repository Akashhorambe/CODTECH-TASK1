import re

def check_password_strength(password):
    # Initialize variables to keep track of different criteria
    length_criteria = len(password) >= 8
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    digit_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Assess the strength of the password based on the criteria
    criteria_met = sum([length_criteria, lowercase_criteria, uppercase_criteria, digit_criteria, special_char_criteria])

    # Provide feedback based on the number of criteria met
    if criteria_met == 5:
        strength = 'Very Strong'
    elif criteria_met == 4:
        strength = 'Strong'
    elif criteria_met == 3:
        strength = 'Moderate'
    elif criteria_met == 2:
        strength = 'Weak'
    else:
        strength = 'Very Weak'

    return strength, {
        'Length': length_criteria,
        'Lowercase': lowercase_criteria,
        'Uppercase': uppercase_criteria,
        'Digit': digit_criteria,
        'Special Character': special_char_criteria
    }

def main():
    while True:
     
        password = input("\n Enter a password to check its strength: ")
        
        strength, criteria = check_password_strength(password)
        
        
        print(f"\nPassword Strength: {strength}")
        print("Criteria Met:")
        for criterion, met in criteria.items():
            print(f" - {criterion}: {'Yes' if met else 'No'}")

        
        continue_check = input("\nDo you want to check another password? (yes/no): ").strip().lower()
        if continue_check != 'yes':
            break  
        else:
            print("Thanks for using ! Use Strong Password And Be Safe \n")

if __name__ == "__main__":
    main()

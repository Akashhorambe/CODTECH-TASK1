Name: Akash Anil Horambe

Company: CODTECH IT SOLUTIONS

ID : CT08DS5369

Domain: Cyber Security & Ethical Hacking

Duration: July to August 2024

Mentor: Muzammil Ahmed



# Password Strength Checker

## Overview

Password Strength Checker is a Python script that evaluates the strength of a password based on various criteria such as length, presence of lowercase and uppercase letters, digits, special characters, and avoidance of common passwords. This tool provides feedback on the strength of the password, which criteria are met, and suggestions to improve the password strength.

## Features

- Checks if the password meets the following criteria:
  - Length of at least 8 characters
  - Contains at least one lowercase letter
  - Contains at least one uppercase letter
  - Contains at least one digit
  - Contains at least one special character (e.g., `!@#$%^&*(),.?":{}|<>`)
  - Is not a common password (e.g., `123456`, `password`)
- Provides feedback on the strength of the password:
  - Very Weak
  - Weak
  - Moderate
  - Strong
  - Very Strong
- Provides suggestions to improve password strength.
- Continues to prompt the user for password input until they choose to stop.

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/Akashhorambe/CODTECH-Task1.git
   ```

2. **Navigate to the project directory**:
   ```sh
   cd CODTECH-TASK1
   ```

3. **Install necessary dependencies**:
   This script only requires the `re` module, which is included in the Python Standard Library. Therefore, no additional installations are necessary.

## Usage

1. **Run the script**:
   ```sh
   python password_checker.py
   ```

2. **Follow the prompts** to enter a password and receive feedback on its strength along with suggestions to improve it.

## Example

```sh
$ python password_checker.py

Enter a password to check its strength: P@ssw0rd

Password Strength: Strong
Criteria Met:
 - Length: Yes
 - Lowercase: Yes
 - Uppercase: Yes
 - Digit: Yes
 - Special Character: Yes
 - Not a Common Password: No

Suggestions to improve your password strength:
 - Avoid using common passwords.

Do you want to check another password? (yes/no): no
Thanks for using! Use a strong password and stay safe.
```



## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


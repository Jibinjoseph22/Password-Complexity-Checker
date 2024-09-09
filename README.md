
# Password Complexity Checker


![Screenshot 2024-09-09 173748](https://github.com/user-attachments/assets/820ea991-4dd5-4e85-962b-337e334f6811)

## Overview

**Password Complexity Checker** is a Python-based GUI tool designed to evaluate the strength of a password based on common security criteria such as length, presence of uppercase and lowercase letters, numbers, and special characters. The tool provides real-time feedback to users and features a dynamic color-changing bar that indicates the strength of the password.

## Features

- **Dynamic Feedback**: Provides immediate feedback on the strength of the password (Weak, Moderate, Strong).
- **Color-Coded Strength Bar**:
  - **Green**: Strong password.
  - **Yellow/Orange**: Moderate password.
  - **Red**: Weak password.
- **Real-Time Suggestions**: Lists improvements to make your password stronger (e.g., adding numbers or special characters).
- **Password Visibility Toggle**: Option to show or hide the password as you type.

## Password Strength Criteria

- **Length**: Minimum of 8 characters.
- **Uppercase Letters**: At least one uppercase letter (A-Z).
- **Lowercase Letters**: At least one lowercase letter (a-z).
- **Numbers**: At least one digit (0-9).
- **Special Characters**: At least one special character (e.g., !, @, #, $, etc.).

## Screenshots

### Weak Password Example:

![Screenshot 2024-09-09 173804](https://github.com/user-attachments/assets/51051863-ce98-44d1-9788-ca59411a8055)

### Moderate Password Example:

![Screenshot 2024-09-09 173822](https://github.com/user-attachments/assets/64bd1410-26c3-4dc3-9162-8b9fccda4cd2)

### Strong Password Example:

![Screenshot 2024-09-09 173850](https://github.com/user-attachments/assets/69772f0c-a071-4ff6-81dc-b7b04c382d5d)

## Requirements

- **Python 3.x**
- **Tkinter**: Python's standard GUI library, which is included with most Python installations.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/Jibinjoseph22/password-complexity-checker.git
   cd password-complexity-checker
   ```

2. (Optional) Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Run the `password_checker_gui.py` file:

   ```bash
   python password_checker_gui.py
   ```

## Usage

- Launch the application, and enter a password in the input field.
- The tool will provide immediate feedback on the strength of the password.
- The strength bar will dynamically change color:
  - **Red** for weak passwords.
  - **Orange** for moderate passwords.
  - **Green** for strong passwords.
- Suggestions to improve password strength will appear below the bar.

## Contributions

Contributions are welcome! Feel free to fork the project and submit a pull request, or open an issue for feature requests and bug reports.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.



# Student Entry Form Application

## Overview
This is a simple student entry form application built with Python and Tkinter. It allows users to input and save student information in a structured format.

## Features
- User-friendly graphical interface
- Input validation for all fields
- Data saved to CSV file for easy access and management
- Clear form functionality
- Current date auto-filled for entry date

## Required Fields
- Student ID (alphanumeric characters only)
- First Name
- Last Name
- Gender (dropdown selection)
- Program (dropdown selection)

## Optional Fields
- Date of Birth (MM/DD/YYYY format)
- Email (validated format)
- Phone Number
- Address
- City
- State
- Zip Code

## How to Run
1. Ensure you have Python installed on your system
2. Make sure Tkinter is installed (included with standard Python installation)
3. Run the application using the command:
   ```
   python student_entry_form.py
   ```

## Data Storage
All student information is saved to a CSV file named `students.csv` in the same directory as the application. The file is created automatically if it doesn't exist.

## Form Validation
The application performs the following validations:
- Required fields must be filled
- Student ID must contain only letters and numbers
- Email must be in a valid format (if provided)
- Phone number must be in a valid format (if provided)
- Dates must be in MM/DD/YYYY format
- Gender and Program selections must be made

## System Requirements
- Python 3.x
- Tkinter (included with standard Python installation)
- Windows, macOS, or Linux operating system
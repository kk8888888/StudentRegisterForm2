import tkinter as tk
from tkinter import ttk, messagebox
import re
import csv
import os
from datetime import datetime

class StudentEntryForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Entry Form")
        self.root.geometry("700x600")
        self.root.resizable(False, False)
        
        # Set the font
        self.font_style = ("Arial", 11)
        
        # Variables for form fields
        self.student_id = tk.StringVar()
        self.first_name = tk.StringVar()
        self.last_name = tk.StringVar()
        self.dob = tk.StringVar()
        self.gender = tk.StringVar()
        self.email = tk.StringVar()
        self.phone = tk.StringVar()
        self.address = tk.StringVar()
        self.city = tk.StringVar()
        self.state = tk.StringVar()
        self.zip_code = tk.StringVar()
        self.program = tk.StringVar()
        self.entry_date = tk.StringVar()
        
        # Set default values
        self.gender.set("Select Gender")
        self.program.set("Select Program")
        
        # Create the form
        self.create_form()
        
    def create_form(self):
        # Main frame
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = tk.Label(main_frame, text="Student Entry Form", font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=4, pady=10, sticky="w")
        
        # Form frame
        form_frame = tk.LabelFrame(main_frame, text="Student Information", font=self.font_style, padx=20, pady=20)
        form_frame.grid(row=1, column=0, columnspan=4, sticky="we", pady=10)
        
        # Student ID
        tk.Label(form_frame, text="Student ID:", font=self.font_style).grid(row=0, column=0, sticky="w", pady=5)
        tk.Entry(form_frame, textvariable=self.student_id, font=self.font_style, width=20).grid(row=0, column=1, sticky="w", pady=5)
        
        # First Name
        tk.Label(form_frame, text="First Name:", font=self.font_style).grid(row=1, column=0, sticky="w", pady=5)
        tk.Entry(form_frame, textvariable=self.first_name, font=self.font_style, width=20).grid(row=1, column=1, sticky="w", pady=5)
        
        # Last Name
        tk.Label(form_frame, text="Last Name:", font=self.font_style).grid(row=2, column=0, sticky="w", pady=5)
        tk.Entry(form_frame, textvariable=self.last_name, font=self.font_style, width=20).grid(row=2, column=1, sticky="w", pady=5)
        
        # Date of Birth
        tk.Label(form_frame, text="Date of Birth (MM/DD/YYYY):", font=self.font_style).grid(row=3, column=0, sticky="w", pady=5)
        tk.Entry(form_frame, textvariable=self.dob, font=self.font_style, width=20).grid(row=3, column=1, sticky="w", pady=5)
        
        # Gender
        tk.Label(form_frame, text="Gender:", font=self.font_style).grid(row=4, column=0, sticky="w", pady=5)
        gender_options = ["Select Gender", "Male", "Female", "Other", "Prefer not to say"]
        gender_menu = ttk.Combobox(form_frame, textvariable=self.gender, values=gender_options, font=self.font_style, width=18, state="readonly")
        gender_menu.grid(row=4, column=1, sticky="w", pady=5)
        
        # Email
        tk.Label(form_frame, text="Email:", font=self.font_style).grid(row=0, column=2, sticky="w", pady=5, padx=(20, 0))
        tk.Entry(form_frame, textvariable=self.email, font=self.font_style, width=25).grid(row=0, column=3, sticky="w", pady=5)
        
        # Phone
        tk.Label(form_frame, text="Phone:", font=self.font_style).grid(row=1, column=2, sticky="w", pady=5, padx=(20, 0))
        tk.Entry(form_frame, textvariable=self.phone, font=self.font_style, width=25).grid(row=1, column=3, sticky="w", pady=5)
        
        # Address
        tk.Label(form_frame, text="Address:", font=self.font_style).grid(row=2, column=2, sticky="w", pady=5, padx=(20, 0))
        tk.Entry(form_frame, textvariable=self.address, font=self.font_style, width=25).grid(row=2, column=3, sticky="w", pady=5)
        
        # City
        tk.Label(form_frame, text="City:", font=self.font_style).grid(row=3, column=2, sticky="w", pady=5, padx=(20, 0))
        tk.Entry(form_frame, textvariable=self.city, font=self.font_style, width=25).grid(row=3, column=3, sticky="w", pady=5)
        
        # State
        tk.Label(form_frame, text="State:", font=self.font_style).grid(row=4, column=2, sticky="w", pady=5, padx=(20, 0))
        tk.Entry(form_frame, textvariable=self.state, font=self.font_style, width=25).grid(row=4, column=3, sticky="w", pady=5)
        
        # Zip Code
        tk.Label(form_frame, text="Zip Code:", font=self.font_style).grid(row=5, column=0, sticky="w", pady=5)
        tk.Entry(form_frame, textvariable=self.zip_code, font=self.font_style, width=20).grid(row=5, column=1, sticky="w", pady=5)
        
        # Program
        tk.Label(form_frame, text="Program:", font=self.font_style).grid(row=5, column=2, sticky="w", pady=5, padx=(20, 0))
        program_options = ["Select Program", "Computer Science", "Business Administration", "Engineering", "Medicine", "Arts", "Law"]
        program_menu = ttk.Combobox(form_frame, textvariable=self.program, values=program_options, font=self.font_style, width=23, state="readonly")
        program_menu.grid(row=5, column=3, sticky="w", pady=5)
        
        # Entry Date
        tk.Label(form_frame, text="Entry Date (MM/DD/YYYY):", font=self.font_style).grid(row=6, column=0, sticky="w", pady=5)
        entry_date_entry = tk.Entry(form_frame, textvariable=self.entry_date, font=self.font_style, width=20)
        entry_date_entry.grid(row=6, column=1, sticky="w", pady=5)
        
        # Set current date as default
        current_date = datetime.now().strftime("%m/%d/%Y")
        self.entry_date.set(current_date)
        
        # Buttons frame
        button_frame = tk.Frame(main_frame)
        button_frame.grid(row=2, column=0, columnspan=4, pady=20)
        
        # Submit button
        submit_button = tk.Button(button_frame, text="Submit", command=self.submit_form, font=self.font_style, width=10, bg="#4CAF50", fg="white")
        submit_button.grid(row=0, column=0, padx=10)
        
        # Clear button
        clear_button = tk.Button(button_frame, text="Clear", command=self.clear_form, font=self.font_style, width=10, bg="#f44336", fg="white")
        clear_button.grid(row=0, column=1, padx=10)
        
        # Exit button
        exit_button = tk.Button(button_frame, text="Exit", command=self.root.destroy, font=self.font_style, width=10, bg="#555555", fg="white")
        exit_button.grid(row=0, column=2, padx=10)
    
    def validate_form(self):
        # Check if required fields are filled
        if not self.student_id.get() or not self.first_name.get() or not self.last_name.get():
            messagebox.showerror("Error", "Student ID, First Name, and Last Name are required fields.")
            return False
        
        # Validate Student ID (alphanumeric)
        if not re.match(r'^[A-Za-z0-9]+$', self.student_id.get()):
            messagebox.showerror("Error", "Student ID should contain only letters and numbers.")
            return False
        
        # Validate Email format
        if self.email.get() and not re.match(r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$', self.email.get()):
            messagebox.showerror("Error", "Please enter a valid email address.")
            return False
        
        # Validate Phone format
        if self.phone.get() and not re.match(r'^[0-9\-\(\)\s\.\+]+$', self.phone.get()):
            messagebox.showerror("Error", "Please enter a valid phone number.")
            return False
        
        # Validate Date of Birth format
        if self.dob.get():
            try:
                datetime.strptime(self.dob.get(), "%m/%d/%Y")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid date of birth in MM/DD/YYYY format.")
                return False
        
        # Validate Entry Date format
        try:
            datetime.strptime(self.entry_date.get(), "%m/%d/%Y")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid entry date in MM/DD/YYYY format.")
            return False
        
        # Validate dropdown selections
        if self.gender.get() == "Select Gender":
            messagebox.showerror("Error", "Please select a gender.")
            return False
        
        if self.program.get() == "Select Program":
            messagebox.showerror("Error", "Please select a program.")
            return False
        
        return True
    
    def submit_form(self):
        if not self.validate_form():
            return
        
        # Prepare data for saving
        student_data = [
            self.student_id.get(),
            self.first_name.get(),
            self.last_name.get(),
            self.dob.get(),
            self.gender.get(),
            self.email.get(),
            self.phone.get(),
            self.address.get(),
            self.city.get(),
            self.state.get(),
            self.zip_code.get(),
            self.program.get(),
            self.entry_date.get()
        ]
        
        # Save to CSV file
        file_exists = os.path.isfile('students.csv')
        
        with open('students.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            
            # Write header if file doesn't exist
            if not file_exists:
                writer.writerow([
                    'Student ID', 'First Name', 'Last Name', 'Date of Birth',
                    'Gender', 'Email', 'Phone', 'Address', 'City', 'State',
                    'Zip Code', 'Program', 'Entry Date'
                ])
            
            writer.writerow(student_data)
        
        messagebox.showinfo("Success", f"Student {self.first_name.get()} {self.last_name.get()} has been registered successfully!")
        self.clear_form()
    
    def clear_form(self):
        self.student_id.set("")
        self.first_name.set("")
        self.last_name.set("")
        self.dob.set("")
        self.gender.set("Select Gender")
        self.email.set("")
        self.phone.set("")
        self.address.set("")
        self.city.set("")
        self.state.set("")
        self.zip_code.set("")
        self.program.set("Select Program")
        self.entry_date.set(datetime.now().strftime("%m/%d/%Y"))

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentEntryForm(root)
    root.mainloop()
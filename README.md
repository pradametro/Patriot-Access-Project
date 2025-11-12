# Patriot-Access 🧑‍💻 
Patriot Access is an interactive, text-based student portal simulation for George Mason University.
It allows newly enrolled students to sign up, log in, manage accounts, deposit "Mason Money", and register for classes, and it happens all from the terminal.

The program uses file storage to persist user data between sessions and features built-in input validation for secure and realistic interaction.

---

## **Features**
- **User Signup & Login**  
  - Automatically generates a **unique 8-digit Student ID**.  
  - Stores account info (name, contact, balance, classes) in a `students.txt` file.

- **Mason Money System**  
  - Add funds using simulated credit-card input.  
  - Validates **numeric, length, and security code** formats.  
  - Updates balance in storage.  

- **Class Management**  
  - Add or drop classes dynamically.  
  - Updates student records in the file.  

- **Profile Display**  
  - Shows full student info, balance, and enrolled classes.  

- **About Mason**  
  - Displays a historical and cultural overview of **George Mason University**.   
    
---

## Technologies Used  
- Python  
- File I/O (`open()`, read/write handling)  
- OS Module – file validation and management  
- Random Module – unique ID generation  
- Basic Input Validation & Error Handling

---

## Program Flow  
- User chooses to **Sign Up** or **Log In**.  
- New users input personal info → system creates `students.txt` entry.  
- Returning users log in using Student ID and password.  
- After login, access the **Main Menu**:
  - [M] About George Mason  
  - [A] Deposit Money  
  - [C] Manage Classes  
  - [P] Display Profile  
  - [E] Exit  

---

## How to Run  
- Save the file as `patriot_access.py`.  
- Make sure `students.txt` exists (will auto-create if not).  
- Run the program in terminal:  
  ```bash
  python patriot_access.py

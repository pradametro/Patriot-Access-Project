#Group 3 Darian Salahi, Virakboth Chau, Emmanuel Ghirmai, Mohamed Elhendawy IT109 project.
#Porject TITLE: Patriot Access

import random #for gnumber generator
import os # for file management




print('----------------------------------------')
print('\tWelcome to Patriot Access')
print('An interactive student interface that allows newly enrolled mason students setup/login to their Mason accounts.\n')




students_file = "students.txt"  # File to store all student data




# Utility Functions
def load_existing_ids():
    """Load all existing student IDs from students.txt."""
    if not os.path.exists(students_file):  # Check if file exists
        return set()  # If file doesn't exist, return an empty set
    with open(students_file, "r") as file:
        return {line.split(":")[0] for line in file if line.strip()}  # Extract numeric IDs




def gen_unique_id(existing_ids):
    """Generate a unique numeric ID based on existing ones."""
    while True:
        student_id = random.randint(10000000, 99999999)  # Generate 8-digit number
        if str(student_id) not in existing_ids:
            return student_id




def save_user_data(student_id, first_name, last_name, phone, email, password):
    """Save user data to students.txt, including initial balance and classes."""
    initial_balance = 0.0  # New students start with a balance of 0.0
    classes = ""  # No classes enrolled initially
    with open(students_file, "a") as file:
        file.write(f"{student_id}:{first_name},{last_name},{phone},{email},{password},{initial_balance},{classes}\n")
    print("Your information has been saved successfully!")




def load_user_credentials():
    """Load user credentials from students.txt."""
    if not os.path.exists(students_file):
        return {}
    user_credentials = {}
    with open(students_file, "r") as file:
        for line in file:
            student_id, details = line.strip().split(":")
            user_details = details.split(",")
            # Ensure classes field exists
            if len(user_details) < 7:
                user_details.append("")
            user_credentials[student_id] = user_details
    return user_credentials




# Functionalities
def signup_func():
    """Main signup function."""
    print('----------------------------------------')
    print('\t***** Welcome new patriot, we are glad to have you enroll to Mason! *****')
    print('\n\tPlease enter your information below to receive your student ID.')




    # Collect user details
    first_name = input('\n\tEnter your first name: ')
    last_name = input('\n\tEnter your last name: ')




    while True:
        phone = input('\n\tEnter your 10-digit phone number (e.g., 1234567890): ')
        if len(phone) == 10 and phone.isdigit():
            break
        print("\nInvalid phone number. Please enter exactly 10 digits.")




    email = input('\n\tEnter your email: ')
    password = input('\n\tCreate a password: ')




    # Load existing student IDs and generate a unique one
    existing_ids = load_existing_ids()
    student_id = gen_unique_id(existing_ids)
    print(f"\n\tYour Student ID is: {student_id}, make sure to keep track of this number as you will use it to log in.")




    # Save all user data to the file
    save_user_data(student_id, first_name, last_name, phone, email, password)




    # Return user details in the same format as `login`
    return [student_id, first_name, last_name, phone, email, password, 0.0, '']






def login():
    print('----------------------------------------')
    print("Welcome to the Mason Student Portal Login")
    user_credentials = load_user_credentials()
    attempt_count = 0
    while attempt_count < 3:
        student_id = input("Enter your student ID: ")
        password = input("Enter your password: ")
        if student_id in user_credentials and user_credentials[student_id][4].strip() == password:
            print("Login successful!\n")
            return [student_id] + user_credentials[student_id]  # Return full user details
        else:
            print("Invalid student ID or password. Please try again.\n")
            attempt_count += 1
    return None




def add_money(user_details):
    """Add money to the user's balance and update the file."""
    print('----------------------------------------')
    print('\tWelcome to MASON MONEY!')
    print('Mason money is money that students can use for campus-related activities such as dining halls, corner pocket, vending machines, and more.')

    try:
        # Get the current balance
        current_balance = float(user_details[6])


        # Ask if the user wants to add money
        add_choice = input(f"\nWould you like to add money to your account? Current Balance: ${current_balance:.2f} (y/n): ").strip().lower()


        if add_choice == 'y':
            # Prompt the user to enter an amount
            amount = input(f"\nYour current Balance is ${current_balance:.2f}. Enter the amount to add to your account (e.g., 50.00): $").strip()


            # Validate the input
            if not amount.replace('.', '', 1).isdigit():
                print("Invalid input. Please enter a numeric value.")
                return

            amount = float(amount)
            if amount <= 0:
                print("Amount must be greater than zero.")
                return

            # Prompt for a 16-digit credit card number
            credit_card = input("Enter your 16-digit credit card number: ").strip()
            if not credit_card.isdigit() or len(credit_card) != 16:
                print("Invalid credit card number. Please ensure it is exactly 16 digits.")
                return
                
            sec_code = input('Enter your 3-digit security code: ').strip()
            if not sec_code.isdigit() or len(sec_code)!=3:
                print("Invalid security code. Please ensure it is exactly 3 digits.")
                return
            
            # Update the balance
            new_balance = current_balance + amount
            user_details[6] = f"{new_balance:.2f}"  # Update in memory



            # Update the file
            with open(students_file, "r") as file:
                lines = file.readlines()



            with open(students_file, "w") as file:
                for line in lines:
                    student_id, details = line.strip().split(":")
                    if student_id == user_details[0]:  # Match the logged-in user
                        user_details_list = details.split(",")
                        user_details_list[5] = f"{new_balance:.2f}"  # Update the balance
                        file.write(f"{student_id}:{','.join(user_details_list)}\n")
                    else:
                        file.write(line)



            print(f"\n${amount:.2f} has been added to your account. Your new balance is ${new_balance:.2f}.")



        elif add_choice == 'n':
            # User chooses not to add money
            print("\nReturning to the main menu.")
            return
        else:
            # Invalid choice handling
            print("Invalid choice. Please enter 'y' or 'n'.")



    except ValueError:
        print("Error: Invalid balance format in user details.")
    except Exception as e:
        print(f"An error occurred while adding money: {e}")










def manage_classes(user_details):
    """Allow students to manage their enrolled classes."""
    student_id = user_details[0]
    
    print('----------------------------------------')
    print(f"Welcome {user_details[1]} {user_details[2]}, Manage Your Classes Here!")
    




    try:
        # Load student data from the file
        with open(students_file, "r") as file:
            lines = file.readlines()




        student_data = {}
        for line in lines:
            sid, details = line.strip().split(":")
            student_data[sid] = details.split(",")




        if student_id not in student_data:
            print("Error: Student ID not found.")
            return




        # Get current classes from the user's data
        current_classes = student_data[student_id][6:] if student_data[student_id][6:] else ['None']




        while True:
            print(f"\nYour current registered classes: {', '.join(current_classes) if current_classes else 'None'}")
            print("[A] Add a Class")
            print("[D] Drop a Class")
            print("[E] Exit Class Management")




            choice = input("Select an option (A/D/E): ").upper()
            if choice == "A":
                new_class = input("\nEnter the name of the class to add: ").strip()
                if new_class and new_class not in current_classes:
                    current_classes.append(new_class)
                    print(f"Class '{new_class}' added successfully!")
                else:
                    print("Class already enrolled or invalid input.")
            elif choice == "D":
                remove_class = input("\nEnter the name of the class to drop: ").strip()
                if remove_class in current_classes:
                    current_classes.remove(remove_class)
                    print(f"Class '{remove_class}' removed successfully!")
                else:
                    print("Class not found in your current list.")
            elif choice == "E":
                print("Exiting Class Management.")
                break
            else:
                print("Invalid choice. Please try again.")




        # Save updated class list
        student_data[student_id][6:] = current_classes
        with open(students_file, "w") as file:
            for sid, details in student_data.items():
                file.write(f"{sid}:{','.join(details)}\n")




        # Update user_details to reflect changes
        user_details[7:] = current_classes




    except FileNotFoundError:
        print("Error: Students file not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")




def about_mason():
    print("\n\t\t\tABOUT GEORGE MASON UNIVERSITY\n")


    print("\n\tGeorge Mason University is a proud and bustling epicenter of "
          "learning, knowledge, and creativity.\n"
          "It's no surprise, considering we've been successfully accomplishing our "
          "mission statement:\n"
          "'to change the world and create a better tomorrow,' for the past fifty-two years "
          "and counting.\n"
          "Even before becoming the #1 ranked public school in Virginia for innovation, "
          "George Mason has had a rich history\n"
          "of excellence in both academia and student life."
    )


    print("\n\tIt was in April of 1972 that George Mason University was brought into existence,\n"
          "marking the beginning of a new era of top-quality higher education for students "
          "around the country.\n"
          "1986 was a particularly exciting year for Mason when Professor James Buchanan won a "
          "Nobel Prize\n"
          "for his revolutionary work concerning public choice theory."
    )


    print("\n\tIn 1998, George Mason University was given the honor to host the first\n"
          "World Congress on Information Technology. This event hosted speeches from high officials\n"
          "all around the world, including Mikhail Gorbachev, Margaret Thatcher, and publisher "
          "Steven Forbes of Forbes magazine.\n"
          "With roots as strong and deep as this, it's no surprise that George Mason is constantly\n"
          "growing and improving to provide students with the best opportunities and resources.\n"
          "These efforts make it easier for George Mason students to continue changing the world\n"
          "for a better tomorrow."
    )
    input('\n\nPress any key to return to the main menu...')




def display_profile(user_details):
    """Display the current user's profile."""
    print('----------------------------------------')
    print("\n***** Student Profile *****")
    print(f"Student ID: {user_details[0]}")
    print(f"First Name: {user_details[1]}")
    print(f"Last Name: {user_details[2]}")
    print(f"Phone: {user_details[3]}")
    print(f"Email: {user_details[4]}")
    print(f"Current Balance: {user_details[6]}")
    print(f"Current Registered Classes: {', '.join(user_details[7:]) if user_details[7:] else 'None'}")
    print("***************************")




def main_menu(user_details):
    print('----------------------------------------')
    print(f"\n\tHi {user_details[1]}! Welcome to Patriot Access.\n")


    while True:
        choice = input("\n\t[M] About George Mason University"
                       '\n\t[A] Deposit Money'
                       '\n\t[C] Manage Classes'
                       '\n\t[P] Display Profile'
                       '\n\t[E] Exit'
                       "\n\nPlease select an option (M,A,C,P,E): ").upper()
        if choice == "A":
            add_money(user_details)  # Call the add_money function
        elif choice == "M":
            about_mason()
        elif choice == "C":
            manage_classes(user_details)
        elif choice == "P":
            display_profile(user_details)
        elif choice == "E":
            print("Thank you for using Patriot Access. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")




def initial_choice():
    while True:
        choice = input("Do you want to (L)ogin or (S)ignup for Patriot Access? (Enter: L/S): ").upper()
        if choice == "L":
            user_details = login()
            if user_details:
                main_menu(user_details)
                break
        elif choice == "S":
            user_details = signup_func()
            main_menu(user_details)
            break
        else:
            print("Invalid choice. Please enter 'L' for Login or 'S' for Signup.")




initial_choice()

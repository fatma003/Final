class Employee:
    """Class representing an employee."""

    def __init__(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details):
        """Initialize an Employee object with provided attributes."""
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.job_title = job_title
        self.basic_salary = basic_salary
        self.age = age
        self.date_of_birth = date_of_birth
        self.passport_details = passport_details

    def display_details(self):
        """Display details of the employee."""
        print("Employee ID:", self.employee_id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Job Title:", self.job_title)
        print("Basic Salary:", self.basic_salary)
        print("Age:", self.age)
        print("Date of Birth:", self.date_of_birth)
        print("Passport Details:", self.passport_details)


class Event:
    """Class representing an event."""

    def __init__(self, event_id, event_type, theme, date, time, duration, venue_address, client_id, caterer_id, cleaning_company_id, decorations_company_id, entertainment_company_id, furniture_supply_company_id, invoice):
        """Initialize an Event object with provided attributes."""
        self.event_id = event_id
        self.event_type = event_type
        self.theme = theme
        self.date = date
        self.time = time
        self.duration = duration
        self.venue_address = venue_address
        self.client_id = client_id
        self.caterer_id = caterer_id
        self.cleaning_company_id = cleaning_company_id
        self.decorations_company_id = decorations_company_id
        self.entertainment_company_id = entertainment_company_id
        self.furniture_supply_company_id = furniture_supply_company_id
        self.invoice = invoice

    def display_details(self):
        """Display details of the event."""
        print("Event ID:", self.event_id)
        print("Event Type:", self.event_type)
        print("Theme:", self.theme)
        print("Date:", self.date)
        print("Time:", self.time)
        print("Duration:", self.duration)
        print("Venue Address:", self.venue_address)
        print("Client ID:", self.client_id)
        print("Caterer ID:", self.caterer_id)
        print("Cleaning Company ID:", self.cleaning_company_id)
        print("Decorations Company ID:", self.decorations_company_id)
        print("Entertainment Company ID:", self.entertainment_company_id)
        print("Furniture Supply Company ID:", self.furniture_supply_company_id)
        print("Invoice:", self.invoice)


# Define other classes and their methods similarly

import tkinter as tk
from tkinter import ttk

class EventManagementSystemGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Event Management System")

        # Create notebook to organize classes
        self.notebook = ttk.Notebook(master)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Main classes to include in the GUI
        main_classes = ['Employee', 'Event', 'Client', 'Guest', 'Supplier']

        # Entry fields dictionary to store user inputs
        self.entry_fields = {class_name: {} for class_name in main_classes}

        # Create tabs for each main class
        self.tabs = {}
        for class_name in main_classes:
            self.tabs[class_name] = ttk.Frame(self.notebook)
            self.notebook.add(self.tabs[class_name], text=class_name)

            # Create entry fields for attributes
            for attribute in classes[class_name]:
                label = tk.Label(self.tabs[class_name], text=attribute)
                label.grid(row=classes[class_name].index(attribute), column=0, padx=5, pady=5, sticky=tk.W)

                entry = tk.Entry(self.tabs[class_name])
                entry.grid(row=classes[class_name].index(attribute), column=1, padx=5, pady=5, sticky=tk.EW)
                self.entry_fields[class_name][attribute] = entry

    def save_data(self):
        # Gather data from entry fields and print
        for class_name, attributes in self.entry_fields.items():
            print(class_name + ":")
            for attribute, entry in attributes.items():
                print(f"{attribute}: {entry.get()}")
            print()

# Define main classes and their attributes
classes = {
    'Employee': ['name', 'employee_id', 'department', 'job_title', 'basic_salary', 'age', 'date_of_birth', 'passport_details'],
    'Event': ['event_id', 'type', 'theme', 'date', 'time', 'duration', 'venue_address', 'client_id', 'caterer_id', 'cleaning_company_id', 'decorations_company_id', 'entertainment_company_id', 'furniture_supply_company_id', 'invoice'],
    'Client': ['client_id', 'name', 'address', 'contact_details', 'budget'],
    'Guest': ['guest_id', 'name', 'address', 'contact_details'],
    'Supplier': ['supplier_id', 'name', 'address', 'contact_details']
}

# Create the main Tkinter window
root = tk.Tk()
app = EventManagementSystemGUI(root)

# Add a button to save data
save_button = tk.Button(root, text="Save Data", command=app.save_data)
save_button.pack()

root.mainloop()



# Test cases
if __name__ == "__main__":
    # Create Employee objects
    emp1 = Employee("John Doe", "E001", "Sales", "Sales Manager", 50000, 30, "1994-05-15", "AB123456")
    emp2 = Employee("Jane Smith", "E002", "Marketing", "Marketing Manager", 55000, 28, "1996-08-20", "CD789012")

    # Display employee details
    print("Employee Details:")
    emp1.display_details()
    print()
    emp2.display_details()
    print()

    # Create Event objects
    event1 = Event("EV001", "Wedding", "Garden", "2024-05-15", "18:00", "4 hours", "123 Main St", "C001", "S001", "CC001", "DC001", "EC001", "FS001", "INV001")
    event2 = Event("EV002", "Birthday", "Superhero", "2024-06-20", "14:00", "3 hours", "456 Oak St", "C002", "S002", "CC002", "DC002", "EC002", "FS002", "INV002")

    # Display event details
    print("Event Details:")
    event1.display_details()
    print()
    event2.display_details()

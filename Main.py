import heapq


# Patient Class
class Patient:
    def __init__(self, name, surname, id_number):
        self.name = name
        self.surname = surname
        self.id_number = id_number

    def __str__(self):
        return f"Patient: {self.name} {self.surname}, ID: {self.id_number}"

    def print_info(self):
        print(self.__str__())


# Scheduler Class
class Scheduler:
    def __init__(self):
        # Priority queue for patients, where heapq is a min-heap by default
        self.schedule = []
        self.consultation_history = []  # List to store consultation records

    def add_patient(self, patient, priority):
        # We negate the priority to make heapq behave as a max-heap
        heapq.heappush(self.schedule, (-priority, patient))

    def get_next_patient(self):
        if self.schedule:
            return heapq.heappop(self.schedule)[1]  # Return the patient object
        else:
            return None

    def print_waiting_patients(self):
        if not self.schedule:
            print("No patients waiting.")
            return

        print("Patients currently waiting:")
        for priority, patient in sorted(self.schedule, reverse=True):
            print(f"Priority: {-priority}, {patient}")

    def save_consultation(self, patient, status):
        with open("consultations.txt", "a") as file:
            file.write(f"{patient}, Status: {status}\n")
        self.consultation_history.append((patient, status))
        print(f"Consultation saved for {patient} with status: {status}")

    def read_consultation_history(self):
        try:
            with open("consultations.txt", "r") as file:
                consultations = file.readlines()
                if consultations:
                    print("Consultation History:")
                    for consultation in consultations:
                        print(consultation.strip())
                else:
                    print("No consultation history available.")
        except FileNotFoundError:
            print("No consultation history found.")


# Main Menu Function
def main_menu():
    scheduler = Scheduler()

    while True:
        print("\n--- Emergency Room Scheduler ---")
        print("1. Add patient")
        print("2. Get next patient")
        print("3. Show waiting patients")
        print("4. Save consultation status")
        print("5. Read consultation history")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            name = input("Enter patient's first name: ")
            surname = input("Enter patient's last name: ")
            id_number = input("Enter patient's ID number: ")
            priority = int(input("Enter priority (1-5): "))
            patient = Patient(name, surname, id_number)
            scheduler.add_patient(patient, priority)
            print(f"Added {patient}")

        elif choice == '2':
            next_patient = scheduler.get_next_patient()
            if next_patient:
                print(f"Next patient: {next_patient}")
            else:
                print("No patients waiting.")

        elif choice == '3':
            scheduler.print_waiting_patients()

        elif choice == '4':
            name = input("Enter patient's first name: ")
            surname = input("Enter patient's last name: ")
            id_number = input("Enter patient's ID number: ")
            status = input("Enter consultation status (e.g., Follow-up required): ")
            patient = Patient(name, surname, id_number)
            scheduler.save_consultation(patient, status)

        elif choice == '5':
            scheduler.read_consultation_history()

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid option, please choose again.")


# Run the Main Menu
if __name__ == "__main__":
    main_menu()

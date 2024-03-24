import csv

# Function to check if file is empty
def is_file_empty(filename):
    with open(filename, 'r') as file:
        return not any(file)

filename = "write1.csv"

# Open file in append mode
with open(filename, "a", newline="") as f:
    a = csv.writer(f)
    
    # Check if file is empty
    if is_file_empty(filename):
        a.writerow(["student id", "roll no", "name", "phone no"])
    
    # Take user input
    studentid = int(input("Enter student id: "))
    rollno = int(input("Enter roll number: "))
    name = input("Enter name: ")
    phoneno = int(input("Enter phone number: "))
    
    # Write data to CSV
    a.writerow([studentid, rollno, name, phoneno])

print("Student record has been saved.")

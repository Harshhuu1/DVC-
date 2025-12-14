import csv

# Data you want to write
data = [
    ["Name", "Age", "City"],
    ["Harsh", 20, "Nagpur"],
    ["Aman", 21, "Pune"],
    ["Riya", 19, "Mumbai"]
]

# Create a CSV file
with open("students.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file created successfully!")

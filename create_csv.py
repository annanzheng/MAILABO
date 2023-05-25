import csv

data = [
    ['Name', 'Age', 'Email'],
    ['John Doe', 25, 'johndoe@example.com'],
    ['Jane Smith', 30, 'janesmith@example.com']
]

with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

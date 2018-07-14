import csv

with open('guests.csv', 'w', newline='') as csvfile:
    fieldnames = ['First Name', 'Last Name', 'Response', 'Guests']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'First Name': 'Raul', 'Last Name': 'Tapia-Martinez', 'Response': 'Yes', 'Guests': '3'})
    writer.writerow({'First Name': 'Abbie', 'Last Name': 'Prescott', 'Response': 'Yes', 'Guests': '3'})

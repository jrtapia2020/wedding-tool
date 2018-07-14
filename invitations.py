import csv

with open('guests.csv', 'w', newline='') as csvfile:
    fieldnames = ['First Name', 'Last Name', 'Response', 'Guests']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'First Name': 'Raul', 'Last Name': 'Tapia-Martinez', 'Response': 'Yes', 'Guests': '3'})
    writer.writerow({'First Name': 'Abbie', 'Last Name': 'Prescott', 'Response': 'Yes', 'Guests': '3'})

# with open('eggs.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile, delimiter=' ',
#                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     writer.writerow(['Spam'] * 5 + ['Baked Beans'])
#     writer.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

# with open('some.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow('Hello World!')
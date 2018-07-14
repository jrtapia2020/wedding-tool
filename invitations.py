#!/usr/bin/env python

import argparse
import csv

# TODO: Figure out what the point of the command line argument is and how to use it properly.
# parser = argparse.ArgumentParser()
# parser.add_argument("--verbose", help="increase output verbosity",
#                     action="store_true")
# args = parser.parse_args()
# if args.verbose:
#     print("verbosity turned on")

# TODO: Find a way to make sure it creates new lines in the CSV file each time the prompt is answered.

print("\n\nGuest Information\n")
first_name = input('First Name: ')
last_name = input('Last Name: ')
response = input('Will you be attending? Yes/No: ')
if response == 'Yes' or 'yes':
    guests = int(input('How many guests (including yourself) will be attending? '))
    print('Information Saved.')
else:
    print('Information Saved.')


def main():
    with open('guests.csv', 'w', newline='') as csvfile:
        fieldnames = ['First Name', 'Last Name', 'Response', 'Guests']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'First Name': first_name, 'Last Name': last_name, 'Response': response, 'Guests': guests})


if __name__ == '__main__':
    main()

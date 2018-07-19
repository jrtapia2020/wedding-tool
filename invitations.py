#!/usr/bin/env python

import argparse
import csv


# TODO: Figure out what the point of the command line argument is and how to use it properly.
# TODO: Find a way to make sure it creates new lines in the CSV file each time the prompt is answered.

def main():
    parser = argparse.ArgumentParser(prog='Invitation Responses')
    parser.add_argument('input')
    args = parser.parse_args()

    # TODO: Where does args.input go? How do I save it to the CSV file?

    print("\n\nGuest Information\n")
    first_name = input('First Name: ')
    last_name = input('Last Name: ')
    response = input('Will they be attending? Yes/No: ')
    guests = int(input('How many guests will be attending? '))
    print('Information Saved.')

    with open('guests.csv', 'w', newline='') as csvfile:
        fieldnames = ['First Name', 'Last Name', 'Response', 'Guests']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'First Name': first_name, 'Last Name': last_name, 'Response': response, 'Guests': guests})

    print(args.input)


if __name__ == '__main__':
    main()

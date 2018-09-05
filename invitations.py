#!/usr/bin/env python

import argparse
import os.path
import csv


# TODO: Find a way to make sure it get rid of the extra line of white space isn't added.

def main() -> None:
    parser = create_parser()
    args = parser.parse_args()

    file_exists = os.path.isfile('guests.csv')

    with open('guests.csv', 'a') as csvfile:
        headers = ['First Name', 'Last Name', 'Response', 'Guest Count']
        writer = csv.DictWriter(csvfile, fieldnames=headers)

        if not file_exists:
            writer.writeheader()  # If the file doesn't exist yet, write a header.

        writer.writerow(
            {'First Name': args.first_name,
             'Last Name': args.last_name,
             'Response': args.response,
             'Guest Count': args.guest_count})

    print('Information Saved.')


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog='Invitation Responses')
    parser.add_argument('first_name', help='First name of guest.')
    parser.add_argument('last_name', help='Last name of guest.')
    parser.add_argument('response', help='Guest response (Yes/No).')
    parser.add_argument('guest_count', help='Number of guests attending (including guest responding).')
    return parser


if __name__ == '__main__':
    main()

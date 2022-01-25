#!/usr/bin/env python3

# Created by: Logan S
# Created on: Jan. 5, 2022
# This program formally gives a Canadian shipping address.

import time
from sys import stdout


def format_address(name, street_num, street, city_name,
                   province_name, postal, apt_num=None):

    address = name
    if apt_num is not None:
        address = (address + "\n" + street_num + " " + street + " " +
                   apt_num + "\n" + city_name + ", " + province_name + "\n"
                   + postal)
    else:
        address = (address + "\n" + street_num + " " + street +
                   "\n" + city_name + ", " + province_name + "\n" + postal)

    return address


def main():

    apt_number = None
    # Assigning the greetings string to a variable
    print("Hello! This program asks for certain parts "
          "of your address to give you a valid "
          "Canadian shipping address.\nDon't worry, "
          "We don't take anything! (We physically can't)")
    print()
    # input
    user_name = input("Enter your name (First and Last):\n> ")
    print()
    user_answer_apt = input("Do you live in an apartment?\n> ")
    if user_answer_apt.upper() == "Y" or user_answer_apt.upper() == "YES":
        print()
        apt_number = input("Please enter the apartment number or code:\n> ")
        print()
    street_number = input("What is your address number for your street?\n> ")
    print()
    street_name = input("What is the name of your street?\n> ")
    print()
    city = input("Which city do you live in?\n> ")
    print()
    province = input("Which province do you live in?\n> ")
    print()
    postal_code = input("What is your Postal Code?\n> ")

    if apt_number is not None:
        complete_address = format_address(user_name, street_number,
                                          street_name, city, province,
                                          postal_code, apt_number)
    else:
        complete_address = format_address(user_name, street_number,
                                          street_name, city,
                                          province, postal_code)
    print()
    print("Your Formal Canadian Shipping address is:")
    for letter in complete_address:
        time.sleep(0.06)  # In seconds
        stdout.write(letter.upper())
        stdout.flush()


if __name__ == "__main__":
    main()

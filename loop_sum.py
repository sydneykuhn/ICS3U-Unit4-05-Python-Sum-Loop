#!/usr/bin/env python3

# Created by: Sydney Kuhn
# Created on: Oct 2020
# This program calculates the sum of positive numbers


def main():
    # this function is a loop
    total = 0

    # input
    number_amount_as_string = input(
        "How many numbers would you like to add together : "
    )

    # process & output
    try:
        number_amount = int(number_amount_as_string)
        for loop_counter in range(number_amount):
            user_input_as_string = input("Enter a number to add : ")
            user_input = int(user_input_as_string)
            if user_input < 0:
                continue
            total += user_input

        print("The sum of just the positive numbers is = {0}".format(total))
    except (Exception):
        print("Invalid number entered, please try again.")

    print("\nDone.")


if __name__ == "__main__":
    main()

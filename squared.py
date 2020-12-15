# Unit 4-03/usr/bin/env python3

# This program was created by Larry Nkengbeza
# This program was created on December 2020
# This program calculates squared.


def main():
    # this function does square root using a for loop.

    # Input
    user_input = int(input("Enter the number you want to be square" +
                           "rooted up to: "))

    # Process
    for loop_counter in range(user_input):
        print("Answer for {0}² is {0}".format(loop_counter))


if __name__ == "__main__":
    main()

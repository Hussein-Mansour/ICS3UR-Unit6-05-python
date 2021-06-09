#!/usr/bin/env python3

# Created by: Hussein Mansour
# Created on: Tue/Jun8/2021
# this program accept marks (0 to 100) repeatedly from the user
# place the values in list, if the user enters "-1"
# calculate average


def cal_average(mark_average):
    # this function calculates the average of the marks

    avg = mark_average[0]

    # adder
    for counter in mark_average:
        avg = avg + counter
    # sum
    total = 0
    for counter_loop in range(0, len(mark_average)):
        total = total + mark_average[counter_loop]
    # process
    process = total / len(mark_average)
    # return
    return process


def main():
    # this function uses list
    mark_list = []
    mark = None

    # guid to user
    print("Please enter 1 mark at a time. Enter -1 to end")
    print("\n")
    # input
    for counter in range(0, len(mark_list)):
        mark = int(input("What is your mark? (as %): "))
        mark_list.append(mark)
    while mark != -1:
        mark = int(input("What is your mark? (as %): "))
        mark_list.append(mark)
    mark_list.pop()  # remove the "-1" that was added
    print("")
    # output
    print("\nThe average is: {0}%".format(cal_average(mark_list)))
    print("\nDone.")


if __name__ == "__main__":
    main()

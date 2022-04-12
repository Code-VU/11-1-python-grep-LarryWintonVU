import re
import string
import sys


def countpatterninfile():
    fileName = 'mbox-long.txt'
    regular_expression = input("Enter a regular expression: ")
    file_handle = open(fileName, mode='r', encoding='utf-8')
    countOfMatchingLines = 0
    for line in file_handle :
        foundList = re.findall(regular_expression, line)
        if (len(foundList) > 0) :
            countOfMatchingLines = countOfMatchingLines + 1
    print(fileName, 'had', countOfMatchingLines, 'lines that matched', regular_expression)


if __name__ == '__main__':
    # this is called a main method
    # This is another way of telling python THIS IS WHERE YOU SHOULD START RUNNING
    # When this is included, python will begin with the code in this block first
    countpatterninfile()
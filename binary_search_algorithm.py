# This is a sample Python script.
from typing import *


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Algorithms and Data structure:
def binary_search_algorithms(sortedList: List, searchItem: Union[AnyStr, int])-> int:
    # or for modern python, use: 
    # def binary_search_algorithms(sortedList: List, searchItem: AnyStr | int):
    # get List length:
    currentLowPos = 0
    currentHighPos = len(sortedList) - 1

    while currentLowPos < currentHighPos:
        currentMidPos = round((currentLowPos + currentHighPos) / 2)
        currentGuessItem = sortedList[currentMidPos]
        if currentGuessItem == searchItem:
            return currentMidPos
        if currentGuessItem > searchItem:
            currentHighPos = currentMidPos - 1
        else:
            currentLowPos = currentMidPos + 1
    return None


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # search through the sorted list and return the position of 5...
    sortedList: List = [1, 3, 5, 7, 9]
    print(binary_search_algorithms(sortedList, 5))

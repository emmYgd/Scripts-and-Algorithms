# This is a sample Python script.
from typing import *


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Algorithms and Data structure:
def QuickSort(givenArray: List) -> List:
    # init:
    global pivot
    lesserThanPivotArray = []
    greaterThanPivotArray = []

    # base case:
    if len(givenArray) < 2:
        return givenArray
    # recursive case
    else:
        pivot = givenArray[0]
        # one liner in python list comprehension:
        # less = [eachElem for eachElem in givenArray[1:] if eachElem <= pivot]

        # conventional programming style:
        for eachElem in givenArray[1:]:
            if eachElem <= pivot:
                lesserThanPivotArray.append(eachElem)

        # one liner in python list comprehension:
        # greater = [eachElem for eachElem in givenArray[1:] if eachElem > pivot]

        # conventional programming style:
        for eachElem in givenArray[1:]:
            if eachElem > pivot:
                greaterThanPivotArray.append(eachElem)

        # return sorted:
        recursiveLeft = QuickSort(lesserThanPivotArray)
        recursiveRight = QuickSort(greaterThanPivotArray)
        sortedList = recursiveLeft + [pivot] + recursiveRight

        return sortedList

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # print(binary_search_algorithms([1, 3, 5, 7, 9], 5))
    print(QuickSort([10, 5, 2, 3]))

# Author: Adam Jeffries
# Date: 2/9/2021
# Description: A recursive function named row_puzzle that takes a list of integers as a parameter
# and returns True if the puzzle is solvable for a given row, but returns False otherwise.

def row_puzzle(row, index = 0, shifts_taken = [], indexes_used = []):

    if (index == len(row) - 1):
        return True

    shiftAmount = row[index]

    if (index + shiftAmount <= len(row) - 1 and (index, shiftAmount) not in shifts_taken and index + shiftAmount not in indexes_used):
        indexes_used.append(index + shiftAmount)
        shifts_taken.append(index, shiftAmount)
        return row_puzzle(row, index + shiftAmount, shifts_taken, indexes_used)
    elif(index - shiftAmount >= 0) and (index, -shiftAmount) not in shifts_taken:
        shifts_taken.append(index, -shiftAmount)
        return row_puzzle(row, index - shiftAmount, shifts_taken, indexes_used)
    else:
        return False
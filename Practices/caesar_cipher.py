# WH 2nd caeser cipher program

# define a function that can ofset a letter by a number
def caeserOffSet(letter,off_set):
    # set Num to Off_set
    num = off_set
    # repeat for evry lower case letter and set Let to the curent letter
    for let in "bcdefghijklomnpqrstuvwxyza":
        # add one to Num
        num += 1
        # check if Letter = Let
        if letter == let:
            # give an output of num but is loops around from 26 and add 27 num but is loops around from 26
            return num%26 + 1
    # repeat for evry upper case letter and set Let to the curent letter
    for let in "BCDEFGHIJKLOMNPQRSTUVWXYZA":
        # add one to Num
        num += 1
        # check if Letter = Let
        if letter == let:
            # give an output of num but is loops around from 26 and add 27
            return num%26 + 27

# define a function that can make a number in to a letter
def numToLetter(number):
    # set Num to 0
    num = 0
    # repeat for evry lower and upper case letter and set Let to the curent letter
    for let in "abcdefghijklomnpqrstuvwxyzABCDEFGHIJKLOMNPQRSTUVWXYZ":
        # add one to Num
        num += 1
        # check if Number = Num
        if number == num:
            # return Let
            return let
# defines a function that encode a masage
def encoder(message,off_set):
    # set Fine_message as a string
    fine_message = ""
    # a loop of each letter in in Message and the letter is Let
    for let in message:
        #add function numToLetter with function caeserOffSet with Letter as let and Off_set and Off_set as Number to Fine_message
        fine_message += numToLetter(caeserOffSet(let,off_set))
    #return fine_massage
    return fine_message

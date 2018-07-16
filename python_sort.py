# This program excepts a data file containing a list of random integer numbers, the goal is read the file and print out:
# The sum and average of all values
# The first 10 values in the array
# The first 10 values in descending order
# The last 10 values in the array
#

# STAGE1: D level Program

# while loop to except the file as being read or not
while True:
    # try statement to open file and close
    try:
        # assign a variable to open and read the file
        numberFile = open("FinalData.Data", 'r')
        # create a variable to read the file while removing whitespaces
        numberText = numberFile.read().splitlines()
        # create and empty List for each number text
        numberList = []
        # for loop to read each line and add to list in numberfile
        for eachline in numberText:
            # append eachline as an integer into the numberList
            numberList.append(int(eachline))
        # Close number File
        numberFile.close()
        # print file read complete statement
        print("File Read Complete")
        # break out of while loop
        break
    # except statement to handle if the file cannot be read
    except:
        # printfile not complete statement
        print("File Not Complete")
        # break out of while loop
        break


# funtion to find the sum and average values in numberlist
def calculateList(numberList):
    # accumulator to add the values in the list
    addNum = 0
    # for loop to add the values in the list
    for i in numberList:
        addNum += i
        # for loop to get the average values in the list
    avgNum = int(addNum / len(numberList))
    # return tuple
    return (addNum, avgNum)


# Return a tuple from the function
addNum, avgNum = calculateList(numberList)

# print sum and average statement , float the average value in the list
print()
print("ORIGINAL LIST")
print("The sum of the values in the list is", addNum)
print("The average values in the array is", float(avgNum))
print()


# STAGE2: C level program

# function will print the first ten elements of the array
def firstTen(numberList):
    firstList = numberList[0:10]
    print("The first 10 indexes in the array:")
    print(firstList)
    print()
    firstList.sort()
    firstList.reverse()
    print("The first 10 from highest to lowest):")
    print(firstList)
    print()
    return firstList


# function that will print the last ten elements of the array
def lastTen(numberList):
    # assign new variable for the last 10 indexes in the list
    lastList = numberList[-10:]
    # print statement
    print("The last 10 indexes in the array:")
    print(lastList)
    print()
    # sort the list
    lastList.sort()
    # reverse the list from highest to lowest
    lastList.reverse()
    # print descending order list
    print("The last 10 from highest to lowest:")
    print(lastList)
    print()
    # return the last list
    return lastList


# Assign a variable and execute the function for the first 10 in the array
firstList = firstTen(numberList)
# Execute the function for the last 10 in the array
lastList = lastTen(numberList)

# STAGE 3: B Level Program
'''randomList=[9047, 7840, 9520, 5228, 7669, 2167, 5287, 8096, 5373]'''


# This method takes any integer and reduce to an odd number by dividing it in half until it becomes an
# odd number
def makeOdd(numberList):
    # create a new reduce List
    reduceList = []
    # for loop to go through the original List
    for i in numberList:
        # while each index is an even number until it is the lowest odd number that cannot be divided
        while int(i) % 2 == 0:
            # divide even index by 2
            i = i / 2
        # once at lowest odd number append to new reduce list
        reduceList.append(i)
        # if statement when each index number is odd
        if int(i) % 3 == 0:
            # index number is odd add to new reduce list
            reduceList.append(i)
    # return new reduce List
    return reduceList


# execute the function, assign variable as reduce List
reduceList = makeOdd(numberList)

# print(reduceList)

# execute the new sum and average of the new reduce List
addNum2, avgNum2 = calculateList(reduceList)

# print new sum and average statement
print("REDUCED LIST")
print("The new sum of the List is:", addNum2)
print("The new average of the List is:", avgNum2)
print()

# execute and print the function for the first ten indexes in reduceList
reduceFirst = firstTen(reduceList)
# execute and print the function for the last ten indexes in reduceList
reduceLast = lastTen(reduceList)

# STAGE 4: A Level Program

# Global variables to analyze the index in the list
odd = 1
even = 0

# while loop to continuously go through the list until it ends
while True:
    try:
        # if the first index value is greater than or equal to the second index value
        if reduceList[even] >= reduceList[odd]:
            # odd index move to next index
            odd += 1
            # even index move to the next index
            even += 1
        # if the index is smaller than the next index
        elif reduceList[even] < reduceList[odd]:
            # delete the smaller index
            del reduceList[even]
            # move back one index
            odd -= 1
            # move back one index
            even -= 1
        # this if statement ensures neither index goes below 0 or -1
        if odd == 0 and even == -1:
            odd += 1
            even += 1
    # except statement to handle the index error then to break the while loop
    except IndexError:
        # break out of while loop
        break

# print removal list summary
print("Your REMOVAL LIST after the entire Reduced List is:")
# print removal List
print(reduceList)

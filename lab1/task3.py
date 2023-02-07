from task2 import jainsall

# initialize an empty list to store values from file
numbers_from_file=[]

# opening the file
with open("lab1/valuesTask3.txt") as file:
    # reading the file line by line
    for line in file:
        # extract the numeric value from line
        value = int(line.strip().split()[0])

        # append the value to the list
        numbers_from_file.append(value)


# print JFI value using jainsall function from task2
print("JFI value: ", jainsall(numbers_from_file))


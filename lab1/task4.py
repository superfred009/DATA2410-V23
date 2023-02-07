from task2 import jainsall

# initialize an empty list to store values from file
numbers_from_file=[]

# opening the file
with open("lab1/valuesTask3.txt") as file:
    # reading the file line by line
    for line in file:
        # splitting each line to value and unit
        value = int(line.strip().split()[0])
        unit = line.strip().split()[1]

        # converting numbers to bits based on unit
        if unit == "Mbps":
            value *= 1000000
        elif unit == "Kbps":
            value *= 1000

        # append the value to the list
        numbers_from_file.append(value)

# print JFI value using jainsall function from task2
print("JFI value: ", jainsall(numbers_from_file))
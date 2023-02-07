# Making a function that calculates the Jains fairness index for a list of input values
# The formula is (sum(throughputValues))^2 / (N * (sum og each throughput value squared))
def jainsall(throughput_list):

    # Summing all the throughput values
    throughput_sum = sum(throughput_list)

    # Using the sum of throughput values to calculate the JFI as numinator
    # and len function to calculate N for denuminator
    # Also need to sum the squared throughput values and multiply by N
    JFI = throughput_sum**2 / (len(throughput_list) * sum([x**2 for x in throughput_list]))

    return JFI

# Testing the function
throughput_list = [1, 2, 3, 4, 5]
JFI = jainsall(throughput_list)
print("Jains list of throughput values: ", JFI)

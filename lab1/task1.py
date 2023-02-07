# Making a function that calculates the Jains fairness index for two input values
# The formula is (throughput1 + throughput2)^2 / (N * (throughput1^2 + throughput2^2))
def jains(throughput1, throughput2): 

    # Making the JFI formula
    # Numinator is sum of thoughputs squared
    numinator = (throughput1 + throughput2)**2

    # Denuminator is N=2 times the sum of thoughputs squared
    denuminator = 2 * (throughput1**2 + throughput2**2)

    # Dividing the numinator by the denuminator to finish the formula
    JFI = numinator / denuminator 

    return JFI

# Testing the function
throughput1 = 1
throughput2 = 2
JFI = jains(throughput1, throughput2)
print("Jains two throughput values: ", JFI)
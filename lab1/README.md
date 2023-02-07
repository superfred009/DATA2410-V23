# Tasks for lab 1

# 1 Introduction

Fairness measures or metrics are used in computer networks to determine whether users or applications
are receiving a fair share of system resources. Commonly, the throughput of competing transfers
(“flows”) is measured in experiments or obtained via simulations, and they are used to calculate Jains
Fairness Index (JFI) [1], using the formula:

image.png

Here, N is the total number of flows, and xi(t) is the throughput of the ith connection — the
output ranges from 1/N to 1 where the value 1 indicates that all flows get the same allocation.

# 2 Task 1

Write a function named jains that takes two throughput values (int and/or float) as arguments and
returns a JFI.

# 3 Task 2

Write a new function jainsall function that takes a list of throughput values (integers and/or float)
and returns a JFI.

# 4 Task 3

Read the throughput values from a file and then use your jainsall function to calculate a JFI.
The text file contains:
7 Mbps
12 Mbps
15 Mbps
32 Mbps
You should only consider the numeric values.
1

# 5 Task 4

Read the throughput values from a file and then use your jainsall function to calculate a JFI. Note:
you must use the same units.
The text file contains:
7 Mbps
1200 Kbps
15 Mbps
32 Mbps

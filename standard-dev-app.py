import math

# Your values
data_input = input("Please enter your values, separated by commas: ")

# Convert the input string to a list of floats
data = [float(x) for x in data_input.split(',')]

# Mean of the data numbers
mean = sum(data) / len(data)

# Median of the data numbers
data.sort()
n = len(data)
if n % 2 == 0:
    median = (data[n // 2 - 1] + data[n // 2]) / 2
else:
    median = data[n // 2]

# Variance of the data numbers
variance = sum((x - mean) ** 2 for x in data) / len(data)

# Standard deviation of the data numbers
std_dev = math.sqrt(variance)

# Range of data within 68% of the mean
lower_bound = mean - std_dev
upper_bound = mean + std_dev
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_dev}")
print(f"Range of data within 68% of the mean: {lower_bound} to {upper_bound}")

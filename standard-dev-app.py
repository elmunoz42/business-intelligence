import math

# Your sales numbers
sales_input = input("Please enter your sales numbers, separated by commas: ")

# Convert the input string to a list of floats
sales = [float(x) for x in sales_input.split(',')]

# Mean of the sales numbers
mean = sum(sales) / len(sales)

# Variance of the sales numbers
variance = sum((x - mean) ** 2 for x in sales) / len(sales)

# Standard deviation of the sales numbers
std_dev = math.sqrt(variance)

# Range of sales within 68% of the mean
lower_bound = mean - std_dev
upper_bound = mean + std_dev

print(f"Standard Deviation: {std_dev}")
print(f"Range of sales within 68% of the mean: {lower_bound} to {upper_bound}")

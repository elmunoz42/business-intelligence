import math

# Your sales numbers
sales = [2, 8, 11, 8, 12, 13, 15, 15, 11, 14, 13.75, 18, 20, 21, 25]

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

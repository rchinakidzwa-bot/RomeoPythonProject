import random

random_numbers = []

# Generate five random floating-point numbers
for number in range(5):
    random_value = random.uniform(0, 10)
    random_numbers.append(random_value)

print("Generated numbers:")

for number in random_numbers:
    print(f"{number:.2f}")

# Use built-in functions to find the minimum and maximum
minimum_value = min(random_numbers)
maximum_value = max(random_numbers)

print(f"\nMinimum value: {minimum_value:.2f}")
print(f"Maximum value: {maximum_value:.2f}")
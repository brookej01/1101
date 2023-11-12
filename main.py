# Read numbers from one_hundred.txt
with open('one_hundred.txt', 'r') as file:
    lines = file.readlines()

# Extract numbers as integers
numbers = [int(line.strip()) for line in lines if line.strip().isdigit()]

# Determine missing numbers
missing_numbers = set(range(1, 101)) - set(numbers)

# Combine numbers and missing_numbers, then sort
result_numbers = sorted(numbers + list(missing_numbers))

# Write sorted numbers to one_hundred_sorted.txt
with open('one_hundred_sorted.txt', 'w') as file:
    for number in result_numbers:
        file.write(str(number) + '\n')

print("Sorted numbers written to one_hundred_sorted.txt")
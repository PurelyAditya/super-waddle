nums = [1, 4, 9, 25, 36, 49, 64, 81, 100]

# First approach
i = 0
found_count = 0
while i < len(nums):
    if nums[i] == 36:
        print("Found number 36 at index", i)
        found_count += 1  # Increment the counter when the number is found
    i += 1

if found_count == 0:
    print("Number 36 not found")

# Second approach
x = int(input("Enter the number: "))

i = 0
found_count = 0
while i < len(nums):
    if nums[i] == x:
        print(f"Number {x} found at index {i}")
        found_count += 1  # Increment the counter when the number is found
    i += 1

if found_count == 0:
    print(f"Number {x} not found")

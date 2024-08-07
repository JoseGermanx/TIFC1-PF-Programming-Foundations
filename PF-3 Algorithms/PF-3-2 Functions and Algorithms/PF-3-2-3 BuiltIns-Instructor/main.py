# A simple list of numbers
numbers = [2.4, 4.3, 6.1, 8, 10, 11.1]

# Adding the numbers manually
print( numbers[0]
     + numbers[1]
     + numbers[2]
     + numbers[3]
     + numbers[4]
     + numbers[5])

# Adding the numbers using the built-in sum() function
# print(sum(numbers))

# Finding the largest number manually
largest = 0
for number in numbers:
  if number > largest:
    largest = number
print(largest)

# Finding the largest number using the built-in max() function
# print(max(numbers))

# Rounding a number manually
if largest == int(largest):
  print(largest)
elif largest > int(largest) and (largest - 0.5) > int(largest):
  print(int(largest) + 1)
else:
  print(int(largest))

# Rounding a number using the built-in round() function
# print(round(largest))
### TODO Given the list, output the item that repeats the most
list = [1, 5, 7, 11, 12, 5, 55, 3, 22, 11, 5, 1, 2]
counter = 0
number = 0


for num in list:
    # Use count function to determine how many times an item in the list is repeated
    repeated_num = list.count(num)
    # Check against the counter to see if the item is repeated more
    if repeated_num > counter:
        # If the item is repeated more than the counter, set the counter to the repeated amount
        counter = repeated_num
        # Assign the item to the number variable
        number = num

print(number)

### convert to function and try to use list comprehension

# FIZZBUZZ SOLUTION_2 #
output = ""  # Creates empty output string.
for num in range(1, 101):  # Defines range of 1-101.
    if num % 3 == 0:  # Checks if number is divisible by 3.
        output += "Fizz"  # Adds Fizz to output string.
    if num % 5 == 0:  # Checks if number is divisible by 5.
        output += "Buzz"  # Adds Buzz to output string.
    if not output:  # Adds number to output string if no condition is true.
        output = num
    print (output)  # Prints output.
    output = ""  # Clears output string ready for next iteration.

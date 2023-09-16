for num in range(1, 101):  # Defines range of 1-100.
    if num % 15 == 0:  # Checks if number is divisible by 15 with no remainder (divisible by 3 and 5).
        print("FizzBuzz")  # Outputs FizzBuzz
    elif num % 3 == 0:  # Checks if number is divisible by 3.
        print("Fizz")  # Outputs Fizz
    elif num % 5 == 0:  # Checks if number is divisible by 5.
        print("Buzz")  # Outputs Buzz
    else:
        print(num)  # Outputs the number if no condition is met.

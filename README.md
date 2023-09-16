# FizzBuzz
Two solutions to the classic "FizzBuzz" problem.

Solution One outputs the three possibilities seperately: "FizzBuzz" if divisible by 15 (3 and 5), "Fizz" if divisible by 3 only, and "Buzz" if divisible by 5 only.
This solution is simple and correct, but is less maintainable.

Solution Two uses a string, and only has two possibilities: "Fizz" if divisible by 3, and "Buzz" if divisible by 5 (in that order). If condition is true, then "Fizz" or "Buzz" is added to the string, and the string is outputted. If both are true, then both will be added to the string, and will output "FizzBuzz", without having to create a seperate possibility. 

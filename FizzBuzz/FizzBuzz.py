fizzBuzz = ['fizzbuzz' if num % 15 == 0 else
            'fizz' if num % 3 == 0 else
            'buzz' if num % 5 == 0 else
            num for num in range(1, 101)]
print(fizzBuzz)
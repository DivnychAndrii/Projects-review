def fibonacci():

    x, y = 0, 1
    all_numbers = [0]
    while y <= 4000000:
        all_numbers.append(y)
        x, y = y, x+y

    summary = 0
    for num in all_numbers:

        if num % 2 == 0:
            summary += num
    return summary

print(fibonacci())
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368,
# 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578]

# result is 4613732


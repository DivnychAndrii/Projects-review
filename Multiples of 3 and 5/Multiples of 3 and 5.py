
def multiples(num):
    summary = 0
    for number in range(num):
        if number % 3 == 0 or number % 5 == 0:
            summary += number
    return summary


print(multiples(1000))


# result of this is 233168
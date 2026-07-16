def primeComposite(number):
    if number <= 1:
        return "neither prime nor composite"
    if number == 2:
        return "prime"
    if number % 2 == 0:
        return "composite"

    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            return "composite"
        divisor += 2

    return "prime"


num = int(input("Enter a number: "))
result = primeComposite(num)
print(f"{num} is {result}.")

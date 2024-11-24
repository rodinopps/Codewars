def fizzbuzz(n):
    new = []
    for i in range(1, n + 1):
        if i % 15 == 0: new.append("FizzBuzz")
        elif i % 5 == 0: new.append("Buzz")
        elif i % 3 == 0: new.append("Fizz")
        else: new.append(i)
    return new

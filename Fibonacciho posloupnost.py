def fibonacci(n):
    if n <= 0:
        return "Zadejte kladné číslo."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

n = int(input("Zadejte číslo n: "))
print(f"{n}-tý člen Fibonacciho posloupnosti je: {fibonacci(n)}")
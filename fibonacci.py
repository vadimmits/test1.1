def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Введіть номер числа Фібоначчі, яке ви хочете розрахувати
n = int(input("Введіть номер числа Фібоначчі: "))
result = fibonacci_recursive(n)
print(f"Число Фібоначчі під номером {n} дорівнює {result}")

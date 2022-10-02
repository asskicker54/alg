def tribonacci(n):
    if (n == 1 or n == 0):
        return 0
    elif (n == 2):
        return 1
    else: #Рекурсивный
        return (tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3))

n = int(input("n: "))
print(tribonacci(n))
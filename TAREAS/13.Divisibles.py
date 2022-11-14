numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

divisible = lambda x: x % 3 == 0

num_div = filter (divisible, numeros)

print(list(num_div))
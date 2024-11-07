numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
number = 0
count = 0

for count in range(len(numbers)):
    is_prime = True
    number = numbers[count]
    if number < 2:
        print(number, 'не относится к спискам')
        continue
    else:
        f = number ** (1 / 2)
    for a in range(2, int(f + 1)):
        if number % a == 0:
            is_prime = False
            break
    if not (is_prime):
        not_primes.append(number)
    else:
        primes.append(number)
is_prime = True
print('Простые числа', primes)
print('Составные числа', not_primes)
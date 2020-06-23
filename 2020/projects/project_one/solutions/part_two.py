def divisible_by(number, factor):
    return number % factor == 0


def factors(number):
    f = []

    i = 1
    while i <= number ** .5:
        if divisible_by(number, i):
            f.append(i)
            f.append(number / i)

        i += 1

    return f


def is_prime(number):
    return len(factors(number)) == 2


def prime_factors(number):
    f = factors(number)

    p_f = []

    i = 0

    while i < len(f):
        if is_prime(f[i]):
            p_f.append(f[i])

        i += 1

    return p_f


def max_in_list(l):
    i = 0

    m = 0

    while i < len(l):
        if l[i] > m:
            m = l[i]

        i += 1

    return m

print(max_in_list(prime_factors(600851475143)))

# sum_of_squares(number)
#    Returns the sum of the squares for 1 --> number
# square_of_sums(number)
#    Returns the square of the sums of 1 --> number

def sum_of_squares(number):
    t_sum_of_squares = 0

    for i in range(1, number + 1):
        t_sum_of_squares += i ** 2

    return t_sum_of_squares


def square_of_sums(number):
    s = 0

    for i in range(1, number + 1):
        s = s + i

    return s ** 2

print(square_of_sums(10) - sum_of_squares(10))
print(square_of_sums(100) - sum_of_squares(100))

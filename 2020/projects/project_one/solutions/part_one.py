def divisible_by(number, factor):
    return number % factor == 0

def multiples_lt(root, number):
    multiples = []

    for i in range(1, number):
        if divisible_by(i, root):
            multiples.append(i)

    return multiples

def multiple_multiples_lt(root_one,
                          root_two,
                          number):
    root_one_multiples = multiples_lt(root_one, number)
    root_two_multiples = multiples_lt(root_two,number)

    new_multiples = []


    for element in root_one_multiples:
        if not element in new_multiples:
            new_multiples.append(element)

    for element in root_two_multiples:
        if not element in new_multiples:
            new_multiples.append(element)

    return new_multiples

def sum_of_list(l):
    to_return = 0

    for i in l:
        to_return += i

    return to_return

# ANSWER #
print(
    sum_of_list(
        multiple_multiples_lt(
            3, 5, 1000
        )
    )
)

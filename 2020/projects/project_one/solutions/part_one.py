def divisible_by(number, factor):
    return number % factor == 0

def multiples_lt(root, number):
    multiples = []

    i = 1
    while i < number:
        if divisible_by(i, root):
            multiples.append(i)

        i += 1

    return multiples


def multiple_multiples_lt(root_one, root_two, number):
    root_one_multiples = multiples_lt(root_one, number)
    root_two_multiples = multiples_lt(root_two, number)

    new_multiples = []

    i = 0
    while i < len(root_one_multiples):
        element = root_one_multiples[i]
        if not element in new_multiples:
            new_multiples.append(element)
        i += 1

    i = 0
    while i < len(root_two_multiples):
        element = root_two_multiples[i]
        if not element in new_multiples:
            new_multiples.append(element)
        i += 1

    return new_multiples


def sum_of_list(l):
    i = 0

    to_return = 0

    while i < len(l):
        to_return += l[i]

        i += 1

    return to_return

# ANSWER #
print(sum_of_list(multiple_multiples_lt(3, 5, 1000)))
